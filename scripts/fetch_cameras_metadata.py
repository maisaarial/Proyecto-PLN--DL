from pathlib import Path
from src.data_sources.camaras_euskadi import EuskadiCamerasClient


def main() -> None:
    client = EuskadiCamerasClient()

    output_path = Path("data/raw/cameras/metadata/cameras_raw.json")
    client.save_raw(output_path)

    cameras = client.fetch_cameras()

    print(f"Total cámaras parseadas: {len(cameras)}")
    print("\nPrimeras 3 cámaras:")
    for camera in cameras[:3]:
        print(camera.to_dict())

    with_image = [c for c in cameras if c.image_url]
    print(f"\nCámaras con image_url detectada: {len(with_image)}")
    for camera in with_image[:5]:
        print(camera.camera_id, camera.name, camera.image_url)


if __name__ == "__main__":
    main()
    