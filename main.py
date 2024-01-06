import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


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
    # mario section:
    if keyboard.right:
        mario.x += 5
    if keyboard.left:
        mario.x -= 5
    if keyboard.up:
        mario.y -= 5
    if keyboard.down:
        mario.y += 5

    # luigi section:
    if keyboard.d:
        luigi.x += 5
    if keyboard.a:
        luigi.x -= 5
    if keyboard.w:
        luigi.y -= 5
    if keyboard.s:
        luigi.y += 5


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
