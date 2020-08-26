import cv2 
import os
from .pipeline import Pipeline

class Writer(Pipeline):
    def __init__(self, save_path, fps=30, fourcc='MJPG'):
        self.save_path = save_path
        self.fps = fps 
        self.fourcc = fourcc 
        self.writer = None
        super().__init__()

    def map(self, data):
        frame = data['frame_data'] 

        if self.writer is None:
            h, w = frame.shape[:2]
            self.writer = cv2.VideoWriter(
                filename = self.save_path,
                fourcc=cv2.VideoWriter_fourcc(*self.fourcc),
                fps=self.fps,
                frameSize=(w, h),
                isColor=(frame.ndim == 3)
            )

        self.writer.write(frame)
    
        return data  
    
    def cleanup(self):
        if self.writer:
            self.writer.release()
    
