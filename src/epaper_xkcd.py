import epaper
def display_last_xkcd():
    """display on epaper the last xkcd and go back to sleep

    """
    epd = epaper.epaper('epd2in13_V4').EPD()

    epd.init()
    epd.clear()

    epd.sleep()

if __name__ == '__main__':
    display_last_xkcd()
