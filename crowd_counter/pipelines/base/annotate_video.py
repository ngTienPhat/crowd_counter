from .pipeline import Pipeline 
from .utils import draw_boxes_on_image, blend_heatmap

class Annotator(Pipeline):
    '''
    Pipeline step to visualize prediction on the current image: heatmaps or bboxes

    Args:
        
    '''
    def __init__(self, cfg):
        super().__init__()

    def map(self, data):
        data['output_heatmap'] = blend_heatmap(data['frame_data'], data['frame_heatmap'])
        data['output_bboxes'] = draw_boxes_on_image(data['frame_data'], data['frame_bboxes'])

        data.pop('heatmap')
        data.pop('bboxes')

        return data
        