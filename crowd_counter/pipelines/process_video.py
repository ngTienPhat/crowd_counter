import sys

from crowd_counter.pipelines.base import (
    Capture, Annotator, Predictor, Writer, VideoPipeline, CaptureImage, ImageWriter
)
from crowd_counter.pipelines.config import C as cfg
import os 

data_dir = "/home/ntphat/projects/crowd_counter/crowd_counter/data"
output_dir = data_dir.replace('data', 'output')



# os.chdir(cfg.WORKING_DIR)

def create_copy_video_pipeline():
    # 1. Create each pipeline step as an independent object
    capture = Capture(src = os.path.join(cfg.DATASET.DATA_PATH, cfg.DATASET.TEST_VIDEO), skip_frame=1)
    writer = Writer(save_path = os.path.join(cfg.DATASET.DATA_PATH, cfg.DATASET.SAVE_PATH), fourcc='MP4V')

    # 2. Combine the above pipeline objects to create a pipeline
    pipeline = VideoPipeline([capture, writer], name = "CopyPipeline")
    return pipeline


def inference_single_image_pipeline():
    # Declare variables
    
    test_image = os.path.join(data_dir, 'images/IMG_1.jpg')
    save_image = os.path.join(output_dir, 'images/IMG_1.jpg')
    sanet_config = {
        'crowd_counter': {
            'package': 'crowd_counter.engines.sanet.sa_engine',
            'module': 'SA_Engine',
            #'args': [],
            'kwargs': {
                'weight_path': 'weight/SANet_weight.hdf5',
            }
        }
    }

    capture = CaptureImage(img_data=test_image)
    predictor = Predictor(sanet_config)
    writer = ImageWriter(save_image)

    runner = VideoPipeline([capture, predictor, writer], name="single image pipeline")
    return runner

def inference_video_pipeline():
    test_video = os.path.join(data_dir, 'videos/test1.mp4')
    save_video = os.path.join(output_dir, 'videos/test1.mp4')
    sanet_config = {
        'crowd_counter': {
            'package': 'crowd_counter.engines.sanet.sa_engine',
            'module': 'SA_Engine',
            #'args': [],
            'kwargs': {
                'weight_path': 'weight/SANet_weight.hdf5',
            }
        }
    }

    capture = Capture(src=test_video)
    predictor = Predictor(sanet_config)
    writer = Writer(save_path = save_video, fourcc = 'MP4V')

    runner = VideoPipeline([capture, predictor, writer], name="count video pipeline")
    return runner

def main():
    config_file = "crowd_counter/pipelines/pipeline_configs/test_config.yaml"
    cfg.merge_from_file(config_file)

    # copy_pipeline = create_copy_video_pipeline()
    # copy_pipeline.run()

    pipeline_runner = inference_video_pipeline()
    pipeline_runner.run()

if __name__ == "__main__":
    main()
