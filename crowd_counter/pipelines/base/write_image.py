import cv2 
import os
import PIL.Image as Image

from .pipeline import Pipeline
from .utils import draw_heatmap_on_image

class ImageWriter(Pipeline):
    def __init__(self, save_path, img_type='jpg'):
        self.save_path = save_path
        super().__init__()

    def map(self, data):
        heatmap = data['frame_heatmap']
        save_img = draw_heatmap_on_image(data['frame_data'], heatmap, 0.6)
        # pil_img = Image.fromarray(save_img)
        save_img.save(self.save_path)
    
        return data  
    