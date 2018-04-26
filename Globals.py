#!/usr/bin/env python.

"""
    This file defines the globals

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

    The global constants
    
"""

WALL_NORTH = 1
WALL_SOUTH = 2
WALL_WEST = 4
WALL_EAST = 8

GONE_EAST = 1
GONE_SOUTH = 2
GONE_WEST = 4
GONE_NORTH = 8
GONE_STOP = 8
GONE_ALL = 15

MAX_MAZE_LEVEL = 10         # The maximum levels of the maze
MIN_MAZE_LEVEL = 2          # The minimum levels of the maze
MAZE_SIZE_X = 50            # The maximum size of the maze in X-direction
MAZE_SIZE_Y = 50            # The maximum size of the maze in Y-direction
MIN_MAZE_SIZE_X = 10        # The minimum size of the maze in X-direction
MIN_MAZE_SIZE_Y = 10    
MAX_MAZE_SIZE_X = 50        # The minimum size of the maze in X-direction
MAX_MAZE_SIZE_Y = 50    

LEAVE_OUT_X_1 = 0
LEAVE_OUT_X_2 = 1
LEAVE_OUT_Y_1 = 2
LEAVE_OUT_Y_2 = 3
