from __future__ import annotations
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from sklearn.metrics import accuracy_score, f1_score
from src.dl.dataset import TrafficImageFolderDataset
from src.dl.model import build_congestion_classifier

def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()
    total_loss = 0.0
    y_true, y_pred = [], []
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        preds = logits.argmax(dim=1)
        y_true.extend(y.cpu().tolist())
        y_pred.extend(preds.cpu().tolist())
    return total_loss / max(len(loader), 1), accuracy_score(y_true, y_pred), f1_score(y_true, y_pred, average="weighted")

def run_training(data_root="data/processed/cameras", epochs=3, batch_size=8, lr=1e-4, device="cpu"):
    tfm = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    train_ds = TrafficImageFolderDataset.from_folder(data_root, split="train", transform=tfm)
    val_ds = TrafficImageFolderDataset.from_folder(data_root, split="val", transform=tfm)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False)

    model = build_congestion_classifier(num_classes=3).to(device)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    history = []
    for epoch in range(epochs):
        loss, acc, f1 = train_one_epoch(model, train_loader, optimizer, criterion, device)
        history.append({"epoch": epoch + 1, "train_loss": loss, "train_acc": acc, "train_f1": f1})
        print(history[-1])
    return model, history
