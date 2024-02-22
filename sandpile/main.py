###############################################################################
# IMPORTS
###############################################################################

from config import parameters
from models.sandpile import Sandpile

###############################################################################
# RUN EXPERIMENT
###############################################################################

def main():

    # Extract experiment details
    print(f"Retrieving experiment details.")
    base_params = parameters['base']['parameters']

    # Initialize model with imported parameters.
    print(f"Initializing experiment: {base_params['steps']} Steps")
    model = Sandpile(base_params)

    # Run the model.
    print("Running model.")
    results = model.run()

    # Save model results.
    print("Experiment complete. Saving results.")
    results.save(exp_name='sandpile', path='data')

if __name__ == '__main__':
    main()