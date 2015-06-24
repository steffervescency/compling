from matplotlib import pyplot
import matplotlib.pyplot as plt


def import_data(filename):

    with open (filename, "r") as f:
       dataPoints = {int(line.split()[0]): (float(line.split()[1]), float(line.split()[2])) \
                     for line in f if '#' not in line}
    return dataPoints


def one_dimension_clustering(dataPoints, mean1, mean2, xy):

    cluster1 = {pointID: (dataPoints[pointID][0], dataPoints[pointID][1]) \
                for pointID in dataPoints \
                if abs(dataPoints[pointID][xy]-mean1) <= abs(dataPoints[pointID][xy]-mean2)}

    cluster2 = {pointID: (dataPoints[pointID][0], dataPoints[pointID][1]) \
                for pointID in dataPoints \
                if abs(dataPoints[pointID][xy]-mean1) > abs(dataPoints[pointID][xy]-mean2)}

    newMean1 = sum(cluster1[pointID][xy] for pointID in cluster1)/len(cluster1)
    newMean2 = sum(cluster2[pointID][xy] for pointID in cluster2)/len(cluster2)

    while True:
        if abs(mean1 - newMean1) != 0.0 and abs(mean2 - newMean2) != 0.0:
            one_dimension_clustering(dataPoints, newMean1, newMean2, xy)
        return mean1, mean2, cluster1, cluster2

def plot_data(dataPoints, colour):

    x = [dataPoints[pointID][0] for pointID in dataPoints]
    y = [dataPoints[pointID][1] for pointID in dataPoints]

    pyplot.plot(x, y, (colour + 'o')) #ro meant red+dot

'''
#multi_dimensional_clustering(dataPoints, [(-10, 100), (10, -100) etc.])
def multi_dimensional_clustering(dataPoints, means):

    meansDict = {means.index(mean): mean for mean in means} #we do this so that each cluster/centre has an ID
    someDict = dict()
    for dataID in dataPoints:
        someOtherDict = dict()
        for meanID in meansDict:
            distance = sum((meansDict[meanID][i] - dataPoints[dataID][i])**2 \
                           for i in range(0, len(meansDict[meanID])))
            someOtherDict[meanID] = distance
        lowestClusterId = min(someOtherDict, key=someOtherDict.get)
        try:
            someDict[lowestClusterId][dataID] = dataPoints[dataID]
        except:
            someDict[lowestClusterId] = dict()
            someDict[lowestClusterId][dataID] = dataPoints[dataID]

    newMeans = {clusterID:  \
                for clusterID in someDict\
                for i in range (0, len(someDict[clusterID])) \

                }

'''




print("hhellow")





dataPoints = import_data('Exercise-8.dat')
print(dataPoints)
#someDict = multi_dimensional_clustering(dataPoints, [(-10, 100), (10, -100)])



xMean1, xMean2, xCluster1, xCluster2 = one_dimension_clustering(dataPoints, -3, 2, 0) #last argument is 0 for x and 1 for y
plot_data(xCluster1, 'b')
plot_data(xCluster2, 'r')
pyplot.show()

yMean1, yMean2, yCluster1, yCluster2 = one_dimension_clustering(dataPoints, 1, 2, 1)
plot_data(yCluster1, 'b')
plot_data(yCluster2, 'r')
pyplot.show()

#multi_dimensional_clustering(dataPoints, [(-10, 100), (10, -100)])