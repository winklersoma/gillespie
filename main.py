import matplotlib.pyplot as plt
import numpy as np
from simulator import simulator

# This file is supposed to contain 3 functions.
# The first one should be able to plot the trajectiories of the state variables of one simulation.
# The second one should be able to plot several trajectories of one (or more?) variable(s) on one plot.
# The third should plot the expected values of the state variables in the different time points
# by running several simulations and calculating the mean of these values in the corresponding points in time.

# initial state of the population
Susc = 100
Inf = 5
Rec = 0

# As the average time spent in disease equals 1 / gamma, the value below can be estimated
g = 1 / 7  # recovery rate

# Let us say that we estimate the reproduction number to be 3.
# Since beta equals gamma * reproduction number, our beta will be 3/7.
b = 3 / 7  # infection rate

end = 50
periods = 25


def plot_one_simulation(initial_states, beta, gamma, end_time, n_periods):
    result = simulator(initial_states=initial_states, beta=beta, gamma=gamma, end_time=end_time, n_periods=n_periods)
    x = np.linspace(start=0, stop=end, num=periods + 1)
    y = result[:, :]
    plt.plot(x, y)
    plt.legend(["Susceptible", "Infected", "Recovered"], loc="upper right")
    plt.show()
    return result


#  print(plot_one_simulation(initial_states=[Susc, Inf, Rec],
#                          beta=b, gamma=g, end_time=end, n_periods=periods))

def plot_n_simulations(initial_states, beta, gamma, end_time, n_periods, n_simulations, var_to_plot=1):
    y = np.zeros(shape=(n_simulations, periods + 1))  # nparray of size 26 x n_sim
    for i in range(n_simulations):
        result = simulator(initial_states=[Susc, Inf, Rec], beta=b, gamma=g, end_time=end, n_periods=periods)
        y[:][i] = result[:, 1]

    x = np.linspace(start=0, stop=end, num=periods + 1)
    for i in range(n_simulations):
        plt.plot(x, y[i])
    plt.show()


plot_n_simulations(initial_states=[Susc, Inf, Rec],
                   beta=b, gamma=g, end_time=end, n_periods=periods, n_simulations=5, var_to_plot=1)

"""
n = 5
y = np.zeros(shape=(n, periods+1))
for i in range(n):
    result = simulator(initial_states=[Susc, Inf, Rec], beta=b, gamma=g, end_time=end, n_periods=periods)
    y[i] = result[:, 0]

z = y.mean(axis=0)
print(z.shape)

x = np.linspace(start=0, stop=end, num=periods+1)
for i in range(n):
    plt.plot(x, z)
plt.legend(["Susceptible"], loc="upper right")
plt.show()
"""
