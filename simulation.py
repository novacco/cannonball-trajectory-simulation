import math
import numpy as np

# CONSTANTS FOR EQUATIONS
h = 0.001  # simulation step
g = 9.81  # gravitation


def simulation(angle, mass, air_resistance, initial_velocity):
    listX = []
    listY = []
    listT = []

    t = 0
    prevX = 0
    prevY = 0
    prev_velocityX = initial_velocity * math.cos(math.radians(angle))
    prev_velocityY = initial_velocity * math.sin(math.radians(angle))

    while prevY >= 0:
        X = vectorX(prevX, prev_velocityX, air_resistance, mass)
        Y = vectorY(prevY, prev_velocityY, air_resistance, mass)

        listX.append(X)
        listY.append(Y)

        prevX = X
        prevY = Y

        prev_velocityX = velocityX(prev_velocityX, air_resistance, mass)
        prev_velocityY = velocityY(prev_velocityY, air_resistance, mass)

        listT.append(t)
        t += h

    return [listX, listY, listT]


def velocityX(prev_velocityX, air_resistance, mass):
    return prev_velocityX - (h * air_resistance * prev_velocityX) / mass


def vectorX(prevX, prev_velocityX, air_resistance, mass):
    return prevX + h * velocityX(prev_velocityX, air_resistance, mass) - (
                h * h * air_resistance * velocityX(prev_velocityX, air_resistance, mass) / (2 * mass))


def velocityY(prev_velocityY, air_resistance, mass):
    return prev_velocityY - h * g - h * air_resistance * prev_velocityY / mass


def vectorY(prevY, prev_velocityY, air_resistance, mass):
    return prevY + h * velocityY(prev_velocityY, air_resistance, mass) + (h * h) * (
                -g - (air_resistance * velocityY(prev_velocityY, air_resistance, mass)) / mass) / 2


def find_optimal_angle(mass, air_resistance, initial_velocity):
    listRange = []
    for angle in np.arange(0, 90, 0.1):
        listRange.append(simulation(angle, mass, air_resistance, initial_velocity)[0][-1])
    return listRange.index(max(listRange)) / 10


def max_values(angle, mass, air_resistance, initial_velocity):
    sim = simulation(angle, mass, air_resistance, initial_velocity)
    max_height = max(sim[1])
    time_to_max = sim[1].index(max_height) * h
    flight_time = len(sim[0]) * h
    max_range = max(sim[0])
    return [max_height, time_to_max, flight_time, max_range]
