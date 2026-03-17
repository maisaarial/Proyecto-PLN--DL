from __future__ import annotations
import requests
from bs4 import BeautifulSoup
from typing import List
from src.common.schemas import TrafficRecord
from src.data_sources.base import BaseSource

class BilbaoAvisosSource(BaseSource):
    source_name = "bilbao_avisos"
    url = "https://www.bilbao.eus/cs/Satellite?cid=3000075232&language=es&pageid=3000075232&pagename=Bilbaonet%2FPage%2FBIO_ListadoAvisos"

    def fetch(self) -> List[TrafficRecord]:
        r = requests.get(self.url, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        records: List[TrafficRecord] = []
        dates = [x.get_text(" ", strip=True) for x in soup.select("li")]
        titles = [x.get_text(" ", strip=True) for x in soup.select("h4")]
        snippets = [x.get_text(" ", strip=True) for x in soup.select("h4 + p")]

        for i, title in enumerate(titles):
            text = snippets[i] if i < len(snippets) else ""
            published = None
            records.append(
                TrafficRecord(
                    source=self.source_name,
                    title=title,
                    text=text,
                    published_at=published,
                    url=self.url,
                )
            )
        return records
