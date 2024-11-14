#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import sqlite3
from PIL import Image
from PIL.ImageOps import invert
import sys
import os

what = sys.argv[1]
how = sys.argv[2]
mid = float(sys.argv[3])
start = mid - 0.05
end   = mid + 0.05

with sqlite3.connect('glyphs.db') as db:
    general = pd.read_sql_query('select * from pores where lfer > 0.9', db)

shit = pd.read_csv('score.csv')
data = general.merge(shit, on = 'label', how = 'inner', validate = "1:1")

query = 'convexity >= %f and convexity < %f' % (start, end)
subdata = data.query(query).sort_values(what, axis = 0)

print(subdata)

plt.rc('font', size = 14)
fig = plt.figure(figsize = (10, 4), dpi = 300)
for i in range(5):
    name = subdata.iloc[i]['label'] + '.pbm'
    img = Image.open(os.path.expanduser(os.path.join('~', 'test', 'grains', name)))
    ax = fig.add_subplot(2, 5, i+1)
    ax.imshow(invert(img))
    ax.title.set_text('$%s = %.4f$' % (how, subdata.iloc[i][what]))
    ax.xaxis.set_major_locator(ticker.NullLocator())
    ax.yaxis.set_major_locator(ticker.NullLocator())

for i in range(5):
    name = subdata.iloc[-i-1]['label'] + '.pbm'
    img = Image.open(os.path.expanduser(os.path.join('~', 'test', 'grains', name)))
    ax = fig.add_subplot(2, 5, i+6)
    ax.imshow(invert(img))
    ax.title.set_text('$%s = %.2f$' % (how, subdata.iloc[-i-1][what]))
    ax.xaxis.set_major_locator(ticker.NullLocator())
    ax.yaxis.set_major_locator(ticker.NullLocator())

plt.subplots_adjust(wspace = 0.3, hspace = 0.05)
plt.savefig('groups-%s-%.2f.png' % (what, mid), bbox_inches='tight')
