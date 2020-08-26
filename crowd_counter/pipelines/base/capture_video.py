import cv2
from .pipeline import Pipeline
from .utils.file_video_capture import FileVideoCapture

class Capture(Pipeline):
    '''
    Pipeline to capture video frames 
    '''

    def __init__(self, src, skip_frame=1):
        '''
        Args
            src: video path
        '''

        self.cap = FileVideoCapture(src = src, skip_frame=skip_frame)
        self.cap.start() # --> start reading video frames from another thread
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS)) # get current video fps
        self.frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) # frame shape
        
        self.frame_count = 0 # use to label frame id
        self.skip_frame = skip_frame

        super().__init__()

    def generator(self):
        """Yield captured frames and pass to next pipeline step"""

        while self.cap.running():
            image = self.cap.read()

            # Create metadata to store frame info
            data = {
                # "frame_num" : self.frame_count,
                "frame_id" : f"{self.frame_count:05d}",
                "frame_data": image,
            }
            
            self.frame_count += self.skip_frame

            if self.filter(data):
                yield self.map(data)
            
    def cleanup(self):
        """Terminate video capture"""
        self.cap.stop()

