import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    
  
    # Create scatter plot
    plt.figure()
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])  

    # Create first line of best fit
    df1=df.copy()
    slope1, intercept1, r, p, se = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    latest_year=df1['Year'].max()
    for i in range(latest_year+1,2051):
      df1=df1._append({'Year':i}, ignore_index=True)
      
    plt.plot(df1['Year'],(slope1*df1['Year'])+intercept1,c='k')

    # Create second line of best fit
    df_new=df.loc[(df['Year']>=2000) & (df['Year']<=latest_year)]
    slope2, intercept2, r, p, se = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    for i in range(latest_year+1,2051):
      df_new=df_new._append({'Year':i}, ignore_index=True)
    plt.plot(df_new['Year'],(slope2*df_new['Year'])+intercept2,c='k')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()