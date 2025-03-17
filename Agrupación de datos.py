from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)  # Experiment with different n_clusters
kmeans.fit(df_pca)
df_pca['cluster'] = kmeans.labels_

# Calculate and print the silhouette score
silhouette_avg = silhouette_score(df_pca, kmeans.labels_)
print(f"Silhouette score: {silhouette_avg}")

df_clustered = df_pca