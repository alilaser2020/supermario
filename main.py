import pgzrun
from pgzero.actor import Actor


def draw():
    """
    A method for drawing anything with any change (execute by pgzrun.go())
    :return:
    """
    background.draw()
    mario.draw()
    luigi.draw()
    enemy.draw()


def update():
    """
    A method for updating and refresh 60 times per second (execute by pgzrun.go())
    :return:
    """
    pass


WIDTH = 1280
HEIGHT = 720

background = Actor("back")
mario = Actor("mario_right")
luigi = Actor("luigi_right")
enemy = Actor("enemy_left")

mario.x = WIDTH // 2
mario.y = HEIGHT // 2

luigi.x = 90
luigi.y = 550

enemy.x = 1100
enemy.y = 591


pgzrun.go()
