from crowd_counter.pipelines.base import BaseProcess 
from crowd_counter.pipelines.base import (
    CaptureImage,
    ImageWriter,
    Predictor,    
)


from .utils import (
    create_image_pipeline,
    create_video_pipeline,
)

class ImageProcess(BaseProcess):
    def __init__(self, 
        list_step=None, 
        img_path=None, 
        save_path=None, 
        engine_config_path = None,
        name='default image pipeline'):
        
        self.img_path = img_path
        self.save_path = save_path

        if list_step is None:
            list_step = create_image_pipeline(img_path, save_path, engine_config_path)
        
        super().__init__(list_step, name=name)
    

    def set_predictor(self, predictor_config_path: str):
        for i in range(len(self.list_step)):
            if isinstance(self.list_step[i], Predictor):
                self.list_step[i].create_engine(predictor_config_path)
                break

    def load_image(self, img_info):
        '''
        Load image to capture step of this pipeline
        Args:
            img_info: image path or PIL, np.array image
        '''
        self.list_step[0].load_image(img_info)

    def set_save_path(self, save_path: str):
        self.list_step[-1].set_save_path(save_path)

    def __update_pipeline(self):
        self.setup_pipeline(self.list_step)

    def default_inference(self):
        self.__update_pipeline()
        assert self.pipeline is not None, "Pipeline has not been implemented yet"

        if self.img_path is not None and self.save_path is not None:
            self.run()

    def inference(self, list_img_paths=None, list_save_paths=None):
        '''
        Inference on a single or multiple images
        Args:
            list_img_paths (list): list of images to inference, 
                        element type can be image path or PIL.Image, np.array 
            list_save_paths (list): list to save inference result
        '''
        self.__update_pipeline()
        assert self.pipeline is not None, "Pipeline has not been implemented yet"

        if list_img_paths is not None:
            assert list_save_paths is not None, "You have to pass save path"
            assert len(list_save_paths) == len(list_img_paths), "Each input image should have it own save path"
            for i, img in enumerate(list_img_paths):
                # Setup new info
                self.load_image(img)
                self.set_save_path(list_save_paths[i])
                self.__update_pipeline()

                self.run()

        



