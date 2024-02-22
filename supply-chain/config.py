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
 }


parameters = {
    'base': {
        'name':'Base parameter set.',
        'parameters': base
    },
}