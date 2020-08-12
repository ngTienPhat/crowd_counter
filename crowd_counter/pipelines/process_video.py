import sys

from base import (
    Capture, Annotator, Predictor, Writer, VideoPipeline
)
from config import C as cfg
import os 

os.chdir(cfg.WORKING_DIR)

def create_copy_video_pipeline():
    # 1. Create each pipeline step as an independent object
    capture = Capture(src = cfg.DATASET.TEST_VIDEO, skip_frame=1)
    writer = Writer(save_path = cfg.DATASET.SAVE_PATH, fourcc='MP4V')

    # 2. Combine the above pipeline objects to create a pipeline
    pipeline = VideoPipeline([capture, writer], name = "CopyPipeline")
    return pipeline


def main():
    copy_pipeline = create_copy_video_pipeline()
    copy_pipeline.run()

if __name__ == "__main__":
    main()
