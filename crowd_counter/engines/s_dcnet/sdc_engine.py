from crowd_counter.engines.s_dcnet.network import SDCNet_VGG16_classify
from crowd_counter.engines import BaseEngine

import torch
import numpy as np
import cv2
from torchvision import transforms

MODEL_CONFIG_DICTIONARY = {
    0: {
        "name": "model/SHA",
        "step": 0.5,
        "max_num": 22,
        "partition": "two_linear",
    },
    1: {
        "name": "model/SHB",
        "step": 0.5,
        "max_num": 7,
        "partition": "two_linear",
    },
}


class SDC_Engine(BaseEngine):
    def __init__(
        self, weight_paths, architech_idx=0, state_dict_key="net_state_dict"
    ):
        super(SDC_Engine, self).__init__()
        self.architech_idx = architech_idx

        self.construct_model()
        self.load_weight(weight_paths, state_dict_key)

    def construct_model(self):
        label_indice = self.get_label_indices()
        self.model = SDCNet_VGG16_classify(label_indice)

    def load_weight(self, weight_paths, state_dict_key="net_state_dict"):
        """ Load model weight from weight_paths """
        checkpoint = torch.load(weight_paths, map_location="cpu")
        self.model.load_state_dict(checkpoint[state_dict_key])

    def get_label_indices(self):
        """ Load hyper parameter to construct model architecture """
        return self.__get_label_indices(
            **MODEL_CONFIG_DICTIONARY[self.architech_idx]
        )

    def __get_label_indices(self, partition, step, max_num, **kwargs):
        """ Private helper function to get label indices
        Copied from original repo
        """
        if partition == "one_linear":
            label_indice = np.arange(step, max_num + step / 2, step)
            add = np.array([1e-6])
            label_indice = np.concatenate((add, label_indice))
        elif partition == "two_linear":
            label_indice = np.arange(step, max_num + step / 2, step)
            add = np.array(
                [1e-6, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45]
            )
            label_indice = np.concatenate((add, label_indice))
        return label_indice

    def _process(self, frame, image_size=None):
        """
        Args:
            frame (PIL Image)
            image_size (tuple)
        """
        original_size = frame.size
        if image_size is not None:
            frame = frame.resize(image_size)
        frame = frame.convert("RGB")
        x = transforms.ToTensor()(frame)
        x = x.unsqueeze(x)

        with torch.no_grad():
            feature_maps = self.model(x)
            output = self.model.resample(feature_maps)

            masks = output["cls2"][0]
            logit = torch.softmax(masks, dim=0)
            heatmap = masks[0]

        # Convert back to cpu
        heatmap = heatmap.cpu().numpy()

        # Resize heatmap to original size
        heatmap = transforms.ToPILImage()(heatmap)
        heatmap = heatmap.resize(original_size)
        heatmap = np.array(heatmap)

        bboxes = self._get_bboxes(heatmap)

        return bboxes, heatmap


    def _get_bboxes(self, heatmap):
        # Magic go here
        contours = cv2.findContours(heatmap, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]

        bboxes = []
        for i, c in enumerate(contours):
            contour_poly = cv2.approxPolyDP(c, 3, True)
            bbox = cv2.boundingRect(contour_poly)
            bboxes.append(bbox)

        return bboxes

        
