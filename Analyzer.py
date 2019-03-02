#!/usr/bin/env python3
# coding: utf-8

#----------------------------------------------------------------------#
# Copyright (C) 2019, Vinícius Orsi Valente (viniciusov@hotmail.com)   #
#                                                                      #
# This file is part of WhatsApp-Group-Analyzer.                        #
#                                                                      # 
# WhatsApp-Group-Analyzer is free software: you can redistribute it    #
# and/or modify it under the terms of the GNU General Public License   #
# as published by the Free Software Foundation, either version 3 of    #
# the License, or (at your option) any later version.                  #
#                                                                      #
# WhatsApp-Group-Analyzer is distributed in the hope that it will be   #
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty  #
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU  #
# General Public License for more details.                             #
#                                                                      # 
# You should have received a copy of the GNU General Public License    #
# along with WhatsApp-Group-Analyzer. If not, see                      #
# <https://www.gnu.org/licenses/>.                                     #
#----------------------------------------------------------------------#

#--------------------------------------------------#
#                   Import Libraries               #
#--------------------------------------------------#

import re
from collections import OrderedDict
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
import pandas as pd
from pandas.plotting import table

#--------------------------------------------------#
#                   Open Chat File                 #
#--------------------------------------------------#

messages = []
with open("Chat.txt", encoding="utf8") as f:
    for line in f:
        messages.append(line)

#--------------------------------------------------#
#                   Prepare Data                   #
#--------------------------------------------------#        

clean_messages = []
for x in messages:
    if re.match('\d{1}[/]\d{2}[/]\d{2}', x) is not None: 
        clean_messages.append(x[17:])

for n,x in enumerate(clean_messages):
    clean_messages[n]=x.split(':')[0]

names = []
for x in clean_messages:
    if re.match('\d{2}\s\d{5}[-]\d{4}', x[5:18]) is not None: #Look for tel numbers
        names.append(x[5:18])
    elif not ('added' in x or 'removed' in x or 'changed' in x or 'left' in x) and x != '':
        names.append(x)

unique_names = set(names)

result = {}
for name in unique_names:
    result[name]=names.count(name)

final_result = OrderedDict((sorted(result.items(), key=lambda x: x[1])))

#--------------------------------------------------#
#               Create Color List                  #
#--------------------------------------------------#

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS) 

color_indexes = random.sample(range(len(colors)), len(unique_names))

color_list = []
for n in color_indexes:
    color_list.append(list(colors.keys())[n])
    
color_list = list(colors.keys())

#--------------------------------------------------#
#               Create Bar Chart                   #
#--------------------------------------------------#

plt.figure(figsize=(len(final_result)/2,len(final_result)/4))
bars = plt.bar(range(len(final_result)), final_result.values(), align='center')

for n,bar in enumerate(bars): #Set different color for each bar
    bar.set_color(color_list[n])
    
plt.yticks(np.arange(0, max(final_result.values())+500, step=500))
plt.xticks(range(len(final_result)), final_result.keys(), rotation='90')

for bar in bars: #Print numbers above bars
    yval = bar.get_height()
    plt.text(bar.get_x(),yval+100, yval, fontsize=8)

plt.savefig('pic1.png', bbox_inches='tight')

#--------------------------------------------------#
#               Create Pie Chart                   #
#--------------------------------------------------#

result_new = {}
result_new['others'] = 0

for x,n in final_result.items():
    if n < 0.1*max(final_result.values()):
        result_new['others']+=n
    else:
        result_new[x]=n        

labels = result_new.keys()
sizes = result_new.values()
explode = np.zeros(len(result_new))
explode[-1] = 0.05

plt.figure() #Pie chart as a new figure
plt.pie(sizes, explode=explode, labels=labels, pctdistance=0.8, autopct='%1.1f%%', startangle=90, colors=color_list[len(unique_names)-len(result_new):])
plt.axis('equal')  #Ensures pie chart is drawn as a circle.

plt.savefig('pic2.png', bbox_inches='tight')

#--------------------------------------------------#
#		   Create Report                   #
#--------------------------------------------------#

import pandas as pd
from pandas.plotting import table

df = pd.DataFrame(reversed(final_result.items()),index=range(1,len(final_result)+1),columns=['CONTACT','MESSAGES'])

fig,ax = plt.subplots(figsize=(8, len(final_result)/4)) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis
ax.set_frame_on(False)  # no visible frame, uncomment if size is ok

table = table(ax, df, loc='center', colWidths=[0.25]*len(df.columns))  # where df is your data frame
table.auto_set_font_size(False) # Activate set fontsize manually
table.set_fontsize(10) # if ++fontsize is necessary ++colWidths

plt.savefig('pic3.png', bbox_inches='tight')
