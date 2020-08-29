import sys
from .pipeline import Pipeline 
from crowd_counter.engines import EngineFactory


class Predictor(Pipeline):
    '''
    Create a predictor for the current task. 
    Args:
        model_config: information used to create model
    '''

    def __init__(self, model_config):
        self.engine = self._create_engine(model_config)
        super().__init__()

    def _create_engine(self, model_config):
        enigne_factory = EngineFactory(model_config)
        engine = enigne_factory.get_instance("sa_net")
    
    def map(self, data):
        frame = data['frame_data']
        bboxes, heatmap = self.engine.process(frame) 
        data['frame_bboxes'] = bboxes
        data['frame_heatmap'] = heatmap

        return data