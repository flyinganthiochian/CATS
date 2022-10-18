

class Simulation:
    currentStep=0
    print("=============================================================")
    print("Welcome to [C]ellular [A]utomata [T]raffic [S]imulation CATS")
    print("=============================================================")

    def __init__(self,givenSimDuration=100, givenSimLength=5):
        self.simDuration=givenSimDuration
        self.cellLength=givenSimLength