#!/usr/bin/env python.

"""
    This file defines the maze

"""

from random import randint
import unittest
import logging, sys
import sys

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
    MAZE_SIZE_X = 10
    MAZE_SIZE_Y = 10
    MIN_MAZE_SIZE_X = 1
    MIN_MAZE_SIZE_Y = 1
    LEAVE_OUT_X_1 = 0
    LEAVE_OUT_X_2 = 1
    LEAVE_OUT_Y_1 = 2
    LEAVE_OUT_Y_2 = 3
    WALL_NORTH = 1
    WALL_SOUTH = 2
    WALL_WEST = 4
    WALL_EAST = 8
    MazeArray = ()
    
    """
        Constructor
    """
    def __init__(self, *args, **kwargs):    # needed for unittest
        super().__init__(*args, **kwargs)

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        
        # The complete maze as array
        self.MazeArray = [[0 for x in range(self.MAZE_SIZE_X)] for y in range(self.MAZE_SIZE_Y)]

        # Wall to the north and south
        for x in range(self.MAZE_SIZE_X):
            self.MazeArray[x][0] = self.WALL_NORTH 
            self.MazeArray[x][self.MAZE_SIZE_Y-1] = self.WALL_SOUTH

        # Wall to the west and east
        for y in range(self.MAZE_SIZE_Y):
            self.MazeArray[0][y] = self.MazeArray[0][y] | self.WALL_WEST 
            self.MazeArray[self.MAZE_SIZE_X-1][y] = self.MazeArray[self.MAZE_SIZE_X-1][y] | self.WALL_EAST

    """
        Create a random maze
    """
    def createRandomMaze(self):                
        self.__createRandomMaze(0, self.MAZE_SIZE_X-1, 0, self.MAZE_SIZE_Y-1)
        
    """
        Create a random maze
        private sub routine
    """
    def __createRandomMaze(self, chamberMinX, chamberMaxX, chamberMinY, chamberMaxY):        
        # check minimum size of chamber
        if (chamberMaxX - chamberMinX) < self.MIN_MAZE_SIZE_X:
            return

        # check minimum size of chamber
        if (chamberMaxY - chamberMinY) < self.MIN_MAZE_SIZE_Y:
            return

        # Create two random walls
        wallX = randint(chamberMinX, chamberMaxX-1) # 0..8 -> 6
        wallY = randint(chamberMinY, chamberMaxY-1) # 0..8

        logging.info("(%d, %d), (%d, %d), walls (%d, %d)", chamberMinX, chamberMinY, chamberMaxX, chamberMaxY, wallX, wallY)

        # select a number between 0 and 3
        leaveOut = randint(0, 3) # 0..3
        
        # hole in the wall
        firstHole = randint(chamberMinX, wallX)     # 0..6
        secondHole = randint(wallX+1, chamberMaxX)  # 7..9

        logging.info("holes (%d, %d)", firstHole, secondHole)

        # Horizontal wall
        for x in range(chamberMinX,chamberMaxX+1): # 0..9
            if (x <= wallX and x != firstHole) or (x > wallX and x != secondHole): 
                self.MazeArray[x][wallY] = self.MazeArray[x][wallY] + self.WALL_SOUTH
                if wallY < self.MAZE_SIZE_Y:
                    self.MazeArray[x][wallY+1] = self.MazeArray[x][wallY+1] + self.WALL_NORTH

        # hole in the wall
        firstHole = randint(chamberMinY, wallY)
        secondHole = randint(wallY+1, chamberMaxY)

        logging.info("holes (%d, %d)", firstHole, secondHole)
     
        for y in range(chamberMinY,chamberMaxY+1):
            if (y <= wallY and y != firstHole) or (y > wallY and y != secondHole): 
                self.MazeArray[wallX][y] = self.MazeArray[wallX][y] | self.WALL_EAST
                if wallX < self.MAZE_SIZE_X:
                    self.MazeArray[wallX+1][y] = self.MazeArray[wallX+1][y] | self.WALL_WEST

        print()

        self.__createRandomMaze(chamberMinX, wallX, chamberMinY, wallY)        # Quarter 0
        self.__createRandomMaze(wallX+1, chamberMaxX, chamberMinY, wallY)      # Quarter 1
        self.__createRandomMaze(wallX+1, chamberMaxX, wallY+1, chamberMaxY)    # Quarter 2
        self.__createRandomMaze(chamberMinX, wallX, wallY+1, chamberMaxY)      # Quarter 3

    """
        Draw random maze
    """
    def drawMaze(self):
        for y in range(self.MAZE_SIZE_Y):
            for x in range(self.MAZE_SIZE_X): # 0..9
                sys.stdout.write("+")
                
                if (self.MazeArray[x][y] & self.WALL_NORTH) > 0:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")

            sys.stdout.write("+")
                    
            print()

            # 2nd row
            for x in range(self.MAZE_SIZE_X):
                if (self.MazeArray[x][y] & self.WALL_WEST) > 0:
                    sys.stdout.write("| ")
                else:
                    sys.stdout.write("  ")

            if (self.MazeArray[self.MAZE_SIZE_X-1][y] | self.WALL_EAST) > 0:
                sys.stdout.write("|")
       
            print()

        for x in range(self.MAZE_SIZE_X): # 0..9
            sys.stdout.write("+")
            
            if (self.MazeArray[x][self.MAZE_SIZE_Y-1] & self.WALL_SOUTH) > 0:
                sys.stdout.write("-")
            else:
                sys.stdout.write(" ")

        sys.stdout.write("+")

    """
        Test creating persons
    """
    def test_createMaze(self):
        self.createRandomMaze()
        self.drawMaze()
    
if __name__ == '__main__':
    unittest.main()        
		
