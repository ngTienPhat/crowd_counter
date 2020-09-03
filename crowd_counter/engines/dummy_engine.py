""" Dummy engine for test purpose """

from .base_engine import BaseEngine

import numpy as np

class DummyEngine(BaseEngine):
    def _process(self, image):
        img_np = np.array(image)
        img_size = img_np.shape[:2]

        heatmap = np.random.randint(low=0, high=255, size=img_size, dtype=np.uint8)
        return [], heatmap

