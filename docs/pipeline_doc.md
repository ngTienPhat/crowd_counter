## Implemented Pipeline steps:
1. Capture Video: pipeline step used to capture each frame of the giveninput video to process, implemented in [capture_video.py](base/capture_video.py)
2. Inference Video: pipeline step used to create an engine and inference on the given frame passed from previous step (capture), implemented in [inference_video.py](base/inference_video.py)
3. Annotate Video: to visualize the inferenced results on the passing frame, implemented in [annotate_video.py](base/annotate_video.py)
4. Write Video: to render the annotated frame, implemented in [write_video.py](base/write_video.py)

## Updates
- Inference video, 1 frame/it, demo with copy video pipeline (12/08/2020)

## Run
- 2 main instances: `VideoProcess` and `ImageProcess`:

Create instance:
```
video_process = VideoProcess (
    engine_config_path = data_info['engine_config_dir']
)
```

Run instance given video input/save path:
```
video_process.inference(
    video_path = input_video_path,
    save_path = save_video_path
)
```

For `ImageProcess`, please pass arguments as list of input/output image dir:

```
image_process.inference(
    list_img_paths = list_input_imgs, 
    list_save_paths = list_save_imgs
)
```


- please use [test_process.py](crowd_counter/pipelines/test_pipeline/test_process.py) as an example.


**Data passes through pipeline format**
```
{   
    ## added by CaptureImage or CaptureVideo:
    "frame_data": np.array --> image/frame array data,

    ## added by Predictor:
    "frame_bboxes": list of boxes
    "frame_heatmap": heat map for current frame_data
}
```
