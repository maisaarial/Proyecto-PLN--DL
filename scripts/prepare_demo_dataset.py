from pathlib import Path

def main():
    base = Path("data/processed/cameras")
    for split in ["train", "val"]:
        for cls in ["baja", "media", "alta"]:
            (base / split / cls).mkdir(parents=True, exist_ok=True)
    print("Estructura creada en data/processed/cameras")

if __name__ == "__main__":
    main()
