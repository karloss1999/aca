import matplotlib.pyplot as plt
import seaborn as sns

# 1. Scatter plot of PC1 and PC2 colored by cluster
plt.figure(figsize=(8, 6))
sns.scatterplot(x=0, y=1, hue='cluster', data=df_clustered, palette='viridis')
plt.title('Clusters visualized using first two principal components')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# 2. Bar chart of cluster distribution
plt.figure(figsize=(6, 4))
df_clustered['cluster'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of data points across clusters')
plt.xlabel('Cluster')
plt.ylabel('Number of data points')
plt.show()


# 3. Correlation heatmap (focus on important variables)
important_variables = ['price', 'sales_count', 'reviews_count', 'average_rating', 'discount']
plt.figure(figsize=(8, 6))
sns.heatmap(df_numeric[important_variables].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Important Numerical Features')
plt.show()

# 4. Additional visualizations:
# Box plots of key numerical features grouped by cluster
numerical_features_for_boxplot = ['price', 'sales_count', 'average_rating']
plt.figure(figsize=(12, 6))
for i, col in enumerate(numerical_features_for_boxplot):
  plt.subplot(1, len(numerical_features_for_boxplot), i+1)
  sns.boxplot(x='cluster', y=col, data=pd.concat([df_clustered, df_numeric], axis=1), palette='Set2')
  plt.title(f'Boxplot of {col} by Cluster')
plt.tight_layout()
plt.show()

# Scatter plot showing the relationship between important features, colored by cluster
plt.figure(figsize=(8, 6))
sns.scatterplot(x='price', y='sales_count', hue='cluster', data=pd.concat([df_clustered, df_numeric], axis=1), palette='viridis')
plt.title('Sales Count vs. Price, colored by cluster')
plt.show()