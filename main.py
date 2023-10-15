import matplotlib.pyplot as plt
import numpy as np
from simulator import simulator


Susc = 100
Inf = 5
Rec = 0
g = 1 / 7  # recovery rate
b = 3 / 7  # infection rate
end = 50
periods = 25
n = 1
for i in range(n):
    result = simulator(initial_states=[Susc, Inf, Rec], beta=b, gamma=g, end_time=end, n_periods=periods)


x = np.linspace(start=0, stop=end, num=periods+1)
y = result[:, 0]

plt.plot(x, y)
plt.show()
