import torch
import torch.nn as nn
import torch.nn.functional as F


# naming convention
class CustomLayer(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def forward(self, x):
        return nn.Identity(x)