import point_cloud_utils as pcu
import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

# Load the point clouds
p1, f1 = pcu.load_mesh_vf("ply-input/blur.ply")
p2, f1 = pcu.load_mesh_vf("ply-input/2Deblur.ply")
p3, f1 = pcu.load_mesh_vf("ply-input/original.ply")

# Function to compute distances to nearest neighbors
def nearest_neighbor_distances(p1, p2):
    tree = cKDTree(p2)
    distances, _ = tree.query(p1)
    return distances

# Compute distances
distances_blur = nearest_neighbor_distances(p1, p3)
distances_deblur = nearest_neighbor_distances(p2, p3)

# Plot CDF
def plot_cdf(data, label, color):
    sorted_data = np.sort(data)
    yvals = np.arange(len(sorted_data)) / float(len(sorted_data) - 1)
    plt.plot(sorted_data, yvals, label=label, color=color)

plot_cdf(distances_blur, 'Blurred', 'red')
plot_cdf(distances_deblur, 'Deblurred', 'blue')

plt.xlabel('Distance to Original')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Distances to Original Point Cloud')
plt.legend()
plt.show()
