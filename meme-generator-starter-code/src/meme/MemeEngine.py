"""Meme Engine Module."""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import random
import textwrap


class MemeEngine():
    """Class MemeEngine."""

    def __init__(self, output_dir):
        """Init Instance."""
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        self.count = 1

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme function."""
        try:
            img = Image.open(img_path)
        except Exception:
            raise "Can not read image. Check image path again"
        # resize image, fix width
        w, h = img.size
        height = int((width * h) / w)
        img = img.resize((width, height))
        # add text to image
        addText = ImageDraw.Draw(img)
        font_quote = ImageFont.truetype('_data/fonts/Roboto-Bold.ttf', 22)
        font_author = ImageFont.truetype('_data/fonts/Roboto-Medium.ttf', 18)
        x = int(random.random() * 75)
        y = int(random.random() * (0.85 * height))

        wrapper = textwrap.TextWrapper(width=25)
        ls_texts = wrapper.wrap(text=text)
        if len(ls_texts) > 1:
            for txt in ls_texts:
                yy = y
                addText.text((x, yy), txt, fill=(255, 0, 0), font=font_quote)
                y += 20
        else:
            addText.text((x, y), text, fill=(255, 0, 0), font=font_quote)
        addText.text((x, y+30), author, fill=(255, 0, 0), font=font_author)

        img_rs_path = f"{self.output_dir}/{self.count}.jpg"
        img.save(img_rs_path)
        self.count += 1
        return img_rs_path
