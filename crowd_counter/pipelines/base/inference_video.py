import sys
import json

from .pipeline import Pipeline 
from crowd_counter.engines import EngineFactory

import cv2
import logging
import numpy as np
logger = logging.getLogger(__name__)


def generate_output_with_specific_colormap(pred, colormap_type='COLORMAP_HOT'):

    gray_pred = np.array(pred*255/pred.max(), dtype = np.uint8)
    
    if colormap_type == 'COLORMAP_HOT':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_HOT)
    if colormap_type == 'COLORMAP_COOL':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_COOL)
    if colormap_type == 'COLORMAP_HSV':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_HSV)
    if colormap_type == 'COLORMAP_AUTUMN':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_AUTUMN)
    if colormap_type == 'COLORMAP_INFERNO':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_INFERNO)
    if colormap_type == 'COLORMAP_MAGMA':
        heatmap = cv2.applyColorMap(gray_pred, cv2.COLORMAP_MAGMA)
    
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    return heatmap

class Predictor(Pipeline):
    '''
    Create a predictor for the current task. 
    Args:
        model_config: information used to create model or path to json file
    '''

    def __init__(self, model_config=None):
        self.engine = None
        if model_config is not None:
            self.engine = self.create_engine(model_config)
        
        super().__init__()

    def create_engine(self, model_config):
        '''
        Args:
            model_config (str|dict): dictionary used to create model or path to json file
        '''
        if isinstance(model_config, str):
            model_config = json.load(open(model_config, 'r'))

        enigne_factory = EngineFactory(model_config)
        engine = enigne_factory.get_instance("crowd_counter")

        return engine

    def map(self, data):
        assert self.engine is not None, "Predictor has not been created yet"
        frame = data['frame_data']
        bboxes, heatmap = self.engine.process(frame) 
        data['frame_bboxes'] = bboxes
        data['frame_heatmap'] = generate_output_with_specific_colormap(heatmap)

        return data
