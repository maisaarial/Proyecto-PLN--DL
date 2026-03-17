from __future__ import annotations
import torch.nn as nn
from torchvision import models

def build_congestion_classifier(num_classes: int = 3):
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)
    return model
