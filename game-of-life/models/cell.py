###############################################################################
# IMPORTS
###############################################################################

from agentpy import Agent

###############################################################################
# CELL AGENT
###############################################################################

class Cell(Agent):

    ###########################################################################
    # INITIALIZATION
    ###########################################################################

    def setup(self):
        """
        Initializes the generic agent's attribute `status`.
        """

        # Set status attribute. Probability, or density of status is user-defined.
        self.status = self.model.nprandom.choice(0, 1, p=[self.model.p['prop'], (1-self.model.p['prop'])])