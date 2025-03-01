import pandas as pd

# Load the original CSV file
df = pd.read_csv('c:/Users/hi/Desktop/project/ecg.csv/ecg.csv', header=None)

# Extract the first row
first_row = df.iloc[0, :]

# Create a new DataFrame with the first row
first_row_df = pd.DataFrame(first_row).transpose()

# Save the new DataFrame to a CSV file
first_row_df.to_csv('c:/Users/hi/Desktop/project/ecg.csv/csv_new.csv', index=False, header=False)

# Load the CSV file with the single row
df = pd.read_csv('c:/Users/hi/Desktop/project/ecg.csv/csv_new.csv', header=None)

# Transpose the DataFrame to convert the row into a column
df_transposed = df.transpose()

# Rename the column to 'ECG'
df_transposed.columns = ['ECG']

# Save the transposed DataFrame to a new CSV file
df_transposed.to_csv('c:/Users/hi/Desktop/project/ecg.csv/csv_column.csv', index=False)