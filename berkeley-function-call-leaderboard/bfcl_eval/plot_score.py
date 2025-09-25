import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV
df = pd.read_csv('score/data_non_live.csv')

# Clean columns: convert to string, remove '%', replace 'N/A', convert to float
for col in df.columns[2:]:
    df[col] = (
        df[col]
        .astype(str)
        .replace('N/A', None)
        .str.replace('%', '', regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop columns where all values are NaN or zero (excluding Rank and Model)
cols_to_keep = ['Rank', 'Model']
for col in df.columns[2:]:
    if df[col].notna().any() and (df[col].fillna(0) != 0).any():
        cols_to_keep.append(col)

df_plot = df[cols_to_keep]

# Melt the DataFrame to long format for grouped bar plot
df_melted = df_plot.melt(id_vars=['Rank', 'Model'], var_name='Metric', value_name='Value')

# Remove rows with NaN or zero values
df_melted = df_melted[df_melted['Value'].notna() & (df_melted['Value'] != 0)]

# Plot: x=Metric, hue=Model, y=Value
plt.figure(figsize=(14, 7))
sns.barplot(data=df_melted, x='Metric', y='Value', hue='Model')
plt.ylabel('Accuracy (%)')
plt.title('Non-Live Model Accuracies by Metric')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('score.png')
plt.close()