from __future__ import annotations
import requests
from bs4 import BeautifulSoup
from typing import List
from src.common.schemas import TrafficRecord
from src.data_sources.base import BaseSource

class DeiaTraficoSource(BaseSource):
    source_name = "deia_trafico"
    url = "https://www.deia.eus/servicios/trafico/"

    def fetch(self) -> List[TrafficRecord]:
        r = requests.get(self.url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        records: List[TrafficRecord] = []
        for tag in soup.select("h1, h2, h3, article"):
            title = tag.get_text(" ", strip=True)
            if title and len(title) > 12:
                records.append(
                    TrafficRecord(
                        source=self.source_name,
                        title=title[:180],
                        text=title,
                        url=self.url,
                    )
                )
        return records[:20]
