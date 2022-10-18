from Simulation import*

class Test:


    def __init__(self):
        pass

    def printDefaultSimParameters(currentSim):
        print("\n***TEST-writeDefaultSimParameters STARTS***")
        print("-------------------------------------")
        print("Default duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Default length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        print("-------------------------------------")
        print("***TEST-writeDefaultSimParameters ENDS***\n")

    def printCurrentSimParameters(currentSim):
        print("\n***TEST-writeCurrentSimParameters STARTS***")
        print("-------------------------------------")
        print("Duration of the current sim = {duration} steps".format(duration=currentSim.simDuration))
        print("Length of each cell in the current sim = {length} meters".format(length=currentSim.cellLength))
        print("-------------------------------------")
        print("***TEST-writeCurrentSimParameters ENDS***\n")
    def printCurrentSimStep(currentSim):
        print("\n***TEST-writeCurrentSimStep STARTS***")
        print("-------------------------------------")
        print("Current Step = {step}".format(step=currentSim.currentStep))
        print("-------------------------------------")
        print("***TEST-writeCurrentSimStep ENDS***\n")
    
    def printSimulationElapsedTime(currentSim):
        #this method gets the currentSim.elapsedTime property 
        #and prints the elapsed time in minutes and seconds
        print('Total difference in minutes: ', currentSim.elapsedTime[0], 'minutes',currentSim.elapsedTime[1], 'seconds')
