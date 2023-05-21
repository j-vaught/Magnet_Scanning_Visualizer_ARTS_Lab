import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap

# Load data from Excel
df = pd.read_excel('Magnet_data_05-21-2023.xlsx')

# Convert DataFrame into numpy array for easy manipulation
data = df.to_numpy()

# Generate y, x coordinates. We switch x and y because rows correspond to y (not x) and columns to x (not y).
y = np.arange(data.shape[0])
x = np.arange(data.shape[1])

# Create a grid for x, y
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define a colormap
cmap = LinearSegmentedColormap.from_list(
    "my_colormap", [(0, "red"), (0.5, "yellow"), (0.75, "green"), (1, "blue")], N=256
)

# Scale data to range 0-1
scaled_data = (data + 300) / (50 + 300)

# Create a surface plot
surf = ax.plot_surface(X, Y, data, facecolors=cmap(scaled_data), shade=False)

# Add a color bar which maps values to colors
m = plt.cm.ScalarMappable(cmap=cmap)
m.set_array(data)
fig.colorbar(m, shrink=0.5, aspect=5)

ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Magnetic Field Strength (gauss)')

plt.show()
