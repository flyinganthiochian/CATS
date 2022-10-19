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
        givenLane.cellList.append(self)
        self.lane=givenLane
    
    
