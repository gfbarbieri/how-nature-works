def get_parameters(static, updates):
    """
    Combine base parameters with the parameter values for the experiment.

    Parameters
    ----------
    status (dict): The base parameters.
    updates (dict): The experiment parameters.

    Returns
    -------
    dict : A dictionary of parameters for the experiment.
    """

    exp_params = static.copy()
    exp_params.update(updates)

    return exp_params

base = {
    'seed': 92,       # Seed for RNG.
    'steps': 10,      # Number of steps.
    'size': 9,        # Number of agents and ^2 grid size. Choose size with rational root.
    'grain_limit': 4, # Limit connected with neighbors.
    'neighbors': 4    # Max number of neighbors is 6.
 }

parameters = {
    'base': {
        'name':'Base parameter set.',
        'parameters': base
    },
}