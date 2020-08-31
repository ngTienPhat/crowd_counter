from .annotate_video import Annotator
from .capture_video import CaptureVideo  
from .inference_video import Predictor 
from .write_video import VideoWriter 
from tqdm import tqdm

class BaseProcess(object):
    def __init__(self, list_step=None, name="default video pipeline"):
        '''
        Args:
            list_step: list of Pipeline object to create a video pipeline.
            
        Example: 
            [Capture, Writer]
        '''
        self.list_step, self.pipeline = None, None
        if list_step is not None:
            self.setup_pipeline(list_step)

        self.name = name
    
    def setup_pipeline(self, list_step):
        self.list_step = list_step
        self.pipeline = list_step[0]
        for step in list_step[1:]:
            self.pipeline |= step

    def run(self):
        assert self.pipeline is not None, "pipeline has been not implemented yet"
        try:
            for _ in tqdm(self.pipeline):
                pass
        except StopIteration:
            return
        except KeyboardInterrupt:
            return
        finally:
            for step in self.list_step:
                if isinstance(step, CaptureVideo) or isinstance(step, VideoWriter):
                    step.cleanup()

            print(f"[{self.name}]: finish")
