"""Declare Quote modules."""
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .csvDocument import csvDocument
from .docxDocument import docxDocument
from .pdfDocument import pdfDocument
from .txtDocument import txtDocument
from .ingest import Ingest

__all__ = (
    "QuoteModel",
    "IngestorInterface",
    "csvDocument",
    "docxDocument",
    "pdfDocument",
    "txtDocument",
    "Ingest",
)
