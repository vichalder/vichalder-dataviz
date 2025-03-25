Here, you can see how the number of crimes in each category evolve over the course of a year.

![alt text](image.png)


## The code:

```python
# Calculate number of rows needed (half of total crimes, rounded up)
n_rows = (len(focuscrimes) + 1) // 2
n_cols = 2

# Create a figure with subplots in 2 columns
fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 4*n_rows))

# Flatten axes array to make it easier to iterate over
axes_flat = axes.flatten()

# Plot data for each crime type
for i, crime in enumerate(focuscrimes):
    # Get data for this crime type
    crime_data = focus_df[focus_df['Category'] == crime]
    monthly_counts = crime_data.groupby(crime_data['Date'].dt.month)['PdId'].count()
    
    # Create the subplot
    axes_flat[i].bar(monthly_counts.index, monthly_counts.values)
    axes_flat[i].set_title(f'Number of {crime.title()} Incidents per month')
    axes_flat[i].set_xlabel('Month')
    axes_flat[i].set_ylabel('Number of Incidents')
    axes_flat[i].grid(True, alpha=0.3)
    
    # Add some padding to the y-axis
    if len(monthly_counts) > 0:
        ymax = monthly_counts.max()
        axes_flat[i].set_ylim(0, ymax * 1.1)
    
    # Rotate x-axis labels for better readability
    axes_flat[i].tick_params(axis='x', rotation=45)

# Hide any empty subplots if number of crimes is odd
if len(focuscrimes) % 2 != 0:
    axes_flat[-1].set_visible(False)

plt.tight_layout()
plt.show()
```

