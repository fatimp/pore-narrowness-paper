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

f = lambda e: 4*e/(np.pi * (3*(1+e) - np.sqrt((3*e+1)*(e+3))))
xs = np.linspace(0, 1, 100)

plt.figure(figsize = (10, 8), dpi = 300)
plt.rc('font', size = 17)
plt.scatter(normal['elongation'], normal['score'], marker = '.')
plt.scatter(thin['elongation'], thin['score'], marker = 'x')
plt.scatter(mnist['elongation'], mnist['score'], marker = '^')
plt.scatter(mostlyconvex['elongation'], mostlyconvex['score'], marker = '+')
plt.plot(xs, f(xs), 'b--')
plt.legend(['Normal', 'Thin', 'MNIST', 'Mostlyconvex', 'Ellipses'], markerscale = 2.5)
plt.xlabel('Elongation')
plt.ylabel('Awesomeness')
plt.savefig('ae.png', bbox_inches = 'tight')
