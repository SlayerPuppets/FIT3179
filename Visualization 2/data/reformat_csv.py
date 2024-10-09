import pandas as pd

# Load the original CSV file with rows representing months and columns representing countries
file_path = 'Tourist Arrivals.csv'  # Replace with your file path
output_file = 'Tourist_Arrivals_Formatted.csv'

# Read the CSV file
data = pd.read_csv(file_path)

# Remove "Total" row if present
data = data[data['Month'] != 'Total']

# Melt the dataframe to convert columns into rows
formatted_data = data.melt(id_vars=['Month'], var_name='Country', value_name='Arrivals')

# Remove any rows where 'Arrivals' is NaN or 0 if necessary
formatted_data = formatted_data.dropna(subset=['Arrivals'])
formatted_data = formatted_data[formatted_data['Arrivals'] != 0]

# Save to a new CSV file
formatted_data.to_csv(output_file, index=False)

print(f'Reformatted CSV saved to {output_file}')
