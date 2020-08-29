import cv2
from PIL import Image 

def draw_boxes_on_image(image_data, boxes: list, labels: str = None, color=(0, 255, 0)):
    '''
    Args:
        image_dir (numpy array): path to image 
        boxes (list): list of bboxes to draw on images
        labels (list): list of labels for each bboxes

    Return:
        drawn image
    ''' 
    if labels is not None:
        assert len(boxes) == len(labels), "number of predicted boxes must be equal to labels"

    for i, box in enumerate(boxes):
        cv2.rectangle(image_data, (box[0], box[1]), (box[2], box[3]), color=color, thickness=1)
        if labels:
            cv2.putText(image_data, labels[i], ((box[0]+box[2])//2, (box[1]+box[3])//2))

    return image_data

def blend_heatmap(image_data, heatmap, alpha=0.5):
    return Image.blend(Image.fromarray(image_data), heatmap, alpha).numpy()


def draw_heatmap_on_image(image, heatmap, alpha = 0.5):
    return image + alpha*heatmap
