import matplotlib
import numpy as np

# np.random.seed(42)

# Model:
# S' = -ß(SI)/N
# I' = ß(SI)/N + γI
# R' = γI

# This function performs one simulation of the SIR model with given parameters,
# starting at time zero and runs until either a specified end time is reached or
# the number of infected hosts becomes zero.


# STEP 1: Initialization: time, states, halting conditions

# initial state of the population
Susc = 100
Inf = 5
Rec = 0

# As the average time spent in disease equals 1 / gamma, the value below can be estimated
g = 1 / 7  # recovery rate

# Let us say that we estimate the reproduction number to be 3.
# Since beta equals gamma * reproduction number, our beta will be 3/7.
b = 3 / 7  # infection rate


def simulator(initial_states: list, beta: float, gamma: float, end_time: int, n_periods) -> np.ndarray:
    time = 0
    states = np.array(initial_states)
    pop = np.sum(states)
    result = np.zeros(shape=(n_periods + 1, 3))
    t = end_time / periods
    i = 1
    for j in range(0, 3):
        result[0][j] = states[j]

    # The model stops if the number of the infected reaches zero or the time reaches the prescribed end time.
    while time < end_time and states[1] > 0:

        # STEP 2: Calculate propensity functions (event probabilities) a_1, a_2 for current(!) state

        # infection_propensity = infection rate * infected people * probability that they will meet a susceptible person
        a_inf = (1 / pop) * beta * states[0] * states[1]
        # recovery propensity = recovery rate * infected people
        a_rec = gamma * states[1]
        a = a_inf + a_rec

        # STEP 3: Determine when does the next event happen
        r_1 = np.random.rand()
        tau = (1 / a) * np.log(1 / r_1)

        # STEP 4: Determine which event happens
        r_2 = np.random.rand() * a
        event_index = 0
        if r_2 > a_inf:
            event_index = 1

        # STEP 5: Update time and state variables
        time = time + tau
        if event_index == 0:
            states[0] -= 1
            states[1] += 1
        else:
            states[1] -= 1
            states[2] += 1

        # Update the states array
        #        print('time is: ',time, 't:', t, 'i: ',i)
        if time < t:  # if the condition is not satisfied, it means that the iteration is in the next period already.
            for j in range(0, 3):
                result[i][j] = states[j]
        else:
            for j in range(0, 3):
                result[i][j] = states[j]
            t += end_time / n_periods  # change for next period
            i += 1

    # transform all zero-rows at the end to the final state vector
    for row in result:
        if (row == 0).all():
            row[:] = states[:]
    print('the time the model ran was: ', time)
    return result


# maximum time until one simulation can run
end = 50
# number of periods
periods = 25
print(simulator(initial_states=[Susc, Inf, Rec], beta=b, gamma=g, end_time=end, n_periods=periods))
