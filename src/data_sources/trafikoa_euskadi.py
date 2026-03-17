from __future__ import annotations
import requests
from bs4 import BeautifulSoup
from typing import List
from src.common.schemas import TrafficRecord
from src.data_sources.base import BaseSource

class TrafikoaEuskadiSource(BaseSource):
    source_name = "trafikoa_euskadi"
    url = "https://www.trafikoa.euskadi.eus/inicio/"

    def fetch(self) -> List[TrafficRecord]:
        # Este scraper es un adaptador base.
        # Si la página usa endpoints internos o JS dinámico, sustituid este método
        # por consumo de API / endpoint real / feed exportado.
        r = requests.get(self.url, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        records: List[TrafficRecord] = []
        for item in soup.select("article, .incidencia, .news-item"):
            title = item.get_text(" ", strip=True)[:140]
            records.append(
                TrafficRecord(
                    source=self.source_name,
                    title=title,
                    text=title,
                    url=self.url,
                )
            )
        return records
