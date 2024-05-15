import pandas as pd

# Define the list of words to check in the "Untertitel" column
words_list = ["IGA", "ARYNA", "COCO", "ELENA", "JESSICA", "ONS", "QINWEN", "MARKETA", "MARIA", "JELENA", "DARIA", "KAROLINA", "MAIA", "JASMINE", "LIUDMILA", "EKATERINA", "ELINA", "MADISON", "VERONIKA", "EMMA", "BARBORA", "ANASTASIA", "PETRA", "SORANA", "ANNA", "MARTA", "CAROLINE", "ELISE", "ANASTASIA", "KATIE", "LINDA", "VICTORIA", "DAYANA", "DONNA", "LEYLAH", "ANHELINA", "YUE", "MIRRA", "MARIE", "LESIA", "SLOANE", "KATERINA", "XINYU", "ANNA", "CLARA", "KAROLINA", "MAGDALENA", "TATJANA", "LUCIA", "CAROLINE", "ELISABETTA", "TORMO", "DANIELLE", "DIANE", "MAGDA", "XIYU", "ARANTXA", "SOFIA", "BELINDA", "PETRA", "MARTINA", "DIANA", "LIN", "YAFAN", "ELINA", "ANA", "PEYTON", "YULIA", "ANNA", "MAYAR", "VIKTORIJA", "TAYLOR", "VIKTORIYA", "CRISTINA", "ASHLYN", "NAO", "TAMARA", "NADIA", "GREET", "PAULA", "BERNARDA", "JAQUELINE", "VARVARA", "OCEANE", "JODIE", "KAYLA", "ZHUOXUAN", "YANINA", "HARRIET", "CAMILA", "LAURA", "CLARA", "REBEKA", "ERIKA", "KAMILLA", "HAILEY", "SARA", "ARINA", "ALIZÉ", "MARIA", "MARIA", "RENATA", "ALIAKSANDRA", "EMINA", "BRENDA", "MAI", "RIBERA", "CAMILA", "DARJA", "ANNA", "JULIA", "JULE", "KAJA", "CLAIRE", "DARIA", "LAURA", "REBECCA", "TAMARA", "JULIA", "MCCARTNEY", "KATIE", "STORM", "EMILIANA", "ALYCIA", "ELIZABETH", "IRINA-CAMELIA", "MANEIRO", "DIAZ", "CAROLINE", "SARA", "SACHIA", "DARIA", "OLGA", "TAYLAH", "ASTRA", "LEOLIA", "YULIIA", "FIONA", "LINDA", "ARIANNE", "ANASTASIA", "JESSIKA", "HEATHER", "DALMA", "TEREZA", "EVA", "CELINE", "REBECCA", "OLIVIA", "ALINA", "MOYUKA", "ELLA", "LUCREZIA", "CHLOE", "LULU", "SUZAN", "ELSA", "BIANCA", "JANA", "PANNA", "EKATERINA", "TABORDA", "ANN", "YURIKO", "LAUREN", "ANNA-LENA", "ANASTASIA", "VALERIA", "KIMBERLY", "ELENA-GABRIELA", "ALEXANDRA", "ZEYNEP", "KATERYNA", "IRINA", "VIKTORIA", "NATALIJA", "SOLANA", "KATHERINE", "KATARINA", "SINJA", "SIMONA", "TIMEA", "ROBIN", "VERONIKA", "AKUGUE", "MADISON", "MIRIAM", "HIMENO", "KATARZYNA", "GABRIELA", "PRISCILLA", "POLINA", "FRANCISCA", "CAROLE", "DESTANEE", "YE-XIN", "ANTONIA", "ALIONA", "JULIA", "IRYNA", "PETRA", "TENA", "DOMINIKA", "MIRJAM", "TALIA", "BAGARIC", "RALUKA", "YA", "JIL", "DALILA", "CAROL", "POLONA", "ANDREEA", "SU", "ELVINA", "MARINA", "VALENTINI", "KAIA", "AJLA", "HARMONY", "LEA", "IPEK", "XIAODI", "JUSTINA", "ANCA", "CRISTINA", "JENNIFER", "NAOMI", "DEJANA", "SIJIA", "YLENA", "SELENA", "DARYA", "YULIYA", "SOFYA", "CATY", "ALICE", "LINA", "XINYU", "DANKA", "ANKITA", "NURIA", "NIKOLA", "GERGANA", "SARA", "MANANCHAYA", "JANA", "TATIANA", "NIGINA", "HANNA", "VALERIYA", "ZULETA", "AMANDA", "JAIMEE", "SONAY", "MAKENNA", "MARGAUX", "ESCORIHUELA", "DESPINA", "CIREZ", "ISABELLA", "LOUISA", "STACEY", "VARVARA", "KRISTINA", "VALENTINA", "VERA", "HARUKA", "FRANCESCA", "SEONE", "SILVIA", "LIV", "AMARNI", "MARIA", "GORMAZ", "DEICHMANN", "LANLANA", "FANNY", "SAPFO", "ANA", "KERKHOVE", "MADDISON", "MONA", "MANON", "SOFIA", "GRACE", "EMMA", "AOI", "ELENA", "JULIE", "HANNE", "LOIS", "SOHYUN", "EN-SHUO", "MAJA", "LINDA", "GIORGIA", "REBECCA", "EUGENIE"]
# Convert the list to lowercase
words_list = [word.lower() for word in words_list]


download_file_path = r"C:\Users\rgvil\Downloads\bina\srf_data_with_gender.csv"
# Load the CSV file into a DataFrame
df = pd.read_csv(download_file_path)

# Function to check if any word in the list is in the "Untertitel" column
def check_words(untertitel):
    # Splitting the text into separate strings to compare each word
    for word in untertitel.lower().split():
        if word in words_list:
            return "Frauen"
    return "Männer"

# Apply the function to each row where "Sportart" is "Tennis"
# and update the "Geschlecht" column based on the condition
df.loc[df['Sportart'] == 'Tennis', 'Geschlecht'] = df[df['Sportart'] == 'Tennis']['Untertitel'].apply(check_words)

# Save the modified DataFrame back to a new CSV file
download_file_path = r"C:\Users\rgvil\Downloads\bina\srf_data_with_gender_tennis_cleaned.csv"
df.to_csv(download_file_path, index=False, encoding='utf-8-sig')



