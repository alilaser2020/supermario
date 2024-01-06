import random
import pgzrun
from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def enemy_random_direction():
    enemy.x_dir = random.randint(-5, 5)
    enemy.y_dir = random.randint(-5, 5)
    if enemy.x_dir > 0:
        enemy.image = "enemy_right"
    else:
        enemy.image = "enemy_left"


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
    """A method for drawing anything with any change (execute by pgzrun.go())"""
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
        mario.image = "mario_right"
    if keyboard.left:
        mario.x -= 5
        mario.image = "mario_left"
    if keyboard.up:
        mario.y -= 5
    if keyboard.down:
        mario.y += 5
    actor_correct_location(mario)

    # luigi section:
    if keyboard.d:
        luigi.x += 5
        luigi.image = "luigi_right"
    if keyboard.a:
        luigi.x -= 5
        luigi.image = "luigi_left"
    if keyboard.w:
        luigi.y -= 5
    if keyboard.s:
        luigi.y += 5
    actor_correct_location(luigi)

    # enemy section:
    enemy.x += enemy.x_dir
    enemy.y += enemy.y_dir
    actor_correct_location(enemy)


WIDTH = 1280
HEIGHT = 720

background = Actor("back")
mario = Actor("mario_right")
mario.x = WIDTH // 2
mario.y = HEIGHT // 2

luigi = Actor("luigi_right")
luigi.x = 90
luigi.y = 550

enemy = Actor("enemy_right")
enemy.x = 1100
enemy.y = 591
enemy.x_dir = 2
enemy.y_dir = 2

clock.schedule_interval(enemy_random_direction, 4)

pgzrun.go()
