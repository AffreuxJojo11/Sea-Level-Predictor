import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, axes = plt.subplots(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    fig, axes = plt.subplots(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051, 1)
    plt.plot(years_extended, res.intercept + res.slope*years_extended, 'r', label='fitted line')

    # Create second line of best fit
    df2 = df.loc[df['Year']>=2000]
    res = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(2000, 2051, 1)
    plt.plot(years_extended, res.intercept + res.slope*years_extended, 'r', label='fitted line')

    # Add labels and title
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()