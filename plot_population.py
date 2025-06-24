import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Read the data
filename = 'API_SP.POP.TOTL_DS2_en_csv_v2_81108.csv'  # Ensure this file is NEXT TO this script
df = pd.read_csv(filename, skiprows=4)

# STEP 2: Choose a country
country_name = 'India'  # You can change this
country_df = df[df['Country Name'] == country_name]

# STEP 3: Extract years and population data
years = list(range(2000, 2023))
pop_values = country_df[[str(year) for year in years]].values.flatten() / 1e6  # in millions

# STEP 4: Plot the data
plt.figure(figsize=(10, 6))
plt.bar(years, pop_values, color='steelblue')
plt.title(f'{country_name} Population (2000–2022)', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# STEP 5: Show the chart
plt.show()
