from __future__ import annotations
from PIL import Image
import torch
from torchvision import transforms
from src.dl.model import build_congestion_classifier

IDX_TO_LABEL = {0: "baja", 1: "media", 2: "alta"}

class CameraCongestionPredictor:
    def __init__(self, weights_path: str | None = None, device: str = "cpu"):
        self.device = device
        self.model = build_congestion_classifier(num_classes=3).to(device)
        if weights_path:
            self.model.load_state_dict(torch.load(weights_path, map_location=device))
        self.model.eval()
        self.tfm = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    @torch.no_grad()
    def predict(self, image_path: str):
        image = Image.open(image_path).convert("RGB")
        x = self.tfm(image).unsqueeze(0).to(self.device)
        logits = self.model(x)
        probs = torch.softmax(logits, dim=1)[0]
        idx = int(torch.argmax(probs).item())
        return {"label": IDX_TO_LABEL[idx], "score": float(probs[idx].item())}
