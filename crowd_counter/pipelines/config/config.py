from yacs.config import CfgNode as CN 

C = CN() 
C.MODEL=CN()
C.DATASET=CN()

C.WORKING_DIR = "/Users/tienphat/Documents/HCMUS/Software_Design/Final_Project/crowd_counter"
C.VISUALIZE_TYPE = "Heatmap" # or "Points"



## MODEL SETUP
C.MODEL.DETECTOR_TYPE = "human_detector"
C.MODEL.PACKAGE = "yolo"
C.MODEL.MODULE = "YoloModel"
C.MODEL.TYPE = "crowd_counter"



## DATASET INFO
C.DATASET.TRAIN = ""
C.DATASET.TEST = ""
C.DATASET.DATA_PATH=""
C.DATASET.TEST_VIDEO = "data/input/video1.mp4"
C.DATASET.SAVE_PATH = "data/output/video1.mp4"
