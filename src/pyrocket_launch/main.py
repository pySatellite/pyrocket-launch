#!/bin/python3

# Import library code
from p5 import *
from random import randint


# Setup global variables
screen_size = 400
rocket_y = screen_size
burn = 100

# The draw_rocket function goes here


# The draw_background function goes here


def setup():
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')


def draw_rocket():
    global rocket_y, fuel, burn  # Use the global rocket_y variable

    if fuel >= burn:
        rocket_y -= 1  # Move the rocket
        fuel -= burn
        print('Fuel left: ', fuel)
        no_stroke()

        for i in range(25):
            fill(255, 255 - i * 10, 0)
            ellipse(screen_size/2, rocket_y + i, 8, 3)

        fill(200, 200, 200, 100)
        for i in range(20):
            ellipse(screen_size/2 + randint(-5, 5), rocket_y + randint(20, 50), randint(5, 10), randint(5, 10))

    image(rocket, screen_size/2, rocket_y, 64, 64)


def draw_background():
    background(0)  # Short for background(0, 0, 0) — black
    image(planet, 400/2, 400, 300, 300)  # Draw the image


def draw():
    draw_background()
    draw_rocket()

fuel = int(input('How many kilograms of fuel do you want to use?'))
run()
