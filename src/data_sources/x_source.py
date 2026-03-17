from __future__ import annotations
from typing import List
from src.common.schemas import TrafficRecord
from src.data_sources.base import BaseSource

class XOfficialSource(BaseSource):
    source_name = "x_trafikoa"

    def fetch(self) -> List[TrafficRecord]:
        # X suele requerir credenciales o una vía oficial de acceso.
        # Este adaptador está preparado para ser sustituido por:
        # 1) API oficial,
        # 2) dataset exportado manualmente,
        # 3) RSS/servicio intermedio, si lo definís.
        return []
