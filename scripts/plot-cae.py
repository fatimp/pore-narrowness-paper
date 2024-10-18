#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

with sqlite3.connect('glyphs.db') as db:
    general = pd.read_sql_query('select * from pores where lfer > 0.9', db)

shit = pd.read_csv('score.csv')
data = general.merge(shit, on = 'label', how = 'inner', validate = "1:1")

normal = data.query('name == "normal/"')
thin = data.query('name == "thin/"')
mnist = data.query('name == "mnist/"')
mostlyconvex = data.query('name == "mostlyconvex/"')

fig = plt.figure(figsize = (10, 9), dpi = 300)
plt.rc('font', size = 14)
ax = fig.add_subplot(projection = '3d')
ax.scatter(normal['convexity'], normal['elongation'], normal['score'], marker = '.')
ax.scatter(thin['convexity'], thin['elongation'], thin['score'], marker = 'x')
ax.scatter(mnist['convexity'], mnist['elongation'], mnist['score'], marker = '^')
ax.scatter(mostlyconvex['convexity'], mostlyconvex['elongation'], mostlyconvex['score'], marker = '+')
ax.set_xlabel('Convexity')
ax.set_ylabel('Elongation')
ax.set_zlabel('Awesomeness')
ax.view_init(elev = 18, azim = -40, roll = 0)
ax.legend(['Normal', 'Thin', 'MNIST', 'Mostlyconvex'], markerscale = 2.5)
plt.savefig('cae.png', bbox_inches = 'tight', pad_inches = 0.4)
