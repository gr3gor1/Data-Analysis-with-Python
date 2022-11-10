import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(12,6))
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    
    ax = plt.plot(df.index.tolist(),df['value'])
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dfc = df.copy()
    dfc['Time'] = pd.to_datetime(dfc.index.values)

    dfc['month'] = dfc['Time'].apply(lambda x: x.month_name())
    dfc['year'] = dfc['Time'].apply(lambda x: x.year)
 
    # Draw bar plot
    dfc = dfc.groupby([dfc.year,dfc.month],as_index=False,sort=False)['value'].mean()
    padding = {
      'year': [2016, 2016, 2016, 2016],
        "month": ['January', 'February', 'March', 'April'],
        "value": [0, 0, 0, 0]
    }
    temp = pd.DataFrame(padding)
    dfc = pd.concat([temp,dfc])
    #print(dfc)
    
    fig, ax =plt.subplots(figsize=(12,6))
    #dfc['year'] = dfc['year'].astype(str)
    #dfc = dfc.groupby(['year'],group_keys=True)
    #dfc = dfc.apply(lambda x: x)
    ax = sns.barplot(data=dfc,x='year',y='value',hue='month')
    plt.title('Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views') 
    #plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1,ax2) = plt.subplots(2,figsize=(12,6))

    plt.subplot(1,2,1)
    ax1 = sns.boxplot(data=df_box,x='year',y='value')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1,2,2)
    lista=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    ax2 = sns.boxplot(data=df_box,x='month',y='value',order=lista)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.ylabel('Page Views')
    plt.xlabel('Month')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
