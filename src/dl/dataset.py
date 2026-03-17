from __future__ import annotations
from pathlib import Path
from PIL import Image
from torch.utils.data import Dataset

class TrafficImageFolderDataset(Dataset):
    '''
    Estructura esperada:
    data/processed/cameras/
        train/
            baja/
            media/
            alta/
        val/
            baja/
            media/
            alta/
    '''
    def __init__(self, samples, transform=None):
        self.samples = samples
        self.transform = transform

    @classmethod
    def from_folder(cls, root: str | Path, split: str = "train", classes=("baja", "media", "alta"), transform=None):
        root = Path(root) / split
        samples = []
        class_to_idx = {c: i for i, c in enumerate(classes)}
        for class_name in classes:
            class_dir = root / class_name
            if not class_dir.exists():
                continue
            for img_path in class_dir.glob("*"):
                if img_path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                    samples.append((str(img_path), class_to_idx[class_name]))
        return cls(samples, transform=transform)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image, label
