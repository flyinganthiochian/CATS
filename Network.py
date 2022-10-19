from Node import *
from Cell import *
from Lane import *
from Road import *
from Simulation import * 
from Test import *

class Network:
    id=0
    nodeList =[] #all the nodes of this network will be stored in this list
    roadList=[] #all the roads of this network will be stored in this list

    def __init__(self,givenSimulation):
        Network.id +=1
        self.id=Network.id #id of the network is given by the creation order
        givenSimulation.network=self #network is set as the simulation's network
        self.simulation = givenSimulation
    

    def createSiouxFallsNetwork(currentSimulation):
        #this method creates default Sioux-Falls network
        siouxFallsNetwork = Network(currentSimulation)

        #below all the nodes of the Sioux-Falls network is created
        Node.createSiouxFallsNodes(siouxFallsNetwork)
        Road.createSiouxFallsRoads(siouxFallsNetwork)