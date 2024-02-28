# -*- coding: utf-8 -*-
"""SI_p10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRUm83lVZIdV0_80lqrlzvRJNEY4sA1I
"""



#PART ONE 
#---------------------------------------------------------------------------------------

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(0)

# Generate random data from various distributions
uniform_data = np.random.uniform(0, 1, 1000)
normal_data = np.random.normal(0, 1, 1000)
gamma_data = np.random.gamma(2, 2, 1000)
exponential_data = np.random.exponential(2, 1000)
binomial_data = np.random.binomial(10, 0.5, 1000)

# Create subplots for each distribution
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
sns.distplot(uniform_data, hist=False)
plt.title('Uniform Distribution')

plt.subplot(2, 3, 2)
sns.distplot(normal_data, hist=False)
plt.title('Normal Distribution')

plt.subplot(2, 3, 3)
sns.distplot(gamma_data, hist=False)
plt.title('Gamma Distribution')

plt.subplot(2, 3, 4)
sns.distplot(exponential_data, hist=False)
plt.title('Exponential Distribution')

plt.subplot(2, 3, 5)
sns.distplot(binomial_data, hist=False)
plt.title('Binomial Distribution')

# Display the plots
plt.tight_layout()
plt.show()

#PART TWO 
#---------------------------------------------------------------------------


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(0)

# Number of iterations
num_iterations = 1000
sample_size = 1000

# Lists to store the sample means for each distribution
means_uniform = []
means_normal = []
means_gamma = []
means_exponential = []
means_binomial = []

for _ in range(num_iterations):
    uniform_data = np.random.uniform(0, 1, sample_size)
    normal_data = np.random.normal(0, 1, sample_size)
    gamma_data = np.random.gamma(2, 2, sample_size)
    exponential_data = np.random.exponential(2, sample_size)
    binomial_data = np.random.binomial(10, 0.5, sample_size)

    means_uniform.append(np.mean(uniform_data))
    means_normal.append(np.mean(normal_data))
    means_gamma.append(np.mean(gamma_data))
    means_exponential.append(np.mean(exponential_data))
    means_binomial.append(np.mean(binomial_data))

# Create subplots for the sample mean distributions
plt.figure(figsize=(15, 6))

plt.subplot(2, 3, 1)
sns.distplot(means_uniform, hist=False)
plt.title('Sample Means (Uniform)')

plt.subplot(2, 3, 2)
sns.distplot(means_normal, hist=False)
plt.title('Sample Means (Normal)')

plt.subplot(2, 3, 3)
sns.distplot(means_gamma, hist=False)
plt.title('Sample Means (Gamma)')

plt.subplot(2, 3, 4)
sns.distplot(means_exponential, hist=False)
plt.title('Sample Means (Exponential)')

plt.subplot(2, 3, 5)
sns.distplot(means_binomial, hist=False)
plt.title('Sample Means (Binomial)')

# Display the plots
plt.tight_layout()
plt.show()



#PART THERE
# (FOR RUN THE REST OF CODE, it is necessary to first execute parts three and four before proceeding with the rest of the code.)
#------------------------------------------------------------------------------------------


import pandas as pd

#I used Google Colab to write this code. If you want to run it anywhere else, you must import the prob10.csv file. 
#I generally recommend using Google Colab. 

#from google.colab import drive
#drive.mount('/content/drive')  
# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('prob10.csv')



#PART FOUR 
#------------------------------------------------------------------------------------------------



#Data contains "?" replace it with NAN
df_data = df.replace('?',np.NAN)
df_data.isnull().sum()

from collections import defaultdict
df_temp = df[df['normalized-losses']!='?']
normalized_mean = df_temp['normalized-losses'].astype(int).mean()
df['normalized-losses'] = df['normalized-losses'].replace('?',normalized_mean).astype(int)

df_temp = df[df['price']!='?']
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(subset=['price'], inplace=True)


df_temp = df[df['horsepower']!='?']
normalized_mean = df_temp['horsepower'].astype(int).mean()
df['horsepower'] = df['horsepower'].replace('?',normalized_mean).astype(int)

df_temp = df[df['peak-rpm']!='?']
normalized_mean = df_temp['peak-rpm'].astype(int).mean()
df['peak-rpm'] = df['peak-rpm'].replace('?',normalized_mean).astype(int)

