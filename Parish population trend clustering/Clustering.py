import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import os
import plotly.express as px

os.chdir(os.path.dirname(os.path.abspath(__file__))) 
# Ensures script is always using files in the same directory as the script

dataFile = pd.read_excel('2020-cornwall-parish-population-estimates.xlsx', header = 3)
years = list(range(2012, 2021))
dataset = dataFile[['Parish Name'] + years].copy()
dataset.set_index('Parish Name', inplace=True)
# extracts relevant information from excell file and compiles them into a new dataset

dataset['growth percentage'] = ((dataset[2020] - dataset[2012]) / dataset[2012]) * 100
# Processes the % change in population between 2012 & 2020.
features = dataset[['growth percentage', 2020]].copy()
features.columns = ['growth percentage', 'population in 2020']
# Strips the data to be analysed from the dataset into a matrix
scaler = StandardScaler()
scaledFeatures = scaler.fit_transform(features)
# Normalises data so parishes orders of magnitude larger than the smallest dont throw off the analysis

# K-means analysis to identify optimal number of clusters using elbow method.
'''inertias = []
# List containing sum of squared distances of data points to their closest cluster centroid.
# We look for the 'elbow' where inertia stops decreasing sharply.
KRange = range(1, 11)
for k in KRange:
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(scaledFeatures)  
    inertias.append(kmeans.inertia_)
plt.figure(figsize=(8,4))
plt.plot(KRange, inertias, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()'''


k = 6
kmeans = KMeans(n_clusters=k, n_init=10)
# n_init determines the number of times the algorithm is run with different starting centroid seeds
dataset['cluster2d'] = kmeans.fit_predict(scaledFeatures)
summary = dataset.groupby('cluster2d')['growth percentage'].agg(['count', 'mean', 'std', 'min', 'max'])
print(summary)
# Prints information about each cluster

plotData = dataset.reset_index()
plotData.columns = ['Parish Name', 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 'growth percentage', 'cluster']
fig = px.scatter(plotData, 
                 x='growth percentage', 
                 y=2020,
                 color='cluster',
                 hover_name='Parish Name', 
                 log_y=True,
                 title='Parish clusters: growth vs population (hover for names)')
fig.show()
# Uses Plotly to create an interactive scatter graph that shows information about each data point when hovered over 

