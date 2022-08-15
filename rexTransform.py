import torch
from torch import functional as F
from torch import Tensor
class Normalize(torch.nn.Module):
    def __init__(self, by= None):
        super().__init__()
        self.by= by

    def forward(self, tensor: Tensor) -> Tensor:
        """
        Args:
            tensor (Tensor): Tensor image to be normalized.

        Returns:
            Tensor: Normalized Tensor image.
        """
        return tensor / self.by

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(mean={self.mean}, std={self.std})"