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
        givenLane.cellList.append(self) #cell is added to the Lane's cellList<>
