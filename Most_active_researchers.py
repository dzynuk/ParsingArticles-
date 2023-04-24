import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file_path = r'C:\Users\dzunk\PycharmProjects\DataScientist(Parser)\result.csv'
df = pd.read_csv(csv_file_path, encoding='latin-1')

# Clean and preprocess the 'Authors' column
df['Authors'] = df['Authors'].str.replace(r'[\[\]\'\"]', '', regex=True)
df['Authors'] = df['Authors'].str.split(', ')

author_count = df.explode('Authors')['Authors'].value_counts()

top_21_to_40_authors = author_count.iloc[1:21]

top_21_to_40_authors.index = top_21_to_40_authors.index.where(top_21_to_40_authors.index != '', '20')

sns.set_style('whitegrid')

plt.figure(figsize=(12, 6))
sns.barplot(x=top_21_to_40_authors.index, y=top_21_to_40_authors.values)
plt.title('Top 20 Most Active Researchers')
plt.xticks(rotation=70)

plt.savefig('top_20_authors_plot.png')
plt.show()