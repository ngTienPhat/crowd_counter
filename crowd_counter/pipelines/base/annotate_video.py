from .pipeline import Pipeline 

class Annotator(Pipeline):
    '''
    Use this pipeline step to visualize prediction on the current image: show heatmap or head-point

    Args:

    
    '''
    def __init__(self, cfg):
        
        super().__init__()

    def map(self, data):
        print(f"annotate data")
        return data
        