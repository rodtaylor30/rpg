#!/usr/bin/env python.

"""
    This file defines the maze

"""

import random
import unittest

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2018, Egertiko Designs"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Sven Eggert"
__email__ = "sven674@web.de"
__status__ = "Development"

"""

    The maze class

"""
class Maze(unittest.TestCase):
    MAZE_SIZE_X = 50
    MAZE_SIZE_Y = 50
    MIN_MAZE_SIZE_X = 2
    MIN_MAZE_SIZE_Y = 2
    LEAVE_OUT_X_1 = 0
    LEAVE_OUT_X_2 = 1
    LEAVE_OUT_Y_1 = 2
    LEAVE_OUT_Y_2 = 3
    WALL_NORTH = 1
    WALL_SOUTH = 2
    WALL_WEST = 4
    WALL_EAST = 8
	MazeArray = [][]
	
    """
        Constructor
    """
	def __init__(self):
		# The complete maze as array
		MazeArray = [[0 for x in range(MAZE_SIZE_X)] for y in range(MAZE_SIZE_Y)]

		# Wall to the north and south
		for x in range(MAZE_SIZE_X-1):
			MazeArray[x][0] = WALL_NORTH 
			MazeArray[x][MAZE_SIZE_Y-1] = WALL_SOUTH

		# Wall to the west and east
		for y in range(MAZE_SIZE_Y-1):
			MazeArray[0][y] = MazeArray[0][y] | WALL_WEST 
			MazeArray[MAZE_SIZE_X-1][y] = MazeArray[MAZE_SIZE_X-1][y] | WALL_EAST

    """
        Create a random maze
    """
	def createRandomMaze(self):				
		__createRandomMaze(0, MAZE_SIZE_X, 0, MAZE_SIZE_Y)
		
    """
        Create a random maze
		private sub routine
    """
    def __createRandomMaze(self, chamberMinX, chamberMaxX, chamberMinY, chamberMaxY):
		# check minimum size of chamber
		if (chamberMaxX - chamberMinX) < MIN_MAZE_SIZE_X:
			return

		# check minimum size of chamber
		if (chamberMaxY - chamberMinY) < MIN_MAZE_SIZE_Y:
			return

		wallX = randint(chamberMinX+1, chamberMaxX-1)
		wallY = randint(chamberMinY+1, chamberMaxY-1)

		# select a number between 0 and 3
		leaveOut = randint(0, 3))
		
		# hole in the wall
		firstHole = randint(chamberMinX, wallX-1)
		secondHole = randint(wallX, chamberMaxX-1)
		
		for x in range(chamberMaxX-1):
			if (x < wallX and if leaveOut != LEAVE_OUT_X_1 and x != firstHole) or (x >= wallX and if leaveOut != LEAVE_OUT_X_2 and x != secondHole): 
				MazeArray[x][wallY] = MazeArray[x][wallY] | EXIT_SOUTH 
				MazeArray[x][wallY+1] = MazeArray[x][wallY+1] | EXIT_NORTH

		# hole in the wall
		firstHole = randint(chamberMinY, wallY-1)
		secondHole = randint(wallY, chamberMaxY-1)
				
		for y in range(chamberMaxY-1):
			if (y < wallY and if leaveOut != LEAVE_OUT_Y_1 and x != firstHole) or (y >= wallY and if leaveOut != LEAVE_OUT_Y_2 and x != secondHole): 
				MazeArray[wallX][y] = MazeArray[wallX][y] | EXIT_WEST 
				MazeArray[x][wallY-1] = MazeArray[x][wallY-] | EXIT_EAST
					
		__createRandomMaze(chamberMinX, wallX, chamberMinY, wallY)		# Quarter 0
		__createRandomMaze(wallX, chamberMaxX, chamberMinY, wallY)		# Quarter 1
		__createRandomMaze(wallX, chamberMaxX, wallY, chamberMaxY)		# Quarter 2
		__createRandomMaze(chamberMinX, wallX, wallY, chamberMaxY)		# Quarter 3

  """
    Test creating persons
  """
  def test_createMaze(self):
	createRandomMaze()
	
if __name__ == '__main__':
    unittest.main()		
