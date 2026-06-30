# ============================================================
# CodeAlpha Data Analytics Internship
# Task 2: Exploratory Data Analysis (EDA)
# Dataset: Students Performance in Exams
# Analyst: Abubakar Abdulahi Olayinka
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# SECTION 1: LOAD DATASET
# ============================================================

df = pd.read_csv('data/StudentsPerformance.csv')

# ============================================================
# SECTION 2: BASIC OVERVIEW
# ============================================================

print("=" * 60)
print("STUDENTS PERFORMANCE — EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\n--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values ---")
print(df.isnull().sum())

# ============================================================
# SECTION 3: DESCRIPTIVE STATISTICS
# ============================================================

print("\n--- Descriptive Statistics (Numerical Columns) ---")
print(df.describe().round(2))

# ============================================================
# SECTION 4: CATEGORICAL VARIABLE DISTRIBUTIONS
# ============================================================

print("\n--- Gender Distribution ---")
print(df['gender'].value_counts())

print("\n--- Parental Level of Education ---")
print(df['parental level of education'].value_counts())

print("\n--- Test Preparation Course ---")
print(df['test preparation course'].value_counts())

# ============================================================
# SECTION 5: AVERAGE SCORES BY GROUP
# ============================================================

print("\n--- Average Scores by Gender ---")
print(df.groupby('gender')[['math score',
                             'reading score',
                             'writing score']].mean().round(2))

print("\n--- Average Scores by Test Preparation ---")
print(df.groupby('test preparation course')[['math score',
                                              'reading score',
                                              'writing score']].mean().round(2))

print("\n--- Average Scores by Parental Education ---")
print(df.groupby('parental level of education')[['math score',
                                                  'reading score',
                                                  'writing score']].mean().round(2))

# ============================================================
# SECTION 6: CORRELATION ANALYSIS
# ============================================================

print("\n--- Correlation Matrix ---")
correlation = df[['math score',
                   'reading score',
                   'writing score']].corr().round(2)
print(correlation)

# ============================================================
# SECTION 7: SCORE DISTRIBUTION SUMMARY
# ============================================================

print("\n--- Score Range Summary ---")
for col in ['math score', 'reading score', 'writing score']:
    print(f"\n{col.upper()}")
    print(f"  Minimum  : {df[col].min()}")
    print(f"  Maximum  : {df[col].max()}")
    print(f"  Mean     : {df[col].mean():.2f}")
    print(f"  Median   : {df[col].median()}")
    print(f"  Std Dev  : {df[col].std():.2f}")

print("\n" + "=" * 60)
print("EDA COMPLETE — READY FOR VISUALISATION (TASK 3)")
print("=" * 60)
