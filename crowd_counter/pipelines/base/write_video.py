import cv2 
import os
import numpy as np
import PIL.Image as Image

from .pipeline import Pipeline
from .utils import draw_heatmap_on_image

class VideoWriter(Pipeline):
    def __init__(self, save_path = None, fps=30, fourcc='MP4V'):
        self.save_path = save_path
        self.fps = fps 
        self.fourcc = fourcc 
        self.writer = None
        super().__init__()

    def reset_writer(self):
        self.writer=None

    def set_save_path(self, save_path: str):
        self.save_path = save_path
        self.reset_writer()

    def map(self, data):
        assert self.save_path is not None, "save path has not been declared yet"

        frame = data['frame_data'] 
        h, w = frame.shape[:2]
        heatmap = data['frame_heatmap']
        save_img = draw_heatmap_on_image(frame, heatmap, 0.6)

        fps = self.fps
        if "fps" in data.keys():
            fps = data['fps']

        if self.writer is None:    
            self.writer = cv2.VideoWriter(
                filename = self.save_path,
                fourcc=cv2.VideoWriter_fourcc(*self.fourcc),
                fps=fps,
                frameSize=(w, h),
                isColor=(frame.ndim == 3)
            )

        self.writer.write(np.asarray(save_img))
    
        return data  
    
    def cleanup(self):
        if self.writer:
            self.writer.release()
    
