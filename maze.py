#!/usr/bin/env python.

"""
    This file defines the maze

"""

from random import randint
import unittest
import logging, sys
import sys
import pickle
import tempfile
from DeadEnd import DeadEnd 
from Entrance import Entrance
import Globals as gl
from _overlapped import NULL

__author__ = "Sven Eggert"
__copyright__ = "Copyright 2018, Egertiko Designs"
__credits__ = []
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Sven Eggert"
__email__ = ""
__status__ = "Development"

"""

    The maze class

"""
class Maze(unittest.TestCase):
    MazeArray = ()
    __mazeFileName = ""
    SearchMazeArray = ()
    SearchMazeList = []
    Entrances = []
    
    """
        Constructor
    """
    def __init__(self, *args, **kwargs):    # needed for unittest
        super().__init__(*args, **kwargs)

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        
        # The complete maze as array
        self.MazeArray = [[0 for x in range(gl.MAZE_SIZE_X)] for y in range(gl.MAZE_SIZE_Y)]

        # Wall to the north and south
        for x in range(gl.MAZE_SIZE_X):
            self.MazeArray[x][0] = gl.WALL_NORTH 
            self.MazeArray[x][gl.MAZE_SIZE_Y-1] = gl.WALL_SOUTH

        # Wall to the west and east
        for y in range(gl.MAZE_SIZE_Y):
            self.MazeArray[0][y] = self.MazeArray[0][y] | gl.WALL_WEST 
            self.MazeArray[gl.MAZE_SIZE_X-1][y] = self.MazeArray[gl.MAZE_SIZE_X-1][y] | gl.WALL_EAST

    """
        Create a random maze
    """
    def createRandomMaze(self):                
        self.__createRandomMaze(0, gl.MAZE_SIZE_X-1, 0, gl.MAZE_SIZE_Y-1)

    """
        Save the random maze
    """
    def __saveMaze(self):
        with tempfile.NamedTemporaryFile(delete = False) as fp:
            # the file is deleted as soon as it is closed. 
            self.__mazeFileName = fp.name
            print(self.__mazeFileName)
            pickle.dump(self.MazeArray, fp)

    """
        Load the random maze
    """
    def __loadMaze(self):
        self.MazeArray = ()
        with open (self.__mazeFileName , 'rb') as fp:
            self.MazeArray = pickle.load(fp)

    """
        Create an exit for the maze
        
    
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
    def __findPathInMaze(self, entranceX, entranceY, entranceFrom):
        self.SearchMazeArray = [[0 for x in range(gl.MAZE_SIZE_X)] for y in range(gl.MAZE_SIZE_Y)]
        deadEnds = []
        
        # walk through the maze
        self.__searchPathThroughMazeV2(entranceX, entranceY, 0, entranceFrom, deadEnds)
        
        # save the entrances to a list
        entrance = Entrance(entranceX, entranceY, entranceFrom, deadEnds)
        self.Entrances.append(entrance)
        
        return deadEnds
 
    """
        Search a path through the maze
    """
    def __searchPathThroughMazeV2(self, x, y, pace, gone, deadEnds):
        if self.SearchMazeArray[x][y] == 1:
            return
        
        self.SearchMazeArray[x][y] = 1
        actualRoom = self.MazeArray[x][y]
      
        #print(x,y, pace)
        
        pace = pace + 1

        if (actualRoom & gl.WALL_EAST) == 0 and gone != gl.GONE_WEST and x < gl.MAZE_SIZE_X-1:
            self.__searchPathThroughMazeV2(x + 1, y, pace, gl.GONE_EAST, deadEnds)
        if (actualRoom & gl.WALL_SOUTH) == 0 and gone != gl.GONE_NORTH and y < gl.MAZE_SIZE_Y-1:
            self.__searchPathThroughMazeV2(x, y + 1, pace, gl.GONE_SOUTH, deadEnds)
        if (actualRoom & gl.WALL_WEST) == 0 and gone != gl.GONE_EAST and x > 0:
            self.__searchPathThroughMazeV2(x - 1, y, pace, gl.GONE_WEST, deadEnds)
        if (actualRoom & gl.WALL_NORTH) == 0 and gone != gl.GONE_SOUTH and y > 0:
            self.__searchPathThroughMazeV2(x, y - 1, pace, gl.GONE_NORTH, deadEnds)
            
        if self.__checkDeadEnd(actualRoom):
            # the actual position a dead end
            deadEnd = DeadEnd(x, y, pace)
            deadEnds.append(deadEnd)
     
    """
        Check dead end
    """
    def __checkDeadEnd(self, actualRoom):
        noOfWalls = 0   # count the number of walls

        if (actualRoom & gl.WALL_NORTH) > 0:
            # to the north there is a wall
            noOfWalls = noOfWalls + 1
        if (actualRoom & gl.WALL_SOUTH) > 0:
            noOfWalls = noOfWalls + 1
        if (actualRoom & gl.WALL_WEST) > 0:
            noOfWalls = noOfWalls + 1
        if (actualRoom & gl.WALL_EAST) > 0:
            noOfWalls = noOfWalls + 1

        return noOfWalls == 3

    """
        Create an exit for the maze
        Entry function
    """
    def __selectBestWeightedEntrance(self, entrances):
        bestEntrance = Entrance()
        bestWeight = 0.0
        for entrance in entrances:
            weight = entrance.getWeightedMeasure()
            print(entrance.EntranceX, entrance.EntranceY, weight)
            if weight > bestWeight:
                bestEntrance = entrance
                bestWeight = weight
                
        print("Best entrance :", bestEntrance.EntranceFrom, bestEntrance.EntranceX, bestEntrance.EntranceY, bestWeight)
            
            

    """
        Create an exit for the maze
        Entry function
    """
    def __createExitForMaze(self):
        entrances = []
        deadEnds = []
        
        # Entry from North
        y = 0
        for x in range(0,gl.MAZE_SIZE_X):
            deadEnds = self.__findPathInMaze(x,y, gl.GONE_NORTH)
            entrance = Entrance(x, y, gl.GONE_NORTH, deadEnds)
            entrances.append(entrance)

        # Entry from South
        y = gl.MAZE_SIZE_Y - 1;
        for x in range(0,gl.MAZE_SIZE_X):
            deadEnds = self.__findPathInMaze(x,y, gl.GONE_SOUTH)
            entrance = Entrance(x, y, gl.GONE_SOUTH, deadEnds)
            entrances.append(entrance)
        
        # Entry from West
        x = 0;
        for y in range(0,gl.MAZE_SIZE_Y):
            deadEnds = self.__findPathInMaze(x,y, gl.GONE_WEST)
            entrance = Entrance(x, y, gl.GONE_NORTH, deadEnds)
            entrances.append(entrance)

        # Entry from South
        x = gl.MAZE_SIZE_X - 1;
        for y in range(0,gl.MAZE_SIZE_Y):
            deadEnds = self.__findPathInMaze(x,y, gl.GONE_SOUTH)
            entrance = Entrance(x, y, gl.GONE_NORTH, deadEnds)
            entrances.append(entrance)

        self.__selectBestWeightedEntrance(entrances)
        
    """
        Create a random maze
        private sub routine
    """
    def __createRandomMaze(self, chamberMinX, chamberMaxX, chamberMinY, chamberMaxY):        
        # check minimum size of chamber
        if (chamberMaxX - chamberMinX) < gl.MIN_MAZE_SIZE_X:
            return

        # check minimum size of chamber
        if (chamberMaxY - chamberMinY) < gl.MIN_MAZE_SIZE_Y:
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
                self.MazeArray[x][wallY] = self.MazeArray[x][wallY] + gl.WALL_SOUTH
                if wallY < gl.MAZE_SIZE_Y:
                    self.MazeArray[x][wallY+1] = self.MazeArray[x][wallY+1] + gl.WALL_NORTH

        # hole in the wall
        firstHole = randint(chamberMinY, wallY)
        secondHole = randint(wallY+1, chamberMaxY)

        logging.info("holes (%d, %d)", firstHole, secondHole)
     
        for y in range(chamberMinY,chamberMaxY+1):
            if (y <= wallY and y != firstHole) or (y > wallY and y != secondHole): 
                self.MazeArray[wallX][y] = self.MazeArray[wallX][y] | gl.WALL_EAST
                if wallX < gl.MAZE_SIZE_X:
                    self.MazeArray[wallX+1][y] = self.MazeArray[wallX+1][y] | gl.WALL_WEST

        print()

        self.__createRandomMaze(chamberMinX, wallX, chamberMinY, wallY)        # Quarter 0
        self.__createRandomMaze(wallX+1, chamberMaxX, chamberMinY, wallY)      # Quarter 1
        self.__createRandomMaze(wallX+1, chamberMaxX, wallY+1, chamberMaxY)    # Quarter 2
        self.__createRandomMaze(chamberMinX, wallX, wallY+1, chamberMaxY)      # Quarter 3

    """
        Draw random maze
    """
    def __drawMaze(self):
        for y in range(gl.MAZE_SIZE_Y):
            for x in range(gl.MAZE_SIZE_X): # 0..9
                sys.stdout.write("+")
                
                if (self.MazeArray[x][y] & gl.WALL_NORTH) > 0:
                    sys.stdout.write("-")
                else:
                    sys.stdout.write(" ")

            sys.stdout.write("+")
                    
            print()

            # 2nd row
            for x in range(gl.MAZE_SIZE_X):
                if (self.MazeArray[x][y] & gl.WALL_WEST) > 0:
                    sys.stdout.write("| ")
                else:
                    sys.stdout.write("  ")

            if (self.MazeArray[gl.MAZE_SIZE_X-1][y] | gl.WALL_EAST) > 0:
                sys.stdout.write("|")
       
            print()

        for x in range(gl.MAZE_SIZE_X): # 0..9
            sys.stdout.write("+")
            
            if (self.MazeArray[x][gl.MAZE_SIZE_Y-1] & gl.WALL_SOUTH) > 0:
                sys.stdout.write("-")
            else:
                sys.stdout.write(" ")

        sys.stdout.write("+")
        print()


    """
        Test creating persons
    """
    def test_createMaze(self):
        self.createRandomMaze()
        self.__drawMaze()
        self.__saveMaze()
        self.__loadMaze()
        self.__drawMaze()
        self.__findPathInMaze(0,0,0)
        self.__createExitForMaze()
    
if __name__ == '__main__':
    unittest.main()        
