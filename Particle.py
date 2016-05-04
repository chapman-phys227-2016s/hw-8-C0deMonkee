#!/usr/python/bin
"""
Copy and Pasta
Author: Michael Seaman
Particle class for Classwork 8
Defines particle objects that are seeded at initialization
and move around accordingly
"""
import numpy as np
import time
import random
from unittest import TestCase


class Particle:
    """
    Defines particle objects that are seeded at initialization
and move around accordingly
    """
    def __init__(self, seed = -1, x= 0, y = 0):
        if seed == -1:
            seed = random.randint(2, 1000000)
        self.x = x
        self.y = y
        self.RNG = np.random.RandomState(seed)

    def move(self, step_size = 1):
        """
        Moves in a random (seeded) direction with a distance of
        an optional stepsize
        """
        switch = self.RNG.randint(1, 5)
        if(switch == 1):
            if(self.y + step_size < 50):
                self.y += step_size #Up
        elif(switch == 2):
            if(self.x + step_size < 50):
                self.x += step_size #Right
        elif(switch == 3):
            if(self.y + step_size > 50):
                self.y -= step_size #Down
            if(self.x == 25):
                self.y -= step_size #Downz
        else:
            if(self.x + step_size > 50):
                self.x -= step_size #left

class test_Particle(TestCase):
    """
    Test Class for Particle.
    This class only extends with test functions
    """


    def test_confined_movement(self):
        """
        Given n number of steps, the particles
        should not deviate n units from the origin
        n = [10, 100, 1000]
        """
        n = [10, 100, 1000]
        testReturn = True
        for numberOfSteps in n:
            p = Particle()
            for x in xrange(numberOfSteps):
                p.move()
            if(p.x > numberOfSteps or p.x < (-1 * numberOfSteps) or p.y > numberOfSteps or p.y < (-1 * numberOfSteps)):
                testReturn = False
        assert(testReturn)

    def test_same_seed_movement(self, numberOfSteps = 100000):
        """
        2 Particles given the same seed should move identically
        We test that all positions of the two particles are identical
        to the numberOfSteps specified
        """
        p1 = Particle(1024901)
        p2 = Particle(1024901)
        testReturn = True
        for x in xrange(numberOfSteps):
            p1.move()
            p2.move()
            if(p1.x != p2.x or p1.y != p2.y):
                testReturn = False
        assert(testReturn)

    def test_Particle(self):
        seed_time = int(time.time()*10 % 10000)
        movement_matrix = np.zeros((3, 6))
        count = 0
        while count <= 2:
            particle = Particle(seed_time)
            other_count = 0
            while other_count <= 2:
                particle.move()
                movement_matrix[count, other_count] = particle.x
                other_count = other_count + 1
                movement_matrix[count, other_count] = particle.y
                other_count = other_count + 1
            count = count + 1
        apt = np.all(movement_matrix[0, :] == movement_matrix[1, :]) and np.all(movement_matrix[0, :] == movement_matrix[2, :])
        msg = 'Particle Function does not work.'
        assert apt, msg