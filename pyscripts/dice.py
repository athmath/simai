import numpy as np

def prob_sum_dice_exceeds(k, a, n=100_000, seed=None):
    """
    Monte Carlo estimate of P(sum of k fair dice > a)

    Parameters
    ----------
    k : int        # number of dice
    a : int/float  # threshold
    n : int        # number of Monte Carlo replications
    seed : int or None

    Returns
    -------
    p_est : float  # estimated probability
    """

    rng = np.random.default_rng(seed)
    rolls = rng.integers(1, 7, size=(n, k))  # each die 1–6
    sums = rolls.sum(axis=1)
    p_est = np.mean(sums > a)
    return p_est

# Example:
k, a, n = 18, 74, 10000
print(prob_sum_dice_exceeds(k, a))
