import PIL.Image as Image
import cv2
import numpy as np
from .pipeline import Pipeline


class CaptureImage(Pipeline):
    def __init__(self, img_data):
        '''
        Args:
            img_path: image dir or image numpy instance
        '''
        self.src = img_data
        super().__init__()

    def __load_image(self):
        if isinstance(self.src, str): # img_data is image path
            return np.asarray(Image.open(self.src)) 
        else:
            return self.src

    def generator(self):
        
        data = {
            'frame_data': self.__load_image()
        }
        # print(data['frame_data'].shape)
        if self.filter(data):
            yield self.map(data)

    

