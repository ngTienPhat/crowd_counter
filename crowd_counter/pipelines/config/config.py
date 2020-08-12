from yacs.config import CfgNode as CN 


C = CN() 

C.WORKING_DIR = 'Documents/HCMUS/Software_Design/Final_Project/crowd_counter'

C.MODEL=CN()
C.SOLVER=CN()
C.DATASET=CN()

C.MODEL.TYPE=""
C.MODEL.PACKAGE=""
C.MODEL.MODULE=""

C.SOLVER.BATCH_SIZE = 10
C.SOLVER.MAX_ITER=200

C.DATASET.TRAIN = "tien"
C.DATASET.TEST = "phat"
C.DATASET.TEST_VIDEO = "data/input/video1.mp4"
C.DATASET.SAVE_PATH = "data/output/video1.mp4"