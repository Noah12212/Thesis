# This script was produced by glue and can be used to further customize a
# particular plot.

### Package imports

from glue.core.state import load
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')
# matplotlib.use('qt5Agg')

### Set up data

data_collection = load('Individual investment Plot.py.data')

### Set up viewer

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='auto', projection='rectilinear')

# for the legend
legend_handles = []
legend_labels = []
legend_handler_dict = dict()

### Set up layers

## Layer 1: ndf_1

layer_data = data_collection[0]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#6c2d22', markersize=3, alpha=0.8, zorder=1, label='ndf_1', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 2: ndf_2

layer_data = data_collection[1]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#2d6c31', markersize=3, alpha=0.8, zorder=2, label='ndf_2', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 3: ndf_3

layer_data = data_collection[2]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#374989', markersize=3, alpha=0.8, zorder=3, label='ndf_3', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 4: ndf_4

layer_data = data_collection[3]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#acc32a', markersize=3, alpha=0.8, zorder=4, label='ndf_4', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 5: ndf_5

layer_data = data_collection[4]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#b04ab4', markersize=3, alpha=0.8, zorder=5, label='ndf_5', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)

### Legend

ax.legend(legend_handles, legend_labels,
    handler_map=legend_handler_dict,
    loc='best',            # location
    framealpha=0.66,      # opacity of the frame
    title='',             # title of the legend
    title_fontsize=3,   # fontsize of the title
    fontsize=3,          # fontsize of the labels
    facecolor='#ffffff',
    edgecolor=(0.0, 0.0, 0.0, 0.6565656565656566)
)

### Finalize viewer

# Set limits
ax.set_xlim(left=0.0, right=200.0)
ax.set_ylim(bottom=2.0, top=4.5)


# Set scale (log or linear)
ax.set_xscale('linear')
ax.set_yscale('linear')


# Set axis label properties
ax.set_xlabel('λ', weight='normal', size=10)
ax.set_ylabel('Expected Individual Investment', weight='normal', size=10)

# Set tick label properties
ax.tick_params('x', labelsize=8)
ax.tick_params('y', labelsize=8)

# For manual edition of the plot
#  - Uncomment the next code line (plt.show)
#  - Also change the matplotlib backend to qt5Agg
#  - And comment the "plt.close" line
# plt.show()

# Save figure
fig.savefig('glue_plot.png')
plt.close(fig)












