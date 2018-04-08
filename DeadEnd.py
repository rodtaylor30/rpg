#!/usr/bin/env python.

import math

"""
    This file defines the maze

"""

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2018, Egertiko Designs"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Sven Eggert"
__email__ = ""
__status__ = "Development"

"""

    The dead end class

"""
class DeadEnd:
    """
        The constructor
    """
    def __init__(self, posX, posY, pace):
        self.posX = posX
        self.posY  = posY
        self.pace = pace
        
    """
        The X position of the dead end
    """
    posX = 0
    
    """
        The Y position of the dead end
    """
    posY = 0

    """
       The number of steps needed to walk to the dead end
    """
    pace = 0
    

    """
       Calculate the distance to the entrance aka start of the maze
    """
    def __getDistance(self, startX, startY):
        # Pythagoras
        csquare = ((startX - self.posX) ** 2) + ((startY - self.posY) ** 2)
        return math.sqrt(csquare) 
    
    """
       Calculate the weighted measure of the key data of a dead end
    """
    def getWeightedMeasure(self, startX, startY):    
        distance = self.__getDistance(startX, startY)
        return distance + self.pace 
