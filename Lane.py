
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
        self.road=givenRoad
        
        

    def createAllRoadLanes(givenRoad):
        #this method will take the Road as an argument and will create all the Lanes of this road
        #then it will add lanes to the Road's laneList<>
        #this method will be automatically called when the road is created
        for laneCounter in givenRoad.numberOfLanes:
            lane = Lane(givenRoad)
            
            givenRoad.laneList.append(lane)

    

    
    