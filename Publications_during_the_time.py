import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

csv_file_path = r'C:\Users\dzunk\PycharmProjects\DataScientist(Parser)\result.csv'
df = pd.read_csv(csv_file_path)

df['Dates'] = pd.to_datetime(df['Dates'])
df = df.sort_values('Dates')

df['Year'] = df['Dates'].dt.year
df['Month'] = df['Dates'].dt.month
df['Day'] = df['Dates'].dt.day

start_value = pd.to_datetime('1974-11-01')
end_value = pd.to_datetime('1980-01-15')

# Plot the histogram
plt.figure(figsize=(15, 8))
plt.hist(df['Dates'], bins=60, range=(start_value, end_value), align='left', rwidth=0.8)

# Add a spline-interpolated line connecting the vertices of the histogram
bin_edges = plt.hist(df['Dates'], bins=60, range=(start_value, end_value), align='left', rwidth=0.8)[1]
bin_heights = plt.hist(df['Dates'], bins=60, range=(start_value, end_value), align='left', rwidth=0.8)[0]
spline = make_interp_spline(bin_edges[:-1], bin_heights)
x_new = np.linspace(bin_edges[:-1].min(), bin_edges[:-1].max(), 500)
y_new = spline(x_new)
plt.plot(x_new, y_new, color='black', linewidth=2.5)

plt.ylabel('Frequency', fontsize=30)
plt.title('Histogram of Dates', fontsize=40)

plt.xlim(start_value, end_value)
plt.gca().set_ylim([0, 350])

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


plt.savefig('hist.png')
