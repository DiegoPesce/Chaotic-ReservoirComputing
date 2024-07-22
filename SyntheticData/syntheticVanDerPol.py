import sys
import os
sys.path.append(os.getcwd())
from Utils.DataGenerator import generate_data
from Utils.DataGenerator import van_der_pol

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], int(1e8))
y0 = [0.1, -0.1]

# Generate the data
t, data = generate_data(van_der_pol, t_span, y0, t_eval)

sampling = int(1e4)
# sample the data every ... points
t = t[::sampling]
data = data[::sampling]

# Save the data to CSV
df = pd.DataFrame(data, columns=['x','dx'])
df['time'] = t
df.to_csv("Data/VanDerPol/vanderpol.csv")

# plot the data in a 3D plot
plt.figure()
plt.plot(data[:,0])
plt.show()
