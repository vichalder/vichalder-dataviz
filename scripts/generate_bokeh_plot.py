import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, VBar, Legend, LegendItem
from bokeh.io import output_file, save

# Sample data (replace with actual data if needed)
data = {
    'hours': list(range(24)),
    'ASSAULT': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'BURGLARY': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1],
    'WEAPON LAWS': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2],
    'ROBBERY': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3],
    'STOLEN PROPERTY': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4],
    'VANDALISM': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5],
    'LARCENY/THEFT': [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6],
    'VEHICLE THEFT': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7],
    'DRUG/NARCOTIC': [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8],
    'PROSTITUTION': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

df = pd.DataFrame(data)

# Create a ColumnDataSource
source = ColumnDataSource(df)

# Create a new plot
p = figure(x_range=(0, 23), y_range=(0, 100), plot_width=800, plot_height=400, title="Incident Percentage by Hour of Day")

# Define colors
colors = ['#5e4fa2', '#3288bd', '#66c2a5', '#abdda4', '#e6f598', '#fee08b', '#fdae61', '#f46d43', '#d53e4f', '#9e0142']

# Add vertical bars for each category
for i, column in enumerate(df.columns[1:]):
    p.vbar(x='hours', top=column, width=0.9, source=source, color=colors[i], legend_label=column, alpha=0.5)

# Customize the plot
p.xaxis.axis_label = 'Hour of Day (24-hour format)'
p.yaxis.axis_label = 'Percentage of Incidents (%)'
p.legend.click_policy = 'hide'

# Output the plot to an HTML file
output_file('new_bokeh_plot.html')

# Save the plot
save(p)

# Show the plot
show(p)
