from crowd_counter.pipelines.base import (
    Predictor,
    CaptureVideo,
    CaptureImage,
    ImageWriter,
    Predictor,
    CaptureVideo,
    VideoWriter,
)

def create_image_pipeline(image_path=None, save_path=None, predictor_config_path=None):
    capture = CaptureImage(image_path)
    writer = ImageWriter(save_path)
    predictor = Predictor(predictor_config_path)
    list_steps = [capture, predictor, writer]
    return list_steps

def create_video_pipeline(video_path=None, save_path=None, predictor_config_path=None):
    capture = CaptureVideo(video_path)
    writer = VideoWriter(save_path)
    predictor = Predictor(predictor_config_path)
    list_steps = [capture, predictor, writer]
    return list_steps
