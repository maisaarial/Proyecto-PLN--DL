from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from src.common.schemas import TrafficRecord

class BaseSource(ABC):
    source_name: str = "base"

    @abstractmethod
    def fetch(self) -> List[TrafficRecord]:
        raise NotImplementedError
