from matplotlib import pyplot
import matplotlib.pyplot as plt
import random, operator, math
from collections import defaultdict


def import_data(filename):
    with open (filename, "r") as f:
       dataPoints = [(float(line.split()[1]), float(line.split()[2])) \
                     for line in f if '#' not in line]
    return dataPoints


def absolute_distance(x, y):
    return abs(x[0] - y[0])

def squared_euclidean_distance(x, y):
    dist = sum([(a-b)**2 for (a,b) in zip(x,y)])
    return dist

# Calculate the z-score of each data point
def normalize(dataPoints):
    new_pts = []
    for dim_pts in zip(*dataPoints):
        total = sum(dim_pts)
        mean = total/len(dataPoints)
        square_diffs = [(pt-mean)**2 for pt in dim_pts]
        variance = sum(square_diffs)/len(dataPoints)
        std_dev = math.sqrt(variance)
        new_pts.append([(pt - mean)/std_dev for pt in dim_pts])
    
    return list(zip(*new_pts))

# Args:
#   dataPts, an array of tuples
#   numClusters: the number of clusters to partition the data into
# Returns:
#   A dictionary of the form cluster_id => list of dataPts indices
def kmeans(dataPts, numClusters):
    dims = len(dataPts[0])
    
    dataPts = normalize(dataPts)
    
    if(dims == 1):
        metric = absolute_distance
    elif(dims == 2):
        metric = squared_euclidean_distance   
   
    # Initialize by selecting random points as centers
    means = random.sample(dataPts, numClusters)
   
    while True:
        clusters = defaultdict(list)

        # Calculate cluster assignment for each point
        for pt_idx, pt in enumerate(dataPts):
            # Calculate the distance to each mean
            distances = [metric(pt, m) for m in means]
            # Assign to the cluster with the closest mean
            min_idx, min_value = min(enumerate(distances), key=operator.itemgetter(1))
            clusters[min_idx].append(pt_idx)
        
        # Calculate the new means
        new_means = []
        for cluster_idx, pts_idx in clusters.items():
            pts = [dataPts[idx] for idx in pts_idx]
            n = len(pts)
            m = [sum(dim)/n for dim in zip(*pts)]
            new_means.append(m)
        
        # check if we have converged
        if new_means == means:
            break
        means = new_means
        
    return clusters        

# Calculate the VRC value for the given data points and k
def vrc(dataPoints, k):
    clusters = kmeans(dataPoints, k)
    dataPoints = normalize(dataPoints)
    cluster_pts = [[dataPoints[idx] for idx in pts_idx] for pts_idx in clusters.values()]
    
    metric = squared_euclidean_distance
    grand_mean = [sum(pts)/len(dataPoints) for pts in zip(*dataPoints)]

    ssb = 0
    ssw = 0
    
    for cluster in cluster_pts:
        n = len(cluster)
        center = [sum(pts)/n for pts in zip(*cluster)]
        ssb += metric(grand_mean, center)*n
        ssw += sum([metric(center, pt) for pt in cluster])
    
    return (ssb/(k-1))/(ssw/(len(dataPoints)-k))

# Find the best k for the given data points
def min_vrc(dataPoints):
    vrcs = {k: vrc(dataPoints, k) for k in range(2, 11)}
    min_val = float("inf")
    best_k = 0
    for k in range(3, 10):
        val = ((vrcs[k+1] - vrcs[k]) - (vrcs[k] - vrcs[k-1]))
        if val < min_val:
            min_val = val
            best_k = k
    return best_k

# Plot a single cluster    
def plot_cluster(dataPoints, colour):
    x = [point[0] for point in dataPoints]
    y = [point[1] for point in dataPoints]

    pyplot.scatter(x, y, color=colour) #ro meant red+dot

# Plot all clusters
def plot_clusters(clusters):
    cluster_pts = []
    color = ['Red', 'Green', 'Blue', 'Orange', 'Purple', 'Magenta', 'Black', 'Pink', 'Brown']
    for cluster_idx, pts_idx in clusters.items():
        cluster_pts.append([dataPoints[idx] for idx in pts_idx])
    
    for idx, cluster in enumerate(cluster_pts):
        plot_cluster(cluster, color[idx])
    pyplot.show()


dataPoints = import_data('Exercise-8.dat')

# one dimensional clustering
xs = [(pt[0],) for pt in dataPoints]
ys = [(pt[1],) for pt in dataPoints]

#clusters = kmeans(xs, 2)
#clusters = kmeans(ys, 2)

# multi-dimensional clustering
clusters = kmeans(dataPoints, 6)
plot_clusters(clusters)