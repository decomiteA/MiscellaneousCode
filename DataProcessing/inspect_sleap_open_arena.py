import os
import h5py
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# PUT THE PATH TO YOUR H5 file here
input_path_file = PATH_TO_H5
with h5py.File(input_path_file,'r') as f:
    for key in f.keys():
        tmp_data = f[key]
        print(tmp_data.shape, type(tmp_data))
    occupancy_matrix = np.squeeze(f['tracks'][:])
    point_scores = np.squeeze(f['point_scores'][:])

# Your data should be in occupancy_matrix

fig, axs = plt.subplots(1,1,figsize=(3,3))
axs.spines[['top','right']].set_visible(False)
for ii in range(occupancy_matrix.shape[1]):
    axs.plot(occupancy_matrix[0,ii,:], occupancy_matrix[1,ii,:],lw=1)
axs.set_xlabel('x-position'), axs.set_ylabel('y-position')
plt.tight_layout()

fig, axs = plt.subplots(1,1,figsize=(3,3))
axs.spines[['top','right']].set_visible(False)
for ii in range(occupancy_matrix.shape[1]):
    axs.plot(occupancy_matrix[0,ii,:],lw=1)
axs.set_ylabel('x-position'), axs.set_xlabel('time')
plt.tight_layout()

fig, axs = plt.subplots(1,1,figsize=(3,3))
axs.spines[['top','right']].set_visible(False)
for ii in range(occupancy_matrix.shape[1]):
    axs.plot(occupancy_matrix[1,ii,:],lw=1)
axs.set_ylabel('y-position'), axs.set_xlabel('time')
plt.tight_layout()
plt.show()
