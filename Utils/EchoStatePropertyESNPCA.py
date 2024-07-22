import sys
import os
sys.path.append(os.getcwd())

import matplotlib.pyplot as plt
import torch
from Reservoirs.ESNPCA import ESNPCA
from Utils.DataLoader import loadData

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

variables=['Component1','Component2','Component3','Component4']

results = []
n_iters=5

(input_fit, target_fit), _ = loadData("R3BP")
io_size = input_fit.size(1)
rs=1024

model = ESNPCA(io_size, io_size, rs, warmup=30, spectral_radius=0.9, sparsity=0.1, leaking_rate=1, seed=None).to(device)
for i in range(n_iters):
    result = model.thermalize(input_fit, h0=torch.randn(rs))
    results.append(result)

plt.figure(figsize=(15, 30))
plt.title("Hidden states components")
plt.axis("off")
for var, varname in enumerate(variables):
    plt.subplot(len(variables), 1, var+1)
    for result in results:
        plt.plot(result[:, var].cpu().detach().numpy())
    plt.grid()
plt.show()
