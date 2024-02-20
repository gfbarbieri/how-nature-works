###############################################################################
# IMPORTS
###############################################################################

from config.base_config import base_params
from models.sandpile import Sandpile

###############################################################################
# RUN EXPERIMENT
###############################################################################

def main():

    print(f"Retrieving Experiment Details.")
    parameters = base_params

    print(f"Starting Experiment: {parameters['steps']} Steps")
    model = Sandpile(parameters)
    results = model.run()

    print(f"Experiment Complete")
    results.save(exp_name='sandpile_base', path='data')

if __name__ == '__main__':
    main()