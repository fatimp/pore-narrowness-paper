#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

with sqlite3.connect('glyphs.db') as db:
    data = pd.read_sql_query('select * from pores where lfer > 0.9', db)

normal = data.query('name == "normal/"')
thin = data.query('name == "thin/"')
mnist = data.query('name == "mnist/"')
mostlyconvex = data.query('name == "mostlyconvex/"')

fig = plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 17)
ax = fig.add_subplot(projection = '3d')
ax.view_init(elev = 18, azim = -40, roll = 0)
ax.scatter(normal['convexity'], normal['elongation'], normal['sphericity'], marker = '.')
ax.scatter(thin['convexity'], thin['elongation'], thin['sphericity'], marker = 'x')
ax.scatter(mnist['convexity'], mnist['elongation'], mnist['sphericity'], marker = '^')
ax.scatter(mostlyconvex['convexity'], mostlyconvex['elongation'], mostlyconvex['sphericity'], marker = '+')
ax.set_xlabel('\nConvexity', linespacing = 2)
ax.set_ylabel('\nElongation', linespacing = 2)
ax.set_zlabel('Roundness')
ax.legend(['Normal', 'Thin', 'MNIST', 'Mostlyconvex'], markerscale = 2.5)
plt.savefig('cer.png', bbox_inches = 'tight', pad_inches = 0.4)
