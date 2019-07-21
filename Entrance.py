#!/usr/bin/env python.

"""
    This file defines an entrance

"""

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2018"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Sven Eggert"
__email__ = ""
__status__ = "Development"

"""

    The entrance class

"""
class Entrance:
    """
        The constructor
    
        Args:
            entranceX: This is the x-Position of the entrance.
            entranceY: This is the y-Position of the entrance.
            entranceFrom: This is the side of the entrance e.g. entrance from north
            deadEnds: This is the list of the dead ends of the entrance
        
        Returns:
            Nothing
        
        Raises:
            Nothing
    """
    def __init__(self, entranceX = None, entranceY = None, entranceFrom = None, deadEnds = None):
        self.EntranceX = entranceX
        self.EntranceY  = entranceY
        self.EntranceFrom = entranceFrom
        #print("entrance: ", self.EntranceX, self.EntranceY, self.EntranceFrom)
        self.DeadEnds = deadEnds
        
    """
        The X position of entrance
    """
    EntranceX = 0
    
    """
        The Y position of the entrance
    """
    EntranceY = 0
    
    """
        On which side is the entrance, from the North etc.
    """
    EntranceFrom = 0

    """
       An array list of the dead ends
    """
    DeadEnds = []

    def getWeightedMeasure(self):
        weightedMeasure = 0.0   
        for deadEnd in self.DeadEnds:
            weightedMeasure = deadEnd.getWeightedMeasure(self.EntranceX, self.EntranceY)
        return weightedMeasure
