import cv2

def draw_boxes_on_image(image_dir: str, boxes: list, labels: str = None):
    '''

    Args:
        image_dir (numpy array): path to image 
        boxes (list): list of bboxes to draw on images
        labels (list): list of labels for each bboxes

    Return:
        image after being drawn
    ''' 
    if labels is not None:
        assert len(boxes) == len(labels), "number of predicted boxes must be equal to labels"

    
    