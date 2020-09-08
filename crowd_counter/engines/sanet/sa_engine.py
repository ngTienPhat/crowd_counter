from .network import SANet
from .network import (
    load_img, 
    gen_x_y, 
    fix_singular_shape,
    generate_output_with_specific_colormap,
)
from crowd_counter.engines import BaseEngine

import numpy as np
import cv2 
import os

# MODEL_CONFIG_DICTIONARY = {
#     "crowd_counter_sanet": {
#         "package": "sanet",
#         "module": ""
#     }
# }

class SA_Engine(BaseEngine):
    def __init__(self, input_shape = (None, None, 3), weight_path=None):
        super(SA_Engine, self).__init__()
        self.__construct_model()
        if weight_path is not None:
            self.load_weight(weight_path)

    def __construct_model(self, input_shape = (None, None, 3)):
        self.model = SANet(input_shape=input_shape, IN=False)

    def load_weight(self, weight_path: str):
        self.model.load_weights(weight_path)

    def __preprocess_input_image(self, frame, image_size=None):
        if image_size is not None:
            frame = frame.resize(image_size)
        
        frame = load_img(frame)
        frame = fix_singular_shape(frame)
        frame = np.expand_dims(frame, axis=0)

        return frame

    def __postprocess_prediction(self, pred, output_map):
        pred = np.squeeze(pred)
        # pred = generate_output_with_specific_colormap(pred, output_map)

        return pred

    def _process(self, frame, image_size = None, output_map='COLORMAP_HOT'):
        frame = self.__preprocess_input_image(frame, image_size)
        pred = self.model.predict(frame)        
        pred = self.__postprocess_prediction(pred, output_map)
        
        boxes = None
        return boxes, pred

