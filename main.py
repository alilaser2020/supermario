import sys
import pgzrun
import random
import pygame.display

from pgzero import clock
from ctypes import windll
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
    random_location(coin_2)


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


def collide_coin(actor, condicate_coin):
    """
    A method for when each actor collide with coin, it's score was increase (execute by pgzrun.go())
    :param actor:
    :param condicate_coin:
    :return:
    """
    global status
    if actor.colliderect(condicate_coin):
        sounds.jiring.play()
        actor.score += condicate_coin.point
        random_location(condicate_coin)
        if actor.score >= 100 and actor == mario:
            status = "mario_win"
        if actor.score >= 100 and actor == luigi:
            status = "luigi_win"


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
        coin_2.draw()
        mushroom.draw()
        mode.screen.draw.text("mario score: " + str(mario.score), (10, 10),
                              color="yellow", fontsize=40, gcolor="red", scolor="black", shadow=(1, 1), alpha=0.8)
        mode.screen.draw.text("luigi score: " + str(luigi.score), (1060, 10),
                              color="yellow", fontsize=40, gcolor="red", scolor="black", shadow=(1, 1), alpha=0.8)
    elif status == "mario_win":
        mode.screen.blit("mario_win", (0, 0))
        mode.screen.draw.text("mario score: " + str(mario.score), topleft=(10, 10), fontsize=50, color="blue", gcolor="green",
                              scolor="red", shadow=(1, 1), alpha=0.9)
        mode.screen.draw.text("luigi score: " + str(luigi.score), topleft=(1050, 10), fontsize=40, color="blue",
                              gcolor="green",
                              scolor="black", shadow=(1, 1), alpha=0.9)
    elif status == "luigi_win":
        mode.screen.blit("luigi_win", (0, 0))
        mode.screen.draw.text("mario score: " + str(mario.score), topleft=(10, 10), fontsize=40, color="blue"
                              , gcolor="orange", scolor="red", shadow=(1, 1), alpha=0.9)
        mode.screen.draw.text("luigi score: " + str(luigi.score), topleft=(1030, 10), fontsize=50, color="blue",
                              gcolor="orange",
                              scolor="black", shadow=(1, 1), alpha=0.9)
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
    elif keyboard.f:
        mode.screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif keyboard.n:
        mode.screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    elif keyboard.escape:
        status = "end"
        clock.schedule(quite_func, 3)
    elif keyboard.c:
        sys.exit(0)


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
        collide_coin(mario, coin)
        collide_coin(mario, coin_2)
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
        collide_coin(luigi, coin)
        collide_coin(luigi, coin_2)
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
hwnd = pygame.display.get_wm_info()["window"]
windll.user32.MoveWindow(hwnd, 330, 150, WIDTH, HEIGHT, False)  # Depends on the device screen site
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

# define coin:
coin_2 = Actor("coin2")
random_location(coin_2)
coin_2.point = 20

# Define mushroom:
mushroom = Actor("mushroom")
random_location(mushroom)
mushroom.speed = 12

pgzrun.go()
