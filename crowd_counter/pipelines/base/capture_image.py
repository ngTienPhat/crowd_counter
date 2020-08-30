import PIL.Image as Image
import cv2
import numpy as np
from .pipeline import Pipeline


class CaptureImage(Pipeline):
    def __init__(self, img_data=None):
        '''
        Args:
            img_path: image dir or image numpy instance
        '''
        self.src=None
        self.load_image(img_data)
        super().__init__()

    def load_image(self, src):
        if isinstance(src, str): # img_data is image path
            self.src = np.asarray(Image.open(src)) 
        elif isinstance(src, Image.Image):
            self.src = np.asarray(src)
    

    def generator(self):
        assert self.src is not None, "source image has not been loaded yet"
        data = {
            'frame_data': self.src
        }
        # print(data['frame_data'].shape)
        if self.filter(data):
            yield self.map(data)

    

