# Engine Document

## Engine Factory
Example usecase:
``` python
config = {
    "human_detector": {
        "package": "yolo",
        "module": "YoloModel",
        "args": ["/path/to/weight.pth"],
        "kwargs": {},
    },
}

# Above config means:
# from yolo import YoloModel
# model = YoloModel(*args, **kwargs)

from crow_counter.engines import EngineFactory
factory = EngineFactory(config)

model = factory.get_instance("human_detector")
```

## Engine Interface
Since we currently have only one engine type (Human Detector), here we will assume that
the engine below is HumanDetector Engine

Method:
`process(inputs, n_frame_skip=5)`:
    - `inputs`: Can be path to image, image numpy, image pillow or list of them.
    - `n_frame_skip`: Only affect when you input list of images.

    - Return: `bboxes`, `heatmaps`.
        - `bboxes`: List of bboxes (Or list of list of bboxes), which information is stored by dictionary.
```
bboxes = [
    {"location": [[0, 2], [0, 4], [2, 4], [2, 2]], "type": "head", "confidence": 0.8, },
    ...
]
```
        - `heatmaps`: Numpy array or list of numpy array


# Extend

To extend model, you need to override the `_process` function.

Docstring of `_process` function:
```
Process for single image file 
Args:
    frame (pillow image)

Return: bboxes, heatmap
    - bboxes (list)
    - heatmap (None or np.ndarray uint8)
```

Example for dummy engine that just generate random heatmap and empty boxes:
``` python
from crowd_counter.engines.base_engine import BaseEngine
import numpy as np

class DummyEngine(BaseEngine):
    def _process(self, image):
        img_np = np.array(image)
        img_size = img_np.shape[:2]

        heatmap = np.random.randint(low=0, high=255, size=img_size, dtype=np.uint8)
        return [], heatmap
```

