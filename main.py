import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def actor_correct_location(actor):
    """
    A method for avoidance out of page and detect correct location for each actor (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.x >= WIDTH + actor.width // 2:
        actor.x = -actor.width // 2
    if actor.x < -actor.width // 2:
        actor.x = WIDTH + actor.width // 2
    if actor.y >= HEIGHT + actor.height // 2:
        actor.y = -actor.height // 2
    if actor.y < -actor.height // 2:
        actor.y = HEIGHT + actor.height // 2


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

    actor_correct_location(mario)

    # luigi section:
    if keyboard.d:
        luigi.x += 5
    if keyboard.a:
        luigi.x -= 5
    if keyboard.w:
        luigi.y -= 5
    if keyboard.s:
        luigi.y += 5

    actor_correct_location(luigi)

    # enemy section:
    enemy.x += -5
    enemy.y += 5
    actor_correct_location(enemy)


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
