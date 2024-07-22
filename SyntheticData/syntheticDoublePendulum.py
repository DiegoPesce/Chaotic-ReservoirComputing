import sys
import os
sys.path.append(os.getcwd())
from Utils.DataGenerator import generate_data
from Utils.DataGenerator import double_pendulum

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], int(1e8))
y0 = [0.001*np.pi, 0.005*np.pi, 0.0, 0.0]

# Generate the data
t, data = generate_data(double_pendulum, t_span, y0, t_eval)

sampling = int(1e2)
# sample the data every ... points
t = t[::sampling]
data = data[::sampling]

# Save the data to CSV
df = pd.DataFrame(data, columns=['theta1','theta2','dtheta1','dtheta2'])
df['time'] = t
df.to_csv("Data/DoublePendulum/double_pendulum.csv")

# plot the data in a 3D plot
plt.figure()
plt.plot(data[:,0],data[:,1])
plt.show()
