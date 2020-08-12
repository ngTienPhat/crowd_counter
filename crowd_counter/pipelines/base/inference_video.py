import sys

from .pipeline import Pipeline 
# from crowd_counter.engines import EngineFactory 


class Predictor(Pipeline):
    def __init__(self, model_config):
        self.engine = self._create_engine(model_config)
        
        super().__init__()

    def _create_engine(self, model_config):
        pass
    
    def map(self, data):
        frame = data['frame_data']
        output = self.engine.process(frame)
        data['output'] = output

        return data