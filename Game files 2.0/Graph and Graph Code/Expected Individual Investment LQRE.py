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

data_collection = load('Expected Individual Investment LQRE.py.data')

### Set up viewer

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect='auto', projection='rectilinear')

# for the legend
legend_handles = []
legend_labels = []
legend_handler_dict = dict()

### Set up layers

## Layer 1: 6 Players

layer_data = data_collection[4]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#ff40ff', markersize=3, alpha=0.8, zorder=1, label='6 Players', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 2: 5 Players

layer_data = data_collection[3]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#00f900', markersize=3, alpha=0.8, zorder=2, label='5 Players', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 3: 4 Players

layer_data = data_collection[2]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#00fdff', markersize=3, alpha=0.8, zorder=3, label='4 Players', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 4: 3 Players

layer_data = data_collection[1]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#aa7942', markersize=3, alpha=0.8, zorder=4, label='3 Players', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)
## Layer 5: 2 Players

layer_data = data_collection[0]

layer_handles = []  # for legend# Get main data values
x = layer_data['col1']
y = layer_data['col2']
keep = ~np.isnan(x) & ~np.isnan(y)
plot_artists = ax.plot(x[keep], y[keep], 'o', color='#0433ff', markersize=3, alpha=0.8, zorder=5, label='2 Players', mec='none')
layer_handles.extend(plot_artists)

legend_handles.append(tuple(layer_handles))
legend_labels.append(layer_data.label)

### Legend

ax.legend(legend_handles, legend_labels,
    handler_map=legend_handler_dict,
    loc='best',            # location
    framealpha=0.59,      # opacity of the frame
    title='',             # title of the legend
    title_fontsize=5,   # fontsize of the title
    fontsize=5,          # fontsize of the labels
    facecolor='#FFFFFF',
    edgecolor=(0.0, 0.0, 0.0, 0.5858585858585859)
)

### Finalize viewer

# Set limits
ax.set_xlim(left=0.0, right=155.0)
ax.set_ylim(bottom=2.0, top=4.25)


# Set scale (log or linear)
ax.set_xscale('linear')
ax.set_yscale('linear')


# Set axis label properties
ax.set_xlabel('λ', weight='normal', size=10)
ax.set_ylabel('Expected Individual Investment ', weight='normal', size=10)

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