###############################################################################
# IMPORTS
###############################################################################

from agentpy import Model, Grid, AgentList
import math

from .cell import Cell

###############################################################################
# MODEL
###############################################################################

class GameOfLife(Model):

    def setup(self):

        # Create agents equal to the size of the grid.
        self.agents = AgentList(self, self.p['size'], Cell)

        # Create grid, add agents, fill completely.
        self.grid = Grid(self, shape=[int(math.sqrt(self.p['size']))]*2, torus=True, track_empty=True)
        self.grid.add_agents(self.agents, random=True, empty=True)

    def step(self):
        
        #######################################################################
        # SIMULTANEOUS ACTIVATION
        #######################################################################
        
        # Introduction:
        # We need to implement a simultaneous activation scheme as AgentPy does
        # not have one. This suggests that AgentPy is not hte appropriate library
        # for this modeling task. Naturally, we could switch to Mesa to maintain
        # an ABM design. In fact, this model does not require an ABM design at
        # all since it's a cellular automaton model. Python core libraries would
        # suffice. Regardless, this version will continue to use AgentPy and implement
        # custom simultaneous activation.
        # 
        # Simultaneous activation: The goal is to update all agents at the time
        # time becased on the state of the model. This differs from random
        # activation in that we do not update each agent one-by-one, where
        # changes accumulate as the model moves through an agent queue. Instead
        # the state of the model will be deteremined and all agents will act
        # at the same time with the same information.
        #
        # Algorithm:
        # 1. Get a full list of the agents on the grid. Since the status of the
        # agent's are fixed, it does not matter how the list is sorted. However,
        # if you want to be sure of the order, one method would be to sort the
        # resulting list such that the first elemlent is the top left agent of
        # the grid, moving from left to right and top to bottom, and last element
        # of the list is the most bottom right agent on the grid.
        # 2. For each agent, use the status of its 8 neighbors to determine
        # what the status of the agent should be in the following step of the
        # model. Store the status in a list.
        # 3. Using hte same list from (1), update the status of the agents using
        # the list from (2), effectively updating the status of all agents
        # simultaneously. This will work as expected because both lists have
        # the agents at the same list indices.

        #######################################################################
        # BIRTH AND DEATH
        #######################################################################
        
        # 1. Get a copy of all the agents on the grid.
        agents = self.agents.copy()
        print(f"Starting status of all agents on the grid:")
        print(self.agents.status)

        # 2. For each agent, find it's neighbors and use the rules of the Game
        # of Life to generate a new status for the agent.
        status_updates = []

        for agent in agents:
            print(f"Starting agent {agent.id}, status: {agent.status}")
            
            neighbors = self.grid.neighbors(agent)
            
            new_status = self.update_status(agent, neighbors)
            print(f"Ending agent {agent.id}, status: {new_status}")

            status_updates.append(new_status)

        # 3. Apply the list to the agents.
        self.agents.status = AttrIter(status_updates)
        print(f"Ending status of all agents on the grid:")
        print(self.agents.status)

    def end(self):
        pass

    def update_status(self, agent, neighbors):
        """
        Updates the status of the activated agent based on the status
        of its neighbors.

        List of the rules of the game here.
        """

        nss = sum(list(neighbors.status))

        print(f"Agent {agent.id}'s live neighbors: {nss}")

        # Birth.
        if agent.status == 0 and nss == 3:
            status = 1
        # Death by underpopulation.
        elif agent.status == 1 and nss <= 1:
            status = 0
        # Death by overpopulation.
        elif agent.status == 1 and nss > 3:
            status = 0
        # Continue at current state (dead or alive).
        else:
            status = agent.status
        
        return status