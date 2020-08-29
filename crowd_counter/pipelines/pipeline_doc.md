## Implemented Pipeline steps:
1. Capture Video: pipeline step used to capture each frame of the giveninput video to process, implemented in [capture_video.py](base/capture_video.py)
2. Inference Video: pipeline step used to create an engine and inference on the given frame passed from previous step (capture), implemented in [inference_video.py](base/inference_video.py)
3. Annotate Video: to visualize the inferenced results on the passing frame, implemented in [annotate_video.py](base/annotate_video.py)
4. Write Video: to render the annotated frame, implemented in [write_video.py](base/write_video.py)

## Updates
- Inference video, 1 frame/it, demo with copy video pipeline (12/08/2020)

## Run
- please use [process_video.py](./process_video.py) as an example.


**Data passes through pipeline format**
```

```
