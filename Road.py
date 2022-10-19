import math
from Network import *
from Cell import *
from Lane import *
from Simulation import * 
from Test import *

class Road:
    id=0 
    laneList = [] #all the lanes will be stored in this List<>
    

    def __init__(self, givenNetwork,givenStartingNode,givenEndingNode,givenNumberOfLanes=1, givenName="",givenLength=0,givenElevation=0):
        Road.id +=1
        self.id=Road.id #id of the Road is given by the order of creation
        self.startingNode=givenStartingNode #road's starting node is set
        self.endingNode=givenEndingNode #road's ending node is set
        self.numberOfLanes=givenNumberOfLanes #number of lanes is set
        
        defaultLength=self.calculateDefaultRoadLength()
        #below in the inside if case it checked whether the given Length is
        #less than the calculated default length
        #given length CAN NOT be less than the shortest distance between nodes
        #in this case length of the road is equal to the line distance between nodes
        #but given length can be bigger than the line distance
        #in this case road length is equal to the user defined length
        if givenLength < defaultLength:
            self.length = defaultLength
        else:
            self.length=givenLength

        self.slope=self.calculateDefaultRoadSlope() #road's slope is set (+ values for incline, - values for decline as percentage)

        #here we check if the user is given a specific Name for the Road
        #if Not Road will be named with the IDs of the starting and ending Nodes
        #letter F than Starting Node ID, letter T and than ending Node ID
        #for example if the Road is starting from node ID 1 and end at the Node ID 2
        #the name of the Road Will be F1T2...
        if givenName == "":
            self.name="F"+str(givenStartingNode.id)+"T"+str(givenEndingNode.id)
        else:
            self.name=givenName
                     
        self.network=givenNetwork
        self.setNumberOfRoadCells()
        givenNetwork.roadList.append(self)
    
    def setNumberOfRoadCells(self):
        #this method takes road lengths in meters and sets the number of Cell property of Road
        self.numberOfCells=round(self.length/self.network.simulation.cellLength)
    def calculateDefaultRoadLength(givenRoad):
        #this method calculates the Road's length by using the Node's abcissa and ordinate
        #and sets the value as Road's length
        #!!This method should be called after the Road's starting and ending Node's are created
        #lenth between two nodes is = sqrt((x1-x2)**2+(y1-y2)**)
        
        length=math.sqrt((givenRoad.startingNode.abcissa-givenRoad.endingNode.abcissa)**2 + (givenRoad.startingNode.ordinate-givenRoad.endingNode.ordinate)**2)
        length = round(length)
        return length

    def calculateDefaultRoadSlope(givenRoad):
        #this method calculates the slope of the given road by using the elevation of starting and ending Nodes
        # formula -> slope = ((elevation2 -elevation1)*100/length)
        #it returns the slope in percantage
        #IMPORTANT!! This Method can be called only after the road length is SET

        
        slope = ((givenRoad.startingNode.elevation-givenRoad.endingNode.elevation)*100)/givenRoad.length
        return slope

    
    

    
            

    def createSiouxFallsRoads(network):
        #this method creates all the roads of the default Sioux Falls Network
        #Sioux falls Network consists of 76 roads

        #creating roads starting from Node 1
        road12=Road(network,network.nodeList[0],network.nodeList[1],3)
        road21=Road(network,network.nodeList[1],network.nodeList[0],3)

        road13=Road(network,network.nodeList[0],network.nodeList[2],3)
        road31=Road(network,network.nodeList[2],network.nodeList[0],3)

        road26=Road(network,network.nodeList[1],network.nodeList[5],3)
        road62=Road(network,network.nodeList[5],network.nodeList[1],3)

        road34=Road(network,network.nodeList[2],network.nodeList[3],3)
        road43=Road(network,network.nodeList[3],network.nodeList[2],3)

        road312=Road(network,network.nodeList[2],network.nodeList[11],3)
        road122=Road(network,network.nodeList[11],network.nodeList[2],3)

        road45=Road(network,network.nodeList[3],network.nodeList[4],3)
        road54=Road(network,network.nodeList[4],network.nodeList[3],3)

        road411=Road(network,network.nodeList[3],network.nodeList[10],3)
        road114=Road(network,network.nodeList[10],network.nodeList[3],3)

        road56=Road(network,network.nodeList[4],network.nodeList[5],3)
        road65=Road(network,network.nodeList[5],network.nodeList[4],3)

        road59=Road(network,network.nodeList[4],network.nodeList[8],2)
        road95=Road(network,network.nodeList[8],network.nodeList[4],2)

        road68=Road(network,network.nodeList[5],network.nodeList[7],2)
        road86=Road(network,network.nodeList[7],network.nodeList[5],2)

        road78=Road(network,network.nodeList[6],network.nodeList[7],2)
        road87=Road(network,network.nodeList[7],network.nodeList[6],2)

        road718=Road(network,network.nodeList[6],network.nodeList[17],2)
        road187=Road(network,network.nodeList[17],network.nodeList[6],2)

        road89=Road(network,network.nodeList[7],network.nodeList[8],2)
        road98=Road(network,network.nodeList[8],network.nodeList[7],2)

        road816=Road(network,network.nodeList[7],network.nodeList[15],2)
        road168=Road(network,network.nodeList[15],network.nodeList[7],2)

        road910=Road(network,network.nodeList[8],network.nodeList[9],2)
        road109=Road(network,network.nodeList[9],network.nodeList[8],2)

        road1011=Road(network,network.nodeList[9],network.nodeList[10],2)
        road1110=Road(network,network.nodeList[10],network.nodeList[9],2)

        road1015=Road(network,network.nodeList[9],network.nodeList[14],2)
        road1510=Road(network,network.nodeList[14],network.nodeList[9],2)

        road1016=Road(network,network.nodeList[9],network.nodeList[15],2)
        road1610=Road(network,network.nodeList[15],network.nodeList[9],2)

        road1017=Road(network,network.nodeList[9],network.nodeList[16],2)
        road1710=Road(network,network.nodeList[16],network.nodeList[9],2)

        road1112=Road(network,network.nodeList[10],network.nodeList[11],2)
        road1211=Road(network,network.nodeList[11],network.nodeList[10],2)

        road1114=Road(network,network.nodeList[10],network.nodeList[13],2)
        road1411=Road(network,network.nodeList[13],network.nodeList[10],2)

        road1213=Road(network,network.nodeList[11],network.nodeList[12],2)
        road1312=Road(network,network.nodeList[12],network.nodeList[11],2)

        road1324=Road(network,network.nodeList[12],network.nodeList[23],2)
        road2413=Road(network,network.nodeList[23],network.nodeList[12],2)

        road1415=Road(network,network.nodeList[13],network.nodeList[14],2)
        road1514=Road(network,network.nodeList[14],network.nodeList[13],2)

        road1423=Road(network,network.nodeList[13],network.nodeList[22],2)
        road2314=Road(network,network.nodeList[22],network.nodeList[13],2)

        road1519=Road(network,network.nodeList[14],network.nodeList[18],2)
        road1915=Road(network,network.nodeList[18],network.nodeList[14],2)

        road1522=Road(network,network.nodeList[14],network.nodeList[21],2)
        road2215=Road(network,network.nodeList[21],network.nodeList[14],2)

        road1617=Road(network,network.nodeList[15],network.nodeList[16],2)
        road1716=Road(network,network.nodeList[16],network.nodeList[15],2)

        road1618=Road(network,network.nodeList[15],network.nodeList[17],2)
        road1816=Road(network,network.nodeList[17],network.nodeList[15],2)

        road1719=Road(network,network.nodeList[16],network.nodeList[18],2)
        road1917=Road(network,network.nodeList[18],network.nodeList[16],2)

        road1820=Road(network,network.nodeList[17],network.nodeList[19],2)
        road2018=Road(network,network.nodeList[19],network.nodeList[17],2)

        road1920=Road(network,network.nodeList[18],network.nodeList[19],2)
        road2019=Road(network,network.nodeList[19],network.nodeList[18],2)

        road2021=Road(network,network.nodeList[19],network.nodeList[20],2)
        road2120=Road(network,network.nodeList[20],network.nodeList[19],2)

        road2022=Road(network,network.nodeList[19],network.nodeList[21],2)
        road2220=Road(network,network.nodeList[21],network.nodeList[19],2)

        road2122=Road(network,network.nodeList[20],network.nodeList[21],2)
        road2221=Road(network,network.nodeList[21],network.nodeList[20],2)

        road2124=Road(network,network.nodeList[20],network.nodeList[23],2)
        road2421=Road(network,network.nodeList[23],network.nodeList[20],2)

        road2223=Road(network,network.nodeList[21],network.nodeList[22],2)
        road2322=Road(network,network.nodeList[22],network.nodeList[21],2)

        road2324=Road(network,network.nodeList[22],network.nodeList[23],2)
        road2423=Road(network,network.nodeList[23],network.nodeList[22],2)