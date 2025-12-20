import numpy as np

def simulate_compensation(l, m, s, r, M, A, nrep=10000, seed=None):
    """
    Monte Carlo simulation of monthly compensation requirements.

    Parameters
    ----------
    l : float   # Poisson rate (claims per month)
    m : float   # mean claim amount
    s : float   # std of claim amount
    r : float   # reimbursement fraction below M
    M : float   # claim threshold
    A : float   # available reserve
    nrep : int  # number of Monte Carlo replications
    seed : int or None

    Returns
    -------
    exp_comp : float  # estimated expected total compensation
    prob_exceed : float  # estimated P(total > A)
    """

    rng = np.random.default_rng(seed)
    totals = np.zeros(nrep)

    for i in range(nrep):
        n_claims = rng.poisson(l)
        if n_claims > 0:
            claims = rng.normal(m, s, n_claims)
            comp = np.where(claims <= M, r * claims, r * M + (claims - M))
            totals[i] = comp.sum()
        else:
            totals[i] = 0.0

    exp_comp = totals.mean()
    prob_exceed = np.mean(totals > A)
    return exp_comp, prob_exceed

# Example usage:
if __name__ == "__main__":
    l, m, s, r, M, A = 10, 1000, 300, 0.8, 1200, 12000
    mean_cost, p_exceed = simulate_compensation(l, m, s, r, M, A)
    print(f"Estimated Total Cost = {mean_cost:.2f} Estimated Probability of Default = {p_exceed:.4f}")
    #
    alevs=np.linspace(5000,30000,100)
    results = [simulate_compensation(l, m, s, r, M, Alev) for Alev in alevs]
    import matplotlib.pyplot as plt 
    plt.plot(alevs, [res[1] for res in results])
    plt.xlabel('Available Reserve A')
    plt.ylabel('Probability of Exceedance')
    plt.title('Probability of Total Compensation Exceeding Available Reserve')
    plt.grid()
    plt.show()
    

