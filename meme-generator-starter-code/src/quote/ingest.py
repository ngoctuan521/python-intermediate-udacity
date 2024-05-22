"""Ingest all extensions."""
from .csvDocument import csvDocument
from .docxDocument import docxDocument
from .pdfDocument import pdfDocument
from .txtDocument import txtDocument
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class Ingest(IngestorInterface):
    """Ingest class."""

    ls_reader = [csvDocument, docxDocument, pdfDocument, txtDocument]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method with all extensions."""
        for reader in cls.ls_reader:
            if reader.can_ingest(path):
                return reader.parse(path)