df_temp = df[df['bore']!='?']
normalized_mean = df_temp['bore'].astype(float).mean()
df['bore'] = df['bore'].replace('?',normalized_mean).astype(float)

df_temp = df[df_data['stroke']!='?']
df_temp['stroke'] = df['stroke'].replace('?', float('nan'))
normalized_mean = df_temp['stroke'].astype(float).mean()
df['stroke'] = df['stroke'].replace('?',normalized_mean).astype(float)


df['num-of-doors'] = df['num-of-doors'].replace('?','four')
df.head()


#PART SIX
#--------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt


# Count the frequency of each car manufacturer
manufacturer_counts = df['make'].value_counts()

# Plot the bar graph
plt.figure(figsize=(10, 6))
manufacturer_counts.plot(kind='bar', color='Violet')
plt.title('Car Manufacturer Frequency')
plt.xlabel('Manufacturer')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

# Find the manufacturer with the most cars
most_cars_manufacturer = manufacturer_counts.idxmax()
most_cars_count = manufacturer_counts.max()

# Convert the index to a list of strings
manufacturer_names = manufacturer_counts.index.tolist()

# Check if the manufacturer name exists in the list before annotating
if most_cars_manufacturer in manufacturer_names:
    plt.annotate(f'Most Cars: {most_cars_manufacturer} ({most_cars_count} cars)',
                 xy=(manufacturer_names.index(most_cars_manufacturer), most_cars_count),
                 xytext=(0, 20), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', color='red'))

plt.show()


#PART SEVEN 
#--------------------------------------------------------------------------------------------------------


import pandas as pd
from scipy.stats import skew, kurtosis


# Calculate the standard deviation for price 
std_deviation = df['price'].std()

# Calculate skewness for price 
skewness = skew(df['price'])

# Calculate kurtosis for price 
kurt = kurtosis(df['price'])

print(f"Standard Deviation: {std_deviation}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Calculate standard deviation, skewness, and kurtosis for all numerical columns
import pandas as pd
from scipy.stats import skew, kurtosis


# Get the numerical columns in the dataset
numerical_columns = df.select_dtypes(include=['number'])

# Calculate and display statistics for each numerical column
for col in numerical_columns.columns:
    std_deviation = numerical_columns[col].std()
    skewness = skew(numerical_columns[col])
    kurt = kurtosis(numerical_columns[col])

    print(f"Column: {col}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Skewness: {skewness}")
    print(f"Kurtosis: {kurt}")
    print()


#PART EIGHT
#--------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt


# Extract the "engine-size" and "price" columns
engine_size = df['engine-size']
price = df['price']

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(engine_size, price, c='Crimson', marker='o')
plt.title('Scatter Plot of Engine Size vs. Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')

# Show the plot
plt.show()

#PART NINE
#--------------------------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Select the some columns for analysis
selected_columns = ['length', 'wheel-base', 'highway-mpg', 'horsepower']
data_to_plot = df[selected_columns]

# Specify the color for the plots using plot_kws
plot_kws = {'color': 'goldenrod'}

# Create a pairplot for the selected columns with the specified color
sns.pairplot(data_to_plot, plot_kws=plot_kws)
plt.show()


#PART TEN 
#---------------------------------------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Calculate the correlation matrix for all numerical columns
correlation_matrix = df.corr()
# Create a heatmap of the correlation matrix
plt.figure(figsize=(15, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="PuBu", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()



#PART ELEVEN
#---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Define the categorical column for analysis
categorical_column = 'body-style'


# Create a custom color palette with distinct colors
custom_palette = ["#00A170", "#AD1C38", "#D1A715", "#9065E8", "#28747A"]

# Create a boxplot for the specified column
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x=categorical_column, y='price', showfliers=False , palette=custom_palette )
plt.title(f'Boxplot of {categorical_column}')

# Calculate percentile, IQR, and whiskers
percentiles = df.groupby(categorical_column)['price'].describe()[['25%', '75%']].reset_index()
iqr = percentiles['75%'] - percentiles['25%']
lower_whisker = percentiles['25%'] - 1.5 * iqr
upper_whisker = percentiles['75%'] + 1.5 * iqr

print(f'Column: {categorical_column}')
print(f'Percentiles:\n{percentiles}')
print(f'IQR: {iqr.iloc[0]}')
print(f'Lower Whisker: {lower_whisker.iloc[0]}')
print(f'Upper Whisker: {upper_whisker.iloc[0]}')

plt.tight_layout()
plt.show()