import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Sea Level Changes Over Time')
    plt.savefig('bar_plot.png')
    return plt

    # Create first line of best fit
    
    res = stats.linregress(x, y)

    plt.scatter(x, y, label='Original Data')
    plt.plot(x, res.intercept + res.slope * x, 'r', label=f'Fitted Line (slope={res.slope:.2f})')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('Sea Level Changes Over Time')

    # Add legend
    plt.legend()

    # Show plot
    plt.show()

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()