from Network import *
from Cell import *
from Road import *
from Simulation import * 
from Test import *


class Lane:
    id=0
    cellList =[] #all the cells of this lane will be stored in this List<>
    
    def __init__(self,givenRoad):
        Lane.id +=1 #lane id is given by the order of creation of lanes in whole network
        self.id=Lane.id
        givenRoad.laneList.append(self) #this lane is added to the road's laneList<>