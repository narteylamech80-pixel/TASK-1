# 📊 Data Cleaning Pipeline

## 🧠 Overview

This project provides an automated **data cleaning pipeline** using Python and pandas. It is designed to load multiple datasets, perform exploratory data analysis (EDA), clean the data, and save cleaned versions of the files.

The script supports both **CSV** and **Excel (.xlsx)** file formats.

---

## 📁 Project Structure

```
project_folder/
│
├── data/                  # Folder containing raw datasets
├── main.py                # Main script
├── README.md              # Project documentation
```

---

## ⚙️ Features

### 📥 Data Loading

* Automatically detects and loads:

  * `.csv` files
  * `.xlsx` files
* Reads all datasets from the `data/` folder

---

### 🔍 Exploratory Data Analysis (EDA)

For each dataset, the script:

* Displays dataset structure (`info()`)
* Shows descriptive statistics (`describe()`)
* Counts missing values
* Identifies duplicate rows

---

### 🧹 Data Cleaning Steps

1. **Remove Empty Rows**

   * Drops rows where all values are missing

2. **Handle Duplicates**

   * Counts and removes duplicate rows

3. **Standardize Text Data**

   * Converts text to lowercase
   * Removes leading/trailing spaces

4. **Normalize Categorical Values**

   * Example:

     * `m → male`
     * `f → female`

5. **Date Formatting**

   * Automatically converts columns containing `"date"` into datetime format

6. **Column Renaming**

   * Converts column names to:

     * lowercase
     * underscores instead of spaces

7. **Data Type Fixing**

   * Converts:

     * `age` → numeric (nullable integer)
     * other numeric-like columns → proper numeric types

---

## 💾 Output

* Cleaned files are saved in the **same directory as the script**
* File naming format:

```
originalfilename_cleaned.csv
originalfilename_cleaned.xlsx
```

---

## ▶️ How to Run

1. Place your datasets inside the `data/` folder

2. Run the script:

```bash
python main.py
```

3. Cleaned files will be generated automatically

---

## 📦 Dependencies

Make sure you have the following installed:

```bash
pip install pandas openpyxl os
```

---

## 🚀 Example Workflow

1. Add raw dataset:

```
data/patient_data.csv
```

2. Run script

3. Output generated:

```
patient_data_cleaned.csv
```

---

## ⚠️ Notes

* The script assumes:

  * Column names like `age`, `gender`, or containing `date`
* Non-numeric values in numeric columns are safely handled using coercion
* Future pandas compatibility is maintained (supports `object` and `string` dtypes)

---

## 🛠️ Future Improvements

* Add visualization (EDA plots)
* Integrate machine learning pipeline
* Add logging instead of print statements
* Export summary reports

---

## 👨‍💻 Author

Developed as part of a **Data Analyst Internship Task**.

---
