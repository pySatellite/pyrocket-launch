#!/bin/python3

# Import library code
from p5 import *
from random import randint
import os


# Setup global variables
screen_size = 400
rocket_y = screen_size
burn = 100
orbit_radius = 250
orbit_y = screen_size - orbit_radius
image_path = os.path.join(os.path.dirname(__file__), "images")


def setup():
    print(image_path)
    size(screen_size, screen_size)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image(f'/Users/m2/code/pysatellite/pyrocket-launch/src/pyrocket_launch/images/planet.png')
    rocket = load_image(f'/Users/m2/code/pysatellite/pyrocket-launch/src/pyrocket_launch/images/rocket.png')


def draw_rocket():
    global rocket_y, fuel, burn  # Use the global rocket_y variable

    if fuel >= burn and rocket_y > orbit_y:
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

        if fuel < burn and rocket_y > orbit_y:  # No more fuel and not in orbit
            tint(255, 0, 0)  # Failure
        elif fuel < 1000 and rocket_y <= orbit_y:
            tint(0, 255, 0)
        elif fuel >= 1000 and rocket_y <= orbit_y:
            tint(255, 200, 0)

    image(rocket, screen_size/2, rocket_y, 64, 64)
    # no_tint()


def draw_background():
    background(0)  # Short for background(0, 0, 0) — black
    image(planet, 400/2, 400, 300, 300)  # Draw the image

    no_fill()
    stroke(255)
    stroke_weight(2)
    ellipse(screen_size/2, screen_size, orbit_radius * 2, orbit_radius * 2)


def draw():
    draw_background()
    draw_rocket()

print(image_path)
fuel = int(input('How many kilograms of fuel do you want to use? '))
# fuel = 50000
run()

if __name__ == "__main__":
    # execute only if run as a script
    run()
