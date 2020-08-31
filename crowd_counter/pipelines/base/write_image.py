import cv2 
import os
import PIL.Image as Image

from .pipeline import Pipeline
from .utils import draw_heatmap_on_image

class ImageWriter(Pipeline):
    def __init__(self, save_path=None, img_type='jpg'):
        self.save_path = save_path
        self.img_type = img_type
        super().__init__()

    def set_save_path(self, save_path: str):
        self.save_path = save_path

    def set_img_type(self, img_type='jpg'):
        self.set_img_type = img_type

    def map(self, data):
        heatmap = data['frame_heatmap']
        save_img = draw_heatmap_on_image(data['frame_data'], heatmap, 0.6)
        # pil_img = Image.fromarray(save_img)
        save_img.save(self.save_path)
    
        return data  
    