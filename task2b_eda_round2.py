# ============================================================
# CodeAlpha Data Analytics Internship
# Task 2: Exploratory Data Analysis — Round Two
# Dataset: Student Performance Factors (6,607 records)
# Analyst: Abubakar Abdulahi Olayinka
# Institution: Al-Mafaazat Arabic and Islamic Training Centre
# ============================================================

# --- Import Libraries ---
# pandas: handles all data loading, cleaning, and analysis
# os: use0d to verify file contents in the data directory
import pandas as pd
import os

# --- Display Settings ---
# Remove column and width limits so full output prints in terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ============================================================
# SECTION 1: LOAD DATASET
# ============================================================

# Read the CSV file from the data folder into a pandas DataFrame
# df is the standard abbreviation for DataFrame — used universally
df = pd.read_csv("data/StudentPerformanceFactors.csv")

# Verify files present in data directory
print("Files in data folder:", os.listdir("data"))

# Confirm dataset loaded correctly — should show (6607, 20)
print("\n--- Dataset Shape (Rows, Columns) ---")
print(df.shape)

# ============================================================
# SECTION 2: COLUMN INSPECTION
# ============================================================

# Print all 20 column names exactly as pandas reads them
# Spelling and capitalisation here must match all future references
print("\n--- Column Names ---")
print(df.columns.tolist())

# ============================================================
# SECTION 3: MISSING VALUE DETECTION
# ============================================================

# isnull() returns True for every empty cell
# .sum() counts those True values per column
# Result confirmed against prior Excel check:
# Teacher_Quality: 78, Parental_Education_Level: 90, Distance_from_Home: 67
print("\n--- Missing Values Per Column ---")
print(df.isnull().sum())

# ============================================================
# SECTION 4: DATA CLEANING
# ============================================================

# Decision: drop all rows containing any missing value
# Justification: affected columns are categorical — imputation
# would require assuming unknown categories, which is unreliable
# Loss: approximately 229 rows (3.6% of dataset)
df = df.dropna()

# Confirm cleaned dataset shape — should show (6378, 20)
print("\n--- Cleaned Dataset Shape ---")
print(df.shape)

# ============================================================
# SECTION 5: DESCRIPTIVE STATISTICS — NUMERICAL COLUMNS
# ============================================================

# df.describe() automatically computes count, mean, std,
# min, 25th percentile, median, 75th percentile, and max
# for every numerical column — equivalent to SPSS Descriptives table
print("\n--- Descriptive Statistics (Numerical Columns) ---")
print(df.describe().round(2))

# ============================================================
# SECTION 6: DESCRIPTIVE STATISTICS — CATEGORICAL COLUMNS
# ============================================================

# include='object' targets text-based columns only
# Returns count, unique categories, most frequent value, and its frequency
print("\n--- Descriptive Statistics (Categorical Columns) ---")
print(df.describe(include='object'))

# ============================================================
# SECTION 7: EXAM SCORE DISTRIBUTION
# ============================================================

# Check frequency of every unique exam score
# Identified anomaly: one student scored 101 (impossible value)
# Decision: retained — single record, negligible impact on analysis
print("\n--- Exam Score Value Counts ---")
print(df['Exam_Score'].value_counts().sort_index())

# ============================================================
# SECTION 8: GROUP COMPARISONS — MEAN EXAM SCORE BY CATEGORY
# ============================================================

# groupby() splits dataset by category, mean() computes
# average Exam_Score within each group
# Pattern: more favourable conditions consistently associate
# with higher scores across all variables

categorical_vars = [
    'Parental_Involvement',
    'Motivation_Level',
    'Internet_Access',
    'Teacher_Quality',
    'Parental_Education_Level',
    'Distance_from_Home',
    'School_Type',
    'Gender',
    'Access_to_Resources',
    'Extracurricular_Activities',
    'Peer_Influence',
    'Learning_Disabilities',
    'Family_Income'
]

print("\n--- Mean Exam Score by Categorical Variables ---")
for var in categorical_vars:
    print(f"\n{var}:")
    print(df.groupby(var)['Exam_Score'].mean().round(2))

# ============================================================
# SECTION 9: CORRELATION ANALYSIS
# ============================================================

# Pearson correlation between all numerical variables and Exam_Score
# Ranked from strongest positive to strongest negative
# Key findings:
# Attendance: r = 0.58 (strong positive)
# Hours_Studied: r = 0.45 (moderate positive)
# Sleep_Hours: r = -0.02 (negligible)
print("\n--- Correlation With Exam Score ---")
print(df.corr(numeric_only=True)['Exam_Score'].sort_values(
    ascending=False).round(2))

# ============================================================
# SECTION 10: EDA SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("EDA SUMMARY — STUDENT PERFORMANCE FACTORS")
print("=" * 60)
print(f"Total students analysed: {len(df)}")
print(f"Variables examined: {len(df.columns)}")
print(f"Mean Exam Score: {df['Exam_Score'].mean().round(2)}")
print(f"Strongest predictor: Attendance (r = 0.58)")
print(f"Second predictor: Hours Studied (r = 0.45)")
print(f"Largest group gap: Parental Education Level (1.08 marks)")
print("=" * 60)
print("\nEDA COMPLETE — READY FOR VISUALISATION (TASK 3)")