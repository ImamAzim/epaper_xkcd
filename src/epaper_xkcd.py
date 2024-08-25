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

    epd_img = Image.new('1', (epd.width, epd.height), 255)

    with tempfile.TemporaryDirectory() as tmpdirname:
        comic = xkcd.getLatestComic()
        comic.download(tmpdirname, 'image')
        fp = os.path.join(tmpdirname, 'image')
        xkcd_img = Image.open(fp)
        img_ratio = xkcd_img.width / xkcd_img.height
        if (epd_ratio-1)*(img_ratio-1)<0:
            xkcd_img = xkcd_img.rotate(90, expand=True)
        maxsize = epd.width, epd.height
        xkcd_img.thumbnail(maxsize, resample)=Image.Resampling.LANCZOS, reducing_gap=10)
        epd_img.paste(xkcd_img)

        buffer = epd.getbuffer(epd_img)
        epd.display(buffer)




    epd.sleep()

if __name__ == '__main__':
    display_last_xkcd()
