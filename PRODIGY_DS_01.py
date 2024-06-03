#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_23.csv'
population_data = pd.read_csv(file_path, skiprows=4)

# Extracting data for a specific year, let's use the latest available year 2022
year = '2022'
population_2022 = population_data[['Country Name', year]].dropna()

# Sorting the data by population in descending order
population_2022_sorted = population_2022.sort_values(by=year, ascending=False).head(10)

# Plotting the bar chart
plt.figure(figsize=(14, 8))
plt.bar(population_2022_sorted['Country Name'], population_2022_sorted[year], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population in 2022')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




