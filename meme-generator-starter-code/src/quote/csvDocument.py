"""CSV extension."""
from .IngestorInterface import IngestorInterface
import pandas as pd
from typing import List
from .QuoteModel import QuoteModel


class csvDocument(IngestorInterface):
    """csvDocument class."""

    extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method with csv file."""
        if not cls.can_ingest(path):
            raise Exception('The format is unsupported.')

        try:
            ls_csv = []
            df = pd.read_csv(path)
            for i in range(len(df)):
                quote = df.loc[i]['body']
                author = df.loc[i]['author']
                ls_csv.append(QuoteModel(quote, author))
            return ls_csv
        except Exception as e:
            print(f'Error: {e}')
            return []
