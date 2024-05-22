"""Run the application."""
import random
import glob
import requests
from flask import Flask, render_template, request
from meme import MemeEngine
from quote import Ingest
import os

app = Flask(__name__)

meme = MemeEngine('./static')
download_img = 0


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for path_file in quote_files:
        quotes.extend(Ingest.parse(path_file))

    images_path = "./_data/photos/dog/"
    imgs = []
    for path_img in glob.glob(f'{images_path}/**/*.jpg', recursive=True):
        imgs.append(path_img)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    global download_img, quotes, imgs
    path_download = "./_data/photos/download"

    if not os.path.exists(path_download):
        os.mkdir(path_download)

    img_url = request.form.get("image_url")
    try:
        r = requests.get(img_url, stream=True)
    except Exception as e:
        print("Cannot download from url.")
        return render_template('meme_error.html')

    path = None
    if r.status_code == 200:
        img = r.raw.read()
        tmp_img = './tmp_image.jpg'
        with open(tmp_img, 'wb') as f:
            f.write(img)
        body = request.form.get('body')
        author = request.form.get('author')
        path = meme.make_meme(tmp_img, body, author)
        os.remove(tmp_img)
    else:
        raise "Cannot download file"
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
