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
    pass


def vectorX(prevX, prev_velocityX, air_resistance, mass):
    pass


def velocityY(prev_velocityY, air_resistance, mass):
    pass


def vectorY(prevY, prev_velocityY, air_resistance, mass):
    pass




