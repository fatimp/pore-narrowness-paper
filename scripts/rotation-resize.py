#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

rot = np.load('rotate.npy')
res = np.load('resize.npy')

def err(a):
    return (np.max(a) - np.min(a)) / np.mean(a)

print(err(rot[:,1]))
print(err(res[:,1]))

res[:,0] = res[:,0] / 1000

fig = plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 17)
#plt.ticklabel_format(axis = "y", scilimits = (0, 0), useMathText = True)
#plt.ticklabel_format(axis = "x", scilimits = (0, 0), useMathText = True)
ax1 = fig.gca()
ax2 = ax1.twiny()
ax1.scatter(rot[:,0], rot[:,1], c = 'r', marker = 'x')
ax2.scatter(res[:,0], res[:,1], c = 'b')
ax1.set_ylabel('Awesomeness')
ax1.set_xlabel('Rotation angle, degrees')
ax2.set_xlabel('Scale factor')
plt.savefig('rotation-resize.png', bbox_inches = 'tight')
