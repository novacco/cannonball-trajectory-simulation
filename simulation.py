import math

# CONSTANTS FOR EQUATIONS
h = 0.001 # simulation step
g = 9.81 # gravitation


def simulation(angle, mass, air_resistance, initial_velocity):
    listX = []
    listY = []
    listT = []

    prevX = 0
    prevY = 0
    prev_velocityX = initial_velocity * math.cos(math.radians(angle))
    prev_velocityY = initial_velocity * math.sin(math.radians(angle))

    while prevY >= 0:
        pass


def velocityX(prev_velocityX, air_resistance, mass):
    return prev_velocityX - (h * air_resistance * prev_velocityX) / mass


def vectorX(prevX, prev_velocityX, air_resistance, mass):
    return prevX + h * velocityX(prev_velocityX, air_resistance, mass) - (h*h * air_resistance * velocityX(prev_velocityX, air_resistance, mass) / (2 * mass)


def velocityY(prev_velocityY, air_resistance, mass):
    return prev_velocityY - h * g - h * air_resistance * prev_velocityY / mass


def vectorY(prevY, prev_velocityY, air_resistance, mass):
    return prevY + h * velocityY(prev_velocityY, air_resistance, mass) + (h*h) * (-g-( air_resistance * velocityY(prev_velocityY, air_resistance, mass)) / mass) / 2






