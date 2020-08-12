from .pipeline import Pipeline 

class Annotator(Pipeline):
    def __init__(self):
        
        super().__init__()

    def map(self, data):
        print(f"annotate data")
        return data
        