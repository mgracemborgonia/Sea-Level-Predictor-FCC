import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    x_year = df["Year"]
    y_sea_level = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x_year,y_sea_level,color = 'b')
    
    # Create first line of best fit
    res = linregress(x_year,y_sea_level)
    x1 = pd.Series([i for i in range(1880,2051)])
    y1 = res.slope * x1 + res.intercept
    plt.plot(x1,y1,color = 'r')
    
    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000]
    new_df_year = df2["Year"]
    new_df_sea_level = df2["CSIRO Adjusted Sea Level"]
    new_res = linregress(new_df_year,new_df_sea_level)
    x2 = pd.Series([i for i in range(2000,2051)])
    y2 = new_res.slope * x2 + new_res.intercept
    plt.plot(x2,y2,color = 'g')
    
    # Add labels and title
    plt.title("Rise in Sea Level", fontdict = {"size": 20})
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
