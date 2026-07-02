import timeit
import statistics


def benchmark(func, *args, repeats=10, number=1000):
    """
    Benchmark a function.

    Parameters
    ----------
    func : callable
        Function to benchmark.
    *args :
        Arguments passed to func.
    repeats : int
        Number of independent timing experiments.
    number : int
        Number of function calls in each experiment.

    Returns
    -------
    dict
        Timing statistics in seconds.
    """

    timer = timeit.Timer(lambda: func(*args))
    times = timer.repeat(repeat=repeats, number=number)

    # Convert to time per call
    times = [t / number for t in times]

    return {
        "min": min(times),
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "stdev": statistics.stdev(times),
    }


# -----------------------------------------------------
# Example
# -----------------------------------------------------

def test_function(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


results = benchmark(test_function, 10000, repeats=20, number=500)

print("Average time : {:.6e} s".format(results["mean"]))
print("Median time  : {:.6e} s".format(results["median"]))
print("Minimum time : {:.6e} s".format(results["min"]))
print("Std. dev.    : {:.6e} s".format(results["stdev"]))