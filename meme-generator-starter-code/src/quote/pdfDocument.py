"""Pdf extension."""
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import subprocess


class pdfDocument(IngestorInterface):
    """pdfDocument class."""

    extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method with pdf file."""
        if not cls.can_ingest(path):
            raise Exception('The format is unsupported.')

        try:
            ls_pdf = []
            tmp_txt = './tmp.txt'
            subprocess.call(['pdftotext', path, tmp_txt])
            with open(tmp_txt, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    p = line.split(sep=' - ')
                    p = [s.strip() for s in p]
                    if p[0] != "":
                        ls_pdf.append(QuoteModel(p[0], p[1]))
            subprocess.call(['rm', tmp_txt])
            return ls_pdf
        except Exception as e:
            print(f'Error: {e}')
            return []
