"""Txt extension."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class txtDocument(IngestorInterface):
    """TxtDocument class."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method with txt file."""
        if not cls.can_ingest(path):
            raise Exception('The format is unsupported.')

        try:
            ls_txt = []
            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    p = line.split(sep=' - ')
                    p = [s.strip() for s in p]
                    if p[0] != "":
                        ls_txt.append(QuoteModel(p[0], p[1]))
            return ls_txt
        except Exception as e:
            print(f'Error: {e}')
            return []
