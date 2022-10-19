import datetime
from Simulation import*
from Network import*
from Node import*
from Road import*
from Lane import*
from Cell import*
from Test import*

def runSimulation(givenSimulation):
    givenSimulation.startTime=datetime.datetime.now() #simulation start time is recorded
    givenSimulation.makeInitialTests() #initial sim parameters are printed
    givenSimulation.makeNetworkTests() #all the network Test will be done
    while givenSimulation.currentStep < givenSimulation.simDuration: #iteration of simulation until the end
        givenSimulation.updateSimulationStep()
    givenSimulation.endTime=datetime.datetime.now() #simulation end time is recorded
    givenSimulation.calculateSimulationElapsedTime() #simulation elapsed time is calculated
    givenSimulation.makeEndTests() #simulation tests are performed once the simulation is finished
    
    

currentSim=Simulation()
Network.createSiouxFallsNetwork(currentSim)

runSimulation(currentSim)



