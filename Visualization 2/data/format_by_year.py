import pandas as pd

# Load the original CSV file
input_file = 'Tourist_Arrivals_Formatted.csv'  
output_file = 'Tourist_Arrivals_By_Year.csv'

# Read the CSV file
data = pd.read_csv(input_file)

# Extract the year from the 'Month' column and create a new 'Year' column
data['Year'] = data['Month'].apply(lambda x: int("20" + x[-2:]))  # Converts "Jan-19" to "2019"

# Aggregate the data by 'Year' and 'Country' and calculate the total arrivals
data_grouped = data.groupby(['Year', 'Country'])['Arrivals'].sum().reset_index()

# Save the reformatted CSV file
data_grouped.to_csv(output_file, index=False)

print(f'Reformatted CSV saved to {output_file}')
