import sys
from django.db import models
from django.shortcuts import render
# from .models import Condition
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os
import descartes

data_pth = "./Data/"
usa= gpd.read_file(os.path.join(data_pth, 'states.shp'))

cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
cities = gpd.read_file(os.path.join(data_pth, "ne_10m_populated_places.shp"))
uscities = cities.query('ADM0NAME == "United States of America"')

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

#___this_is_the_code_needed_to_render_our_map_using_mymd_condtitions_data_once_we_figure_out_thia_bug___________________

# all_conditions = Condition.objects.all()

# merged = usa.set_index(‘state’).join(all_conditions.set_index(‘condition’))
# var = ‘condition’
# # set the range for the choropleth
# vmin, vmax = 120, 220
# # create figure and axes for Matplotlib
# fig, ax = plt.subplots(1, figsize=(10, 6))
#
# merged.plot(column=var, cmap=’Reds’, linewidth=0.8, ax=ax, edgecolor=’0.8')
#______________________________________

def state_plotter(states, us_map=True):
    fig, ax = plt.subplots(figsize=(10,8))
    #turns the axis off
    ax.axis('off')

    #adds a title
    ax.set_title("MeMD Diagnosis Across the US", fontdict={'fontsize': '25', 'fontweight' : '3'})

    if us_map:
        if 'HI' in states:
            usa[0:50].plot(ax=ax, alpha = 0.3)
        elif 'AK' in states:
            usa[1:51].plot(ax=ax, alpha = 0.3)
        elif 'AK' and 'HI' in states:
            usa[0:51].plot(ax=ax, alpha = 0.3)
        else:
            usa[1:50].plot(ax=ax, alpha = 0.3)
        #ax=ax makes the map plot on the initial matplotlib figure
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth = 1)

    elif us_map == False:
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth =2)

# usa[usa.STATE_ABBR == 'TX'].plot()
# usa[usa.SUB_REGION == 'East North Central'].plot()
# base = usa.plot(state_plotter(['LA', 'AR']))
# base = state_plotter(['LA', 'AR'])

base = usa.plot(state_plotter(['LA', 'AR', 'MO', 'CO', 'UT', 'NM', 'TX', 'CA', 'NV', 'MS', 'IL', 'KY', 'TN', 'WV', 'SC','NC', 'OK', 'MD', 'KS', 'IL', 'ID', 'WY', 'NE', 'DC', 'VA', 'PA', 'MN', 'IA', 'AZ']))
uscities.plot(ax=base,figsize=(15,10), color='orange', markersize= 1)

fig, x = plt.subplots(1, 1)
world.plot(column='pop_est', ax=x, legend=True, figsize=(15,10))


# usa.plot()
plt.show()


#______________everything_below_is_just_notes_for_future_reference_________________________



# from models import Conditions
# print(sys.path)
# from conditions_map.models import Conditions
# from django.shortcuts import render

# df.head()

#database stuff
# from models import Conditions
# #
# all_conditions = Conditions.objects.all()

# mysql -u nathanthomas conditions -h localhost --cashflow < exported_mysql_data.sql

# import folium
# plt.rcParams['figure.figsize'] = (10,8)
