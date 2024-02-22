###############################################################################
# IMPORTS
###############################################################################

from agentpy import Model, Grid, AgentList
import math

from .firm import Firm

###############################################################################
# MODEL
###############################################################################

class SupplyChain(Model):

    def setup(self):

        # Create agents equal to the size of the grid.
        self.agents = AgentList(self, self.p['size'], Firm)

        # Create grid, add agents, fill completely.
        self.grid = Grid(self, shape=[int(math.sqrt(self.p['size']))]*2, torus=True, track_empty=True)
        self.grid.add_agents(self.agents, random=True, empty=True)

    def step(self):
        pass

    def end(self):
        pass