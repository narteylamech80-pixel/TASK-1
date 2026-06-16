import pandas as pd
import glob
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(BASE_DIR, "data")

data_files = glob.glob(os.path.join(data_path, "*.csv")) + \
             glob.glob(os.path.join(data_path, "*.xlsx"))


def read_file ():
    dfs = []
    filenames = []
    for file in data_files:
        if file.endswith(".xlsx"): 
            df = pd.read_excel(file)
        else: 
            df = pd.read_csv(file)
        dfs.append(df)
        filenames.append(file)
    return dfs, filenames
    

###################################################################################




def clean_dataset(dfs):

    print("\n📥 Loading data...")

    cleaned_dfs = []

    for i, df in enumerate(dfs):
        print("🔍 BASIC INFO")
        print("-" * 50)
        print(df.info())

        print("\n📊 DESCRIPTIVE STATISTICS")
        print("-" * 50)
        print(df.describe(include='all'))

        # 1. Identify missing values
        print("Missing values per column:\n", df.isnull().sum())

        # Handle missing values (example strategies)
        df = df.dropna(how='all')  # remove rows where all values are missing

        
        #2. Count duplicate rows
        print("\n🔁 DUPLICATE ROWS")
        print("-" * 50)
        duplicate_count = df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicate_count}") 

        # Remove duplicate rows
        df = df.drop_duplicates()


        # 3. Standardize text values (example for object columns)
        for col in df.select_dtypes(include=['object', 'string']).columns:
            df[col] = df[col].str.strip().str.lower()

        # Optional: specific replacements (customize as needed)
        if 'gender' in df.columns:
            df['gender'] = df['gender'].replace({
                'm': 'male',
                'f': 'female'
            })

        # 4. Convert date columns to consistent format
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
                

        # 5. Rename column headers (lowercase, no spaces)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        # 6. Fix data types
        if 'age' in df.columns:
            df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

        # Convert all numeric-like columns properly
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col])
                except:
                    pass

        print("\n👌Data cleaning complete.")

        cleaned_dfs.append(df)
    return cleaned_dfs



dfs, filenames = read_file()
cleaned = clean_dataset(dfs)

for df, file in zip(cleaned, filenames):
    
    # Extract filename only (no folder path)
    base = os.path.basename(file)
    
    # Split name and extension
    name, ext = os.path.splitext(base)
    
    # Create new filename
    new_name = f"{name}_cleaned{ext}"
    
    # Save file 
    if ext.lower() == ".xlsx":
        df.to_excel(new_name, index=False)
    else:
        df.to_csv(new_name, index=False)    



