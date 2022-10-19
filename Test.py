from Simulation import*

class Test:


    def __init__(self):
        pass

    def printDefaultSimParameters(currentSim):
        print("\n***TEST-printDefaultSimParameters STARTS***")
        print("-------------------------------------")
        print("Default duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Default length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        print("-------------------------------------")
        print("***TEST-printDefaultSimParameters ENDS***\n")

    def printCurrentSimParameters(currentSim):
        print("\n***TEST-printCurrentSimParameters STARTS***")
        print("-------------------------------------")
        print("Duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        print("-------------------------------------")
        print("***TEST-printCurrentSimParameters ENDS***\n")
    def printCurrentSimStep(currentSim):
        print("\n***TEST-printCurrentSimStep STARTS***")
        print("-------------------------------------")
        print("Current Step = {step}".format(step=currentSim.currentStep))
        print("-------------------------------------")
        print("***TEST-printCurrentSimStep ENDS***\n")
    
    def printSimulationElapsedTime(currentSim):
        #this method gets the currentSim.elapsedTime property 
        #and prints the elapsed time in minutes and seconds
        print('Total elapsed time = : ', currentSim.elapsedTime[0], 'minutes',currentSim.elapsedTime[1], 'seconds')


    
    
    
    
    def printNetworkNodeInfo(currentSim):
        #this method will print number of nodes info and ID of each node
        print("\n***TEST-printNetworkNodeInfo STARTS***")
        print("-------------------------------------")
        print("Total number of Nodes in this network is = {node}".format(node=len(currentSim.network.nodeList)))
        for nodeID in currentSim.network.nodeList:
            print("Node ID= {id}".format(id=nodeID.id))

        print("-------------------------------------")
        print("***TEST-printNetworkNodeInfo ENDS***")
    
    def printNetworkRoadInfo(currentSim):
        #this method prints the IDs, names, lengths and Slope of the Roads
        print("\n***TEST-printNetworkRoadInfo STARTS***")
        print("-------------------------------------")
        print("Total number of Roads in this network is = {node}".format(node=len(currentSim.network.roadList)))
        for Road in currentSim.network.roadList:
            print("Road ID= {id} | Name= {name} | length = {length} | slope = {slope}".format(id=Road.id, name=Road.name, length=Road.length, slope=Road.slope))

        print("-------------------------------------")
        print("***TEST-printNetworkRoadInfo ENDS***")
