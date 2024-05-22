"""Test meme function."""
import os
import random
from quote import QuoteModel
from quote import IngestorInterface
from quote import Ingest
from meme import MemeEngine
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingest.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=None, help='path to an image file',
                        required=False)
    parser.add_argument('--body', default=None, type=str,
                        help='quote body to add to the image', required=False)
    parser.add_argument('--author', default=None, type=str, help='quote \
                        author to add to the image', required=False)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
