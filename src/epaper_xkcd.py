import tempfile
import os


import epaper
import xkcd
from PIL import Image


def display_last_xkcd():
    """display on epaper the last xkcd and go back to sleep

    """
    epd = epaper.epaper('epd2in13_V4').EPD()
    epd.init()
    epd.Clear()
    epd_ratio = epd.width / epd.height

    with tempfile.TemporaryDirectory() as tmpdirname:
        comic = xkcd.getLatestComic()
        comic.download(tmpdirname, 'image')
        fp = os.path.join(tmpdirname, 'image')
        img = Image.open(fp)
        print(img.size)
        img_ratio = img.width / img.height
        if (epd_ratio-1)*(img_ratio-1)<0:
            img = img.rotate(90, expand=True)
        maxsize = epd.width, epd.height
        img.thumbnail(maxsize)
        print(img.size)




    epd.sleep()

if __name__ == '__main__':
    display_last_xkcd()
