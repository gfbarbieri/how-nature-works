import agentpy as ap
import math

class Sandpile(ap.Model):

    def setup(self):

        # Create agents (location for a pile).
        self.agents = ap.AgentList(self, self.p['size'])

        # Initialize avalanche size.
        self.num_pile_collapses = 0
        self.num_grains_moved = 0

        # Create grid (area) and place agents on them. Fill grid completely
        self.grid = ap.Grid(self, shape=[int(math.sqrt(self.p['size']))]*2, torus=True)
        self.grid.add_agents(self.agents, random=True, empty=True)

        # Agent properties: grains = 0; collapse = 0.
        self.agents.grains = 0
        self.agents.collapse = False

    def step(self):
        
        # Reset counters.
        self.num_pile_collapses = 0
        self.num_grains_moved = 0
        self.agents.collapse = False
        
        #######################################################################
        # DROP GRAIN
        #######################################################################
        
        # Randomly select an agent on a grid and increment their grain
        # pile by 1.
        self.agents.random(n=1).grains += 1

        #######################################################################
        # AVALANCHE
        #######################################################################

        # A collapse occurs when an agent's grain piles exceed grain limits.
        #
        # In the case of a collapse, the collapsing pile spills a single grain
        # onto a number of neighbors. This process contains until the grid does
        # not contain any agents exceeding grain limits.
        while any(self.agents.select(self.agents.grains > self.p['grain_limit'])):

            # Find the agents on the grid exceeding grain limits.
            agnts = self.agents.select(self.agents.grains > self.p['grain_limit'])

            # Record the size of the avalanche as the number of agents with a
            # gain pile larger than the grain limit. This count untils to
            # accumulate until the grid does not have any more agents with grain
            # piles above the limit. The resulting count is the size of the
            # avalanche: the total number of collapsing piles that resulted from
            # dropping a single grain onto the grid.
            # 
            # Another natural way to count the size of the avalanche is to count
            # the total number of grains that moved to different piles as a
            # result of the collapses. Since the number of grains that shift
            # piles as a result of the collapse is fixed, then the total number
            # of grains that move between piles is a factor of the total number
            # of piles that collapse. Therefore, there is no need to count both
            # the number of collapsing piles and the number of moving grains
            # since the latter is a constant factor of the former.
            # 
            # Lastly, if a grain pile collapses more than once during a string
            # of collapses, then it is counted more than once. For example, X's
            # pile collapses onto neighboring piles. Enough neighboring piles
            # collapse onto X's pile to cause X's pile to exceed grain limit
            # again and collapse onto neighboring piles.
            self.num_pile_collapses += len(agnts)

            # For each agent exceeding grain limits, select a neighbor and from their six
            # possible neighbors and add one grain to their piles.
            for agnt in agnts:
                agnt.collapse = True

                for neighbor in self.grid.neighbors(agnts).random(n=self.p['neighbors'], replace=False):
                    if agnt.grains > 0:
                        agnt.grains -= 1
                        neighbor.grains += 1
                        self.num_grain_moved += 1
                    
    def end(self):
        pass