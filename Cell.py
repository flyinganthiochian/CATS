from Simulation import*
from Network import*
from Node import*
from Road import*
from Lane import*
from Test import*

class Cell:
    id=0

    def __init__(self,givenLane):
        Cell.id +=1
        self.id = Cell.id
        
        self.lane=givenLane
    
    def createLaneCells(givenLane):
        for cellCounter in range(givenLane.road.numberOfCells):
            #print("Number of Cells = " + str(givenLane.road.numberOfCells))
            givenLane.cellList.append(Cell(givenLane))
    
    
