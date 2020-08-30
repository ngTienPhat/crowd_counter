import sys
import json

from .pipeline import Pipeline 
from crowd_counter.engines import EngineFactory
from crowd_counter.engines.sanet import SA_Engine


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

        # engine = SA_Engine(weight_path = model_config['crowd_counter']['kwargs']['weight_path'])
        return engine

    def map(self, data):
        assert self.engine is not None, "Predictor has not been created yet"

        frame = data['frame_data']
        bboxes, heatmap = self.engine.process(frame) 
        data['frame_bboxes'] = bboxes
        data['frame_heatmap'] = heatmap

        return data