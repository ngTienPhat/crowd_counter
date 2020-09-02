import os.path as osp

from crowd_counter.pipelines.model import (
    ImageProcess,
    VideoProcess
)

data_info = {
    'image_dir': 'data/images',
    'video_dir': 'data/videos',
    'test_img': ['IMG_1.jpg', 'IMG_2.jpg', 'IMG_3.jpg', 'IMG_4.jpg'],
    'test_vid': ['test1.mp4', 'test3.mp4', 'test4.mp4', 'test5.mp4'],
    
    'save_dir': 'output',
    'image_save_dir': 'output/images',
    'video_save_dir': 'output/videos',

    'engine_config_dir': 'crowd_counter/configs/engine_configs/sa_net.json'
}


def test_image_process():
    test_image1 = data_info['test_img'][0]
    test_image2 = data_info['test_img'][2]
    image_process = ImageProcess(
        img_path = osp.join(data_info['image_dir'], test_image2),
        save_path = osp.join(data_info['image_save_dir'], test_image2),
        engine_config_path = data_info['engine_config_dir']
    )

    # image_process.inference()

    list_input_imgs = [osp.join(data_info['image_dir'], inp) for inp in data_info['test_img']]
    list_save_imgs = [osp.join(data_info['image_save_dir'], inp) for inp in data_info['test_img']]
    image_process.inference(
        list_img_paths = list_input_imgs, 
        list_save_paths = list_save_imgs
    )

def test_video_process():
    # test_video1 =  data_info['test_vid'][0]
    # test_video2 =  data_info['test_vid'][1]
    video_process = VideoProcess (
        vid_path = None, #osp.join(data_info['video_dir'], test_video1),
        save_path = None, #osp.join(data_info['video_save_dir'], test_video1),
        engine_config_path = data_info['engine_config_dir']
    )

    for vid in data_info['test_vid']:
        print(vid)
        video_process.inference(
            video_path = osp.join(data_info['video_dir'], vid),
            save_path = osp.join(data_info['video_save_dir'], vid),
        )


if __name__ == "__main__":
    test_video_process()