from Simulation import*
from Network import*
from Node import*
from Road import*

from Cell import*
from Test import*


class Lane:
    id=0
    cellList = []

    def __init__(self,givenRoad):
        Lane.id +=1
        self.id = Lane.id
        givenRoad.laneList.append(self)
        self.road=givenRoad


    def createRoadLanes(givenRoad):

        for counter in givenRoad.numberOfLanes:
            createdlane = Lane(givenRoad)
            for cellCounter in givenRoad.numberOfCells:
                createdCell = Cell(createdlane)

