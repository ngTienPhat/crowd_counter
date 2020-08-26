from crowd_counter.engines import BaseEngine
from .model import CANNet

import torch

class CannEngine(BaseEngine):
    def __init__(self, weight_path, device=None):
        super(CannEngine, self).__init__()
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self._device = torch.device(device)

        self.construct_model()
        self.load_weight(weight_path)

    def construct_model(self):
        self.model = CANNet(True)

    def load_weight(self, weight_path, key="state_dict"):
        checkpoint = torch.load(weight_path, map_location="cpu")
        self.model.load_state_dict(checkpoint[key])

        self.model.to(self._device)

