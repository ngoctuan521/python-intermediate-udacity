"""Declare ABC class."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """IngestorInterface class."""

    extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Classmethod."""
        ext = path.split(sep='.')[-1]
        return ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method."""
        raise Exception('Please implement parse method.')
