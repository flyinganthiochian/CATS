from Network import *
from Lane import *
from Road import *
from Simulation import * 
from Test import *

class Cell:
    id=0

    def __init__(self,givenLane):
        Cell.id +=1
        self.id=Cell.id #id is given by the order of creation in the whole network
        self.lane=givenLane
    def createAllLaneCells(givenLane):
        #this method will take a Lane as an agruement and will create cells and add them into the Lane's cellList<>
        #this method is automatically called wheneever a Lane is Created
        for cellCounter in givenLane.road.numberOfCells:
            cell = Cell(givenLane)
            givenLane.cellList.append(cell)
