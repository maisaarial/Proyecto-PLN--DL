from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import json
import requests


DEFAULT_CAMERAS_JSON_URL = (
    "https://opendata.euskadi.eus/contenidos/ds_localizaciones/"
    "camaras_trafico/opendata/camaras-trafico.json"
)

@dataclass
class CameraRecord:
    camera_id: str
    name: str | None = None
    road: str | None = None
    direction: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    image_url: str | None = None
    raw: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EuskadiCamerasClient:
    def __init__(self, json_url: str = DEFAULT_CAMERAS_JSON_URL, timeout: int = 30):
        self.json_url = json_url
        self.timeout = timeout

    def fetch_raw(self) -> Any:
        response = requests.get(self.json_url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def save_raw(self, output_path: str | Path) -> Path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        data = self.fetch_raw()
        output_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        return output_path

    def parse_cameras(self, data: Any) -> list[CameraRecord]:
        items = data if isinstance(data, list) else data.get("camaras", data.get("items", []))
        cameras: list[CameraRecord] = []

        for item in items:
            if not isinstance(item, dict):
                continue

            camera_id = self._pick(item, ["id", "cameraId", "idCamera", "codigo", "code"])
            name = self._pick(item, ["name", "nombre", "descripcion", "description"])
            road = self._pick(item, ["road", "carretera", "via"])
            direction = self._pick(item, ["direction", "sentido", "direccion"])
            latitude = self._pick(item, ["latitude", "latitud", "lat"])
            longitude = self._pick(item, ["longitude", "longitud", "lon", "lng"])
            image_url = self._pick(item, ["imageUrl", "url", "imagen", "snapshot", "photo", "img"])

            cameras.append(
                CameraRecord(
                    camera_id=str(camera_id) if camera_id is not None else "",
                    name=name,
                    road=road,
                    direction=direction,
                    latitude=self._to_float(latitude),
                    longitude=self._to_float(longitude),
                    image_url=image_url,
                    raw=item,
                )
            )

        return cameras

    def fetch_cameras(self) -> list[CameraRecord]:
        raw = self.fetch_raw()
        return self.parse_cameras(raw)

    @staticmethod
    def _pick(item: dict[str, Any], keys: list[str]) -> Any:
        for key in keys:
            if key in item and item[key] not in (None, ""):
                return item[key]
        return None

    @staticmethod
    def _to_float(value: Any) -> float | None:
        if value in (None, ""):
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None