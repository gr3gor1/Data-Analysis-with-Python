import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    firstLine = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    xfirst = np.arange(df['Year'].min(),2051,1)
    yfirst = xfirst*firstLine.slope + firstLine.intercept
    plt.plot(xfirst,yfirst)
  
    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    secondLine = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    xsecond = np.arange(df2['Year'].min(),2051,1)
    ysecond = xsecond*secondLine.slope + secondLine.intercept   
    plt.plot(xsecond,ysecond)
    
    # Add labels and title
    plt.xlabel('Year');
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()