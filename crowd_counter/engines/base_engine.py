import numpy as np
from PIL import Image

import logging


class BaseEngine(object):
    """ Base class for Engine """

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    def process(self, inputs, n_frame_skips=5, **kwargs):
        """ Main process function for Engine Class
        Args:
            
        Return:
            bboxes (list): 
            heat_maps (np.ndarray)
        """
        # Convert all supported data types to Pillow
        inputs = self.ensure_loaded(inputs)

        # Check if video -> Use video process
        is_video = self.check_is_video(inputs)
        if is_video:
            return self.process_video(inputs, n_frame_skips, **kwargs)

        # Else return single frame output
        return self._process(inputs, **kwargs)

    def check_is_video(self, inputs):
        """ Check if inputs is video or not """
        if isinstance(inputs, list):
            return True

        if isinstance(inputs, np.ndarray) and len(inputs.shape) == 4:
            return True
        return False

    def ensure_loaded(self, frames):
        """ Convert all know data types to Pillow Image """
        if isinstance(frames, list):
            return [self.ensure_np_array(frame) for frame in frames]

        elif isinstance(frames, str):
            return Image.open(frames)

        elif isinstance(frames, np.ndarray):
            return Image.fromarray(frames)
            
        return frames

    def process_video(self, inputs, n_frame=5):
        """ Process video """
        outputs = [
            self._process(frame)
            for idx, frame in enumerate(inputs)
            if idx % n_frame == 0
        ]

        bboxes = [output[0] for output in outputs]
        masks = [output[1] for masks in outputs]
        return bboxes, masks

    def _process(self, frame, **kwargs):
        """ Process for single image file 
        Args:
            frame (pillow image)

        Return: bboxes, heatmap
            - bboxes (list)
            - heatmap (None or np.ndarray uint8)
        """
        raise NotImplementedError()
