# Lecture 6 bokeh plot

![alt text](image-1.png)

```python
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, FactorRange, ColumnDataSource, HoverTool, Legend
from bokeh.palettes import Category10, Spectral10
from bokeh.plotting import figure, show
from bokeh.io import output_notebook, save, output_file

file_path = r'G:\My Drive\Skole\DTU\8. semester\Social_data_viz\Data\2003_to_present.csv'
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Filter data for 2014-2024
filtered_df = df[(df['Year'] >= 2014) & (df['Year'] <= 2024)]

# List of focus crimes
focuscrimes = ['DRUG/NARCOTIC', 'LARCENY/THEFT', 'VANDALISM', 'ASSAULT', 'BATTERY', 'ROBBERY', 'WEAPONS VIOLATION']

# Group by TimeOfDay and count occurrences
hourly_crimes = filtered_df.groupby(['TimeOfDay', 'Category']).size().reset_index(name='Count')

# Sort by TimeOfDay to ensure chronological order
hourly_crimes = hourly_crimes.sort_values('TimeOfDay')


# The resulting hourly_crimes DataFrame will have:
# - TimeOfDay (0-23)
# - Count (number of crimes in each hour)
# - Percentage (percentage of crimes in each hour)

hourly_crimes = hourly_crimes.pivot_table(index='TimeOfDay', columns='Category', values='Count', aggfunc='sum')

# Calculate normalized data
normalized_crimes = hourly_crimes.copy()
for column in normalized_crimes.columns:
    normalized_crimes[column] = normalized_crimes[column] / normalized_crimes[column].sum()

# Sort crimes by their maximum hourly percentage (descending to plot largest first)
max_percentages = (normalized_crimes * 100).max()
crimes = max_percentages.sort_values(ascending=False).index.tolist()

# Prepare the data
source = ColumnDataSource(data=dict(
    hours=list(range(24)),
    **{crime: normalized_crimes[crime].values * 100 for crime in crimes}
))

# Set up the figure
p = figure(
    width=1500, 
    height=600, 
    title="Distribution of Crimes by Hour of Day (Normalized)",
    x_axis_label="Hour of Day (24-hour format)",
    y_axis_label="Percentage of Incidents (%)",
    toolbar_location="above"
)

# Create the bars (largest to smallest, so smaller ones appear on top)
for i, crime in enumerate(reversed(crimes)):
    p.vbar(
        x='hours',
        width=0.9,
        top=crime,
        bottom=0,  # All bars start from 0
        source=source,
        color=Spectral10[i],
        alpha=0.5,  # Make them slightly transparent
        legend_label=crime,
        name=crime
    )

# Configure the legend
p.legend.click_policy = "hide"
p.legend.location = "left" #or 'bottom_left' depending on your preference
p.add_layout(p.legend[0], 'left') # Place the legend outside the plot area, above it. Alternatively use 'below', 'left', or 'right'

# Add hover tool
hover = HoverTool()
hover.tooltips = [
    ("Hour", "@hours:00"),
    *[(crime, f"@{{{crime}}}{' %'}") for crime in crimes]
]
p.add_tools(hover)

# Style the plot
p.xaxis.major_label_orientation = "horizontal"
p.xgrid.grid_line_alpha = 0.3
p.ygrid.grid_line_alpha = 0.3
p.y_range.start = 0

# Configure x-axis to show all hours
p.xaxis.ticker = list(range(24))
p.xaxis.major_label_overrides = {i: f"{i}" for i in range(24)}

# Save the plot to an HTML file
output_file("crime_distribution.html")
save(p)

# Show the plot
show(p)
```