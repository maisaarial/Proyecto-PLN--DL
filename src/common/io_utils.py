from __future__ import annotations
from pathlib import Path
import json
import pandas as pd

def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def save_json(data, path: str | Path) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def save_csv(df: pd.DataFrame, path: str | Path) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    df.to_csv(path, index=False, encoding="utf-8")

def load_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)
