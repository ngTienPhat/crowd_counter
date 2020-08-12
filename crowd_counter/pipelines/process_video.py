from crowd_counter.pipelines.base import (
    Capture, Annotator, Predictor, Writer, VideoPipeline
)
from config.config import C as cfg
import os 

os.chdir(cfg.WORKING_DIR)


def create_copy_video_pipeline():
    capture = Capture(src = cfg.DATASET.TEST_VIDEO, skip_frame=1)
    writer = Writer(save_path = cfg.DATASET.SAVE_PATH, fourcc='MP4V')

    pipeline = VideoPipeline([capture, writer], name = "CopyPipeline")
    return pipeline


def main():
    copy_pipeline = create_copy_video_pipeline()
    copy_pipeline.run()

if __name__ == "__main__":
    main()
