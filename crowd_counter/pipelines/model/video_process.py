from crowd_counter.pipelines.base import BaseProcess
from crowd_counter.pipelines.base import CaptureVideo


from .utils import (
    create_image_pipeline,
    create_video_pipeline,
)


class VideoProcess(BaseProcess):
    def __init__(
        self,
        list_step=None,
        vid_path=None,
        save_path=None,
        engine_config_path=None,
        name="default video pipeline",
        fourcc="MP4V",
    ):

        self.vid_path = vid_path
        self.save_path = save_path

        if list_step is None:
            list_step = create_video_pipeline(
                vid_path, save_path, engine_config_path, fourcc
            )

        super().__init__(list_step, name=name)

    def __update_pipeline(self):
        self.setup_pipeline(self.list_step)

    def set_predictor(self, predictor_config_path: str):
        for i in range(len(self.list_step)):
            if isinstance(self.list_step[i], predictor_config_path):
                self.list_step[i].create_engine(predictor_config_path)
                break

    def load_video(self, video_path):
        """
        Load new video to run       
        Args:
            video_path: path to new video to process 
        """
        self.list_step[0].setup(video_path)

    def setup_in_out(self, video_path, output_path):
        self.load_video(video_path)
        self.set_save_path(output_path)
        self.__update_pipeline()

    def set_save_path(self, save_path: str):
        self.list_step[-1].set_save_path(save_path)

    def default_inference(self):
        self.__update_pipeline()
        assert (
            self.pipeline is not None
        ), "Pipeline has not been implemented yet"

        if self.vid_path is not None and self.save_path is not None:
            self.run()

    def inference(self, video_path=None, save_path=None):
        """
        Inference on a single camera
        Args:
            video_path (str): video path
            save_path (str): save path
        """

        self.__update_pipeline()
        assert (
            self.pipeline is not None
        ), "Pipeline has not been implemented yet"

        if video_path is not None and save_path is not None:
            self.load_video(video_path)
            self.set_save_path(save_path)

            self.__update_pipeline()
            # print(self.list_step[-1].save_path)
            self.run()

    def get_num_frame(self):
        return self.list_step[0].get_num_frame()
