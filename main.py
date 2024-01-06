import pgzrun
from pgzero.actor import Actor


def draw():
    """
    A method for drawing anything with any change (execute by pgzrun.go())
    :return:
    """
    background.draw()


def update():
    """
    A method for updating and refresh 60 times per second (execute by pgzrun.go())
    :return:
    """
    pass


WIDTH = 1280
HEIGHT = 720

background = Actor("back")
pgzrun.go()
