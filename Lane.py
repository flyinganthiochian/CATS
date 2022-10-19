from Cell import Cell
from Simulation import*
from Network import*
from Node import*
from Road import*

from Cell import*
from Test import*


class Lane:
    id=0
    

    def __init__(self,givenRoad):
        Lane.id +=1
        self.id = Lane.id
        self.cellList = []
        self.road=givenRoad


    def createRoadLanes(givenRoad):

        for counter in range(givenRoad.numberOfLanes):
            
            givenRoad.laneList.append(Lane(givenRoad))
            Cell.createLaneCells(givenRoad.laneList[counter])
            

