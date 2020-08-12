from __future__ import absolute_import

from annotate_video import Annotator
from capture_video import Capture 
from inference_video import Predictor
from save_video import Writer
from video_pipeline import VideoPipeline


__video_pipeline_factory = {
    'annotator': Annotator,
    'capture': Capture,
    'predictor': Predictor,
    'writer': Writer, 
}


def create_video_pipeline_step(step_id, **kwargs):
    assert step_id not in __video_pipeline_factory.keys(), \
        f"unsupported pipeline step, valid ones are: {list(__video_pipeline_factory.keys())}"

    return __video_pipeline_factory[step_id](kwargs)
