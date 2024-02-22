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
    'seed': 92,     # Seed for RNG.
    'steps': 1,     # Number of steps.
    'size': 9,      # Number of agents and ^2 grid size. Choose size with rational root.
    'prop': 0.50    # Probability of agents with status = 1 (alive).
 }

dense = {
    'prop': 0.90   # Probability of agents with status = 1 (alive).
 }

parameters = {
    'base': {
        'name':'Base parameter set.',
        'parameters': base
    },
    'dense': {
        'name': 'Highly dense initial condition.',
        'parameters': get_parameters(base, dense)
    }
}