import random
from datetime import datetime

class Environment:
    random.seed(datetime.now())


    def __init__(self):
        self.things = [0,0]
        self.agents = ["",""]
        self.agentPosition = 0

    def randomizeObj(self):
        for x in range(2):
            event = random.random()
            if (0.0<event<0.5):
                self.things[x] = 1
            else:
                self.things[x] = 0   

    def printEnv(self):
        print("\n", self.things)
        print(self.agents)
        print("agent is at:", self.agentPosition, "\n")

    def addAgent(self, agent):
        event1 = random.random()
        if(0.0<event1<0.5):
            self.agents[0] = agent.name
        else:
            self.agents[1] = agent.name
            self.agentPosition = 1
        
        
class Agent:

    def __init__(self, name, env):
        self.name = name
        self.alive = True
        self.env = env

    def moveLeft(self):
        if self.env.agentPosition == 1:
            print("Action: move left")
            self.env.agents[0] = self.env.agents[1]
            self.env.agents[1] = ""
            self.env.agentPosition -=1
        else:
            print("You cannot do that!")

    def moveRight(self):
        if self.env.agentPosition == 0:
            print("Action: move right")
            self.env.agents[1] = self.env.agents[0]
            self.env.agents[0] = ""
            self.env.agentPosition +=1
        else:
            print("You cannot do that!")

    def suck(self):
        if self.env.agentPosition == 0:
            if self.env.things[0] == 1:
                self.env.things[0] = 0
                print("sucked at pos 0!")
            else:
                print("already clean!")
        else:
            if self.env.things[1] == 1:
                self.env.things[1] = 0
                print("sucked at pos 1!")
            else:
                print("already clean!")


    
#-----------------------------------------------------------------

def main():
    #initialize environment
    env1 = Environment()
    env1.randomizeObj()
    #initialize agent
    tonton = Agent("tonton", env1)
    env1.addAgent(tonton)
    env1.printEnv()

    #I used the code below just for testing it lol
    """
    tonton.moveLeft()
    tonton.suck()
    env1.printEnv()
    tonton.moveRight()
    tonton.suck()
    env1.printEnv()
    """

    #implementation of the different types of agents! (kulang pa to)
    #simpleReflexAgent(tonton,env1)
    #modelBasedReflexAgent(tonton,env1)
    goalBasedAgent(tonton,env1)

#-----------------------------------------------------------------

def simpleReflexAgent(agent,environment):
    #These agents select actions on the basis of the current 
    #percept, ignoring the rest of the percept history.
    print("\nSimple Reflex Agent!\n")
    
    for x in range(10):
        
        if environment.things[environment.agentPosition] == 1:
            agent.suck()
        else:
            if environment.agentPosition == 0:
                agent.moveRight()
            else:
                agent.moveLeft()

def modelBasedReflexAgent(agent,environment):
    print("\n Model-Based Reflex Agent!\n")

    model = [None,None]
    for x in range(100):
        model[environment.agentPosition] = environment.things[environment.agentPosition]
        if environment.things[environment.agentPosition] == 1:
            agent.suck()
        else:
            if environment.agentPosition == 0:
                agent.moveRight()
            else:
                agent.moveLeft()
        if model == [0,0]:
            break

def goalBasedAgent(agent, environment):
    print("\n Goal-Based Reflex Agent!\n")

    goal = [0,0]

    for x in range(100):
        if environment.things == goal:
            print("goal achieved!")
            break
        
        if environment.things[environment.agentPosition] == 1:
            agent.suck()
        else:
            if environment.agentPosition == 0:
                agent.moveRight()
            else:
                agent.moveLeft()


if __name__ == "__main__":
    main()