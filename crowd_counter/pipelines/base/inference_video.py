import sys

from .pipeline import Pipeline 
# from crowd_counter.engines import EngineFactory 

#TODO: wait for engine

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
        pass
    
    def map(self, data):
        frame = data['frame_data']
        output = self.engine.process(frame) 
        data['output'] = output

        return data