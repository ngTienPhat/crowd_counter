from .annotate_video import Annotator
from .capture_video import Capture 
from .inference_video import Predictor 
from .save_video import Writer 
from tqdm import tqdm

class VideoPipeline(object):
    def __init__(self, list_step, name="default video pipeline"):
        '''
        Args:
            list_step: list of Pipeline object to create a video pipeline, ex: [Capture, Writer]
        '''
        self.list_step = list_step
        self.pipeline = list_step[0]
        for step in list_step[1:]:
            self.pipeline |= step

        self.name = name
    
    def run(self):
        try:
            for _ in tqdm(self.pipeline):
                pass
        except StopIteration:
            return
        except KeyboardInterrupt:
            return
        finally:
            for step in self.list_step:
                if isinstance(step, Capture) or isinstance(step, Writer):
                    step.cleanup()

            print(f"[{self.name}]: finish")
