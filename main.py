import random
import sys

import pgzrun
from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds


def reset_actors():
    """
    A method for reset every actors (execute by pgzrun.go())
    :return:
    """
    mario.score = luigi.score = 0
    mario.speed = luigi.speed = 5
    random_location(mario)
    random_location(luigi)
    random_location(enemy)
    random_location(mushroom)
    random_location(coin)


def reset_mario_speed():
    """
    A method for reset speed of mario (execute by pgzrun.go())
    :return:
    """
    mario.speed = 5
    mario.power = False


def reset_luigi_speed():
    """
    A method for reset speed of mario (execute by pgzrun.go())
    :return:
    """
    luigi.speed = 5
    luigi.power = False


def collide_coin(actor):
    """
    A method for when each actor collide with coin, it's score was increase (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.colliderect(coin):
        sounds.jiring.play()
        actor.score += coin.point
        random_location(coin)


def random_location(actor):
    """
    A method for specify random location for each actor in page (execute by pgzrun.go())
    :param actor:
    :return:
    """
    actor.x = random.randint(actor.width // 2, WIDTH - actor.width // 2)
    actor.y = random.randint(actor.height // 2, HEIGHT - actor.height // 2)


def enemy_random_direction():
    enemy.x_dir = random.randint(-enemy.speed, enemy.speed)
    enemy.y_dir = random.randint(-enemy.speed, enemy.speed)
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
    if status == "home":
        mode.screen.blit("home", (0, 0))
    elif status == "play":
        background.draw()
        mario.draw()
        luigi.draw()
        enemy.draw()
        coin.draw()
        mushroom.draw()
        mode.screen.draw.text("mario score: " + str(mario.score), (10, 10),
                              color="yellow", fontsize=40, gcolor="red", scolor="black", shadow=(1, 1), alpha=0.8)
        mode.screen.draw.text("luigi score: " + str(luigi.score), (1050, 10),
                              color="yellow", fontsize=40, gcolor="red", scolor="black", shadow=(1, 1), alpha=0.8)
    elif status == "end":
        mode.screen.blit("end", (0, 0))


def quite_func():
    """
    A method for existing from game (execute by pgzrun.go())
    :return:
    """
    quit()


def on_key_down():
    """
    A method for occurrence an event when press down a specific key on keyboard (execute by pgzrun.go())
    :return:
    """
    global status
    if keyboard.space and status == "home":
        status = "play"
        clock.schedule_interval(enemy_random_direction, 4)
    elif keyboard.h and status != "home":
        status = "home"
        reset_actors()
    elif keyboard.p and status != "play":
        status = "play"
        reset_actors()
    elif keyboard.escape:
        status = "end"
        clock.schedule(quite_func, 3)
    elif keyboard.c:
        quit()


def update():
    """
    A method for updating and refresh 60 times per second (execute by pgzrun.go())
    :return:
    """
    global status
    if status == "play":
        # mario section:
        if keyboard.right:
            mario.x += mario.speed
            mario.image = "mario_right"
        if keyboard.left:
            mario.x -= mario.speed
            mario.image = "mario_left"
        if keyboard.up:
            mario.y -= mario.speed
        if keyboard.down:
            mario.y += mario.speed
        if mario.colliderect(mushroom):
            sounds.speed.play()
            mario.speed = mushroom.speed
            mario.power = True
            print(f"mario power: {mario.power}")
            clock.schedule_unique(reset_mario_speed, 5)
            random_location(mushroom)
        collide_coin(mario)
        actor_correct_location(mario)

        # luigi section:
        if keyboard.d:
            luigi.x += luigi.speed
            luigi.image = "luigi_right"
        if keyboard.a:
            luigi.x -= luigi.speed
            luigi.image = "luigi_left"
        if keyboard.w:
            luigi.y -= luigi.speed
        if keyboard.s:
            luigi.y += luigi.speed
        if luigi.colliderect(mushroom):
            sounds.speed.play()
            luigi.speed = mushroom.speed
            luigi.power = True
            print(f"luigi power: {luigi.power}")
            clock.schedule_unique(reset_luigi_speed, 5)
            random_location(mushroom)
        collide_coin(luigi)
        actor_correct_location(luigi)

        # enemy section:
        enemy.x += enemy.x_dir
        enemy.y += enemy.y_dir
        actor_correct_location(enemy)


WIDTH = 1280
HEIGHT = 720
status = "home"
mode = sys.modules["__main__"]

# define background:
background = Actor("back")

# define mario actor:
mario = Actor("mario_right")
random_location(mario)
mario.score = 0
mario.speed = 5
mario.power = False

# define luigi actor:
luigi = Actor("luigi_right")
random_location(luigi)
luigi.score = 0
luigi.speed = 5
luigi.power = False

# define enemy actor:
enemy = Actor("enemy_right")
random_location(enemy)
enemy.speed = 7
enemy.x_dir = enemy.speed
enemy.y_dir = enemy.speed

# define coin:
coin = Actor("coin")
random_location(coin)
coin.point = 10

# Define mushroom:
mushroom = Actor("mushroom")
random_location(mushroom)
mushroom.speed = 12

pgzrun.go()
