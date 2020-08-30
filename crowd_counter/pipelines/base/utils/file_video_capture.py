import cv2
import time

from threading import Thread
from queue import Queue


class FileVideoCapture(object):
    """Video file capturing class utilizing threading and the queue to obtain FPS speedup."""

    def __init__(self, src, transform=None, queue_size=128, name="FileVideoCapture", skip_frame=1):
        '''
        Args:
            src: video path
            transform: transform object to apply to a specific frame. None: won't do anything
            queue_size: max number of buffer to store all frames of the given video
            skip_frame: default = 1 (cap all frames)
        '''
        
        self.cap = cv2.VideoCapture(src)
        if not self.cap.isOpened():
            raise IOError(f"Cannot open video {src}")

        self.transform = transform

        # initialize the queue used to store frames read from the video file
        self.queue = Queue(maxsize=queue_size)

        # initialize the variable used to indicate if the thread should be stopped
        self.stopped = False

        # initialize thread
        self.thread = Thread(target=self.update, args=(), name=name)
        self.thread.daemon = True

        self.skip_frame = skip_frame

    def start(self):
        # start a thread to read frames from the file video stream
        self.thread.start()
        return self

    def get(self, cv2_prop):
        return self.cap.get(cv2_prop)

    def update(self):
        # keep looping through video frames
        frame_id = -1
        while self.cap.isOpened():
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                break

            # otherwise, ensure the queue has room in it
            if not self.queue.full():
                # read the next frame from the file
                (grabbed, frame) = self.cap.read()
                
                # if the `grabbed` boolean is `False`, then we have reached the end of the video file
                if not grabbed:
                    self.stopped = True
                    break
                
                # else: increase frame_id by 1 unit
                frame_id+=1
                
                if frame_id%self.skip_frame:
                    continue

                if self.transform:
                    frame = self.transform(frame)

                # add the frames to the queue
                
                self.queue.put(frame)
            else:
                time.sleep(0.001)  # Rest for 1ms, we have a full queue

        self.cap.release()

    def read(self):
        # return next frame in the queue
        return self.queue.get()

    def running(self):
        return self.more() or not self.stopped

    def more(self):
        # return True if there are still frames in the queue. If stream is not stopped, try to wait a moment
        tries = 0
        while self.queue.qsize() == 0 and not self.stopped and tries < 5:
            time.sleep(0.001)
            tries += 1

        return self.queue.qsize() > 0

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
        # wait until stream resources are released (producer thread might be still grabbing frame)
        self.thread.join()
