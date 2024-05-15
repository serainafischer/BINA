import pandas as pd

download_file_path = r"C:\Users\rgvil\Downloads\bina\srf_data_manual_clean.csv"
# Load the CSV file into a DataFrame
df = pd.read_csv(download_file_path)

# Split the "Datum" column into three new columns: "Tag", "Monat", and "Jahr"
df[['Tag', 'Monat', 'Jahr']] = df['Datum'].str.split('-', expand=True)

# Save the modified DataFrame to a new CSV file with BOM encoding in the specified path
output_path = r'C:\Users\rgvil\Downloads\bina\srf_data_split_date.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig')
