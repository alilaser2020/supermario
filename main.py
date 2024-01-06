import random
import sys

import pgzrun
from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def random_location(actor):
    """
    A method for specify random location for each actor in page (execute by pgzrun.go())
    :param actor:
    :return:
    """
    actor.x = random.randint(actor.width // 2, WIDTH - actor.width // 2)
    actor.y = random.randint(actor.height // 2, HEIGHT - actor.height // 2)


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
    coin.draw()
    mode.screen.draw.text("mario score: " + str(mario.score), (10, 30),
                          color="yellow", fontsize=30)
    mode.screen.draw.text("luigi score: " + str(luigi.score), (1100, 30),
                          color="yellow", fontsize=30)


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
    if mario.colliderect(coin):
        mario.score += coin.point
        random_location(coin)
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
    if luigi.colliderect(coin):
        luigi.score += coin.point
        random_location(coin)
    actor_correct_location(luigi)

    # enemy section:
    enemy.x -= enemy.x_dir
    enemy.y += enemy.y_dir
    actor_correct_location(enemy)


WIDTH = 1280
HEIGHT = 720
mode = sys.modules["__main__"]

# define background:
background = Actor("back")

# define mario actor:
mario = Actor("mario_right")
random_location(mario)
mario.score = 0

# define luigi actor:
luigi = Actor("luigi_right")
random_location(luigi)
luigi.score = 0

# define enemy actor:
enemy = Actor("enemy_left")
random_location(enemy)
enemy.x_dir = 2
enemy.y_dir = 2
clock.schedule_interval(enemy_random_direction, 4)

# define coin:
coin = Actor("coin")
random_location(coin)
coin.point = 10
pgzrun.go()
