import pandas as pd

# Specify the path to the file in your Downloads folder
file_path = r"C:\Users\rgvil\Downloads\bina\srf_data.csv"

# Load the CSV file from the specified path
df = pd.read_csv(file_path, encoding = 'utf8')

# Define a function to determine the value for the "Geschlecht" column
def determine_geschlecht(row):
    sendung = str(row["Sendung"])
    untertitel = str(row["Untertitel"])

    mixed_keywords = {"Männer und Frauen", "MÄNNER UND FRAUEN", "Frauen und Männer", "FRAUEN UND MÄNNER", "MIXED",
                      "mixed", "Mixed-Staffel", "Mixed"}
    maenner_keywords = {"Männer", "MÄNNER"}
    frauen_keywords = {"Frauen", "FRAUEN"}

    if any(keyword in sendung or keyword in untertitel for keyword in mixed_keywords):
        return "Mixed"
    elif any(keyword in sendung or keyword in untertitel for keyword in maenner_keywords):
        return "Männer"
    elif any(keyword in sendung or keyword in untertitel for keyword in frauen_keywords):
        return "Frauen"
    else:
        return "Unknown"

# Apply the function to each row in the DataFrame
df["Geschlecht"] = df.apply(determine_geschlecht, axis=1)

# Save the modified DataFrame back to a CSV file in the same location
download_file_path = r"C:\Users\rgvil\Downloads\bina\srf_data_with_gender.csv"
df.to_csv(download_file_path, index=False, encoding='utf-8-sig')
