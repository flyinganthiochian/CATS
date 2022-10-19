from Network import *
from Cell import *
from Lane import *
from Road import *
from Simulation import * 
from Test import *

class Node:
    id=0
    
    inRoadList=[]#all the roads which ends in this Node will be hold in this List<>
    outRoadList=[]#all the roads which starts in this Node will be hold in this List<>


    def __init__(self,givenNetwork,givenAbcissa,givenOrdinate,givenElevation=0,givenName="") -> None:
        Node.id +=1
        self.id=Node.id #id of the node is given by the order of creation
        self.abcissa = givenAbcissa #X coordinate of the Node in meters
        self.ordinate = givenOrdinate # Y coordinate of the Node in meters
        self.elevation = givenElevation #elevation above the Sea Level (experimental feature)
        self.name = givenName #set the user name as the Node name
        if self.name == "":
            self.name = str(Node.id) #if no name is given then  the node ID is set as the Node name
        givenNetwork.nodeList.append(self) #this node is added to the nodeList of the Network
    
    def createSiouxFallsNodes(network):
        #this method creates all the nodes of default sioux Falls network
        #Sioux-Falls network consists of 24 Nodes
        node1 = Node(network,0,0)
        node2 = Node(network,6000,0)
        node3 = Node(network,0,-2000)
        node4 = Node(network,2000,-2000)
        node5 = Node(network,4000,-2000)
        node6 = Node(network,6000,-2000)
        node7 = Node(network,8000,-4000)
        node8 = Node(network,6000,-4000)
        node9 = Node(network,4000,-4000)
        node10 = Node(network,4000,-6000)
        node11 = Node(network,2000,-6000)
        node12 = Node(network,0,-6000)
        node13 = Node(network,0,-14000)
        node14 = Node(network,2000,-10000)
        node15 = Node(network,4000,-10000)
        node16 = Node(network,6000,-6000)
        node17 = Node(network,6000,-8000)
        node18 = Node(network,8000,-6000)
        node19 = Node(network,6000,-10000)
        node20 = Node(network,6000,-14000)
        node21 = Node(network,4000,-14000)
        node22 = Node(network,4000,-12000)
        node23 = Node(network,2000,-12000)
        node24 = Node(network,2000,-14000)

        

        
