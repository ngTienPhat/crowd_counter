import cv2
from .pipeline import Pipeline
from .utils.file_video_capture import FileVideoCapture

class CaptureVideo(Pipeline):
    '''
    Pipeline to capture video frames 
    '''

    def __init__(self, src=None, skip_frame=1):
        '''
        Args
            src: video path
        '''
        self.skip_frame = skip_frame
        
        if src is not None:
            self.setup(src)
        # self.start_capturing() # --> start reading video frames from another thread

        super().__init__()



    def start_capturing(self):
        self.cap.start()


    def setup(self, video_path: str):
        self.cap = FileVideoCapture(src = video_path, skip_frame = self.skip_frame)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS)) # get current video fps
        self.frame_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
                            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) # frame shape
        self.frame_count = 0 # use to label frame id
        self.start_capturing()

    def generator(self):
        """Yield captured frames and pass to next pipeline step"""
        assert self.cap is not None, "Video Capture instance must be installed first"


        while self.cap.running():
            image = self.cap.read()

            # Create metadata to store frame info
            data = {
                # "frame_num" : self.frame_count,
                "frame_id" : f"{self.frame_count:05d}",
                "frame_data": image,
                "fps": self.fps,
            }
            
            self.frame_count += self.skip_frame
            yield data
            # if self.filter(data):
            #     yield self.map(data)
            
    def cleanup(self):
        """Terminate video capture"""
        self.cap.stop()

