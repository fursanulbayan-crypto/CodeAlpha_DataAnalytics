# ============================================================
# CodeAlpha Data Analytics Internship
# Task 3: Data Visualisation
# Dataset: Students Performance in Exams
# Analyst: Abubakar Abdulahi Olayinka
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ============================================================
# SETUP
# ============================================================

df = pd.read_csv('data/StudentsPerformance.csv')

# Create output folder for saving charts
os.makedirs('visualisations', exist_ok=True)

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

print("Dataset loaded successfully. Generating visualisations...")

# ============================================================
# CHART 1: Distribution of Math Scores
# ============================================================

plt.figure()
sns.histplot(df['math score'], bins=20, kde=True, color='steelblue')
plt.title('Distribution of Math Scores', fontsize=14, fontweight='bold')
plt.xlabel('Math Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('visualisations/chart1_math_score_distribution.png')
plt.close()
print("Chart 1 saved — Math Score Distribution")

# ============================================================
# CHART 2: Distribution of Reading and Writing Scores
# ============================================================

fig, axes = plt.subplots(1, 2)
sns.histplot(df['reading score'], bins=20,
             kde=True, color='seagreen', ax=axes[0])
axes[0].set_title('Reading Score Distribution',
                   fontsize=12, fontweight='bold')
axes[0].set_xlabel('Reading Score')
axes[0].set_ylabel('Number of Students')

sns.histplot(df['writing score'], bins=20,
             kde=True, color='coral', ax=axes[1])
axes[1].set_title('Writing Score Distribution',
                   fontsize=12, fontweight='bold')
axes[1].set_xlabel('Writing Score')
axes[1].set_ylabel('Number of Students')

plt.tight_layout()
plt.savefig('visualisations/chart2_reading_writing_distribution.png')
plt.close()
print("Chart 2 saved — Reading and Writing Distribution")

# ============================================================
# CHART 3: Average Scores by Gender
# ============================================================

gender_scores = df.groupby('gender')[['math score',
                                       'reading score',
                                       'writing score']].mean().round(2)
gender_scores.plot(kind='bar', colormap='Set2', edgecolor='black')
plt.title('Average Scores by Gender', fontsize=14, fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.legend(title='Subject')
plt.tight_layout()
plt.savefig('visualisations/chart3_scores_by_gender.png')
plt.close()
print("Chart 3 saved — Average Scores by Gender")

# ============================================================
# CHART 4: Impact of Test Preparation on Scores
# ============================================================

prep_scores = df.groupby('test preparation course')[['math score',
                                                       'reading score',
                                                       'writing score']].mean().round(2)
prep_scores.plot(kind='bar', colormap='Set1', edgecolor='black')
plt.title('Impact of Test Preparation Course on Scores',
          fontsize=14, fontweight='bold')
plt.xlabel('Test Preparation Course')
plt.ylabel('Average Score')
plt.xticks(rotation=0)
plt.legend(title='Subject')
plt.tight_layout()
plt.savefig('visualisations/chart4_test_preparation_impact.png')
plt.close()
print("Chart 4 saved — Test Preparation Impact")

# ============================================================
# CHART 5: Scores by Parental Level of Education
# ============================================================

parental_scores = df.groupby(
    'parental level of education')[['math score',
                                    'reading score',
                                    'writing score']].mean().round(2)
parental_scores.plot(kind='barh', colormap='coolwarm', edgecolor='black')
plt.title('Average Scores by Parental Level of Education',
          fontsize=14, fontweight='bold')
plt.xlabel('Average Score')
plt.ylabel('Parental Education Level')
plt.legend(title='Subject')
plt.tight_layout()
plt.savefig('visualisations/chart5_parental_education_impact.png')
plt.close()
print("Chart 5 saved — Parental Education Impact")

# ============================================================
# CHART 6: Correlation Heatmap
# ============================================================

plt.figure()
corr_matrix = df[['math score',
                   'reading score',
                   'writing score']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu',
            fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Subject Scores',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualisations/chart6_correlation_heatmap.png')
plt.close()
print("Chart 6 saved — Correlation Heatmap")

# ============================================================
# CHART 7: Boxplot — Score Spread by Gender
# ============================================================

fig, axes = plt.subplots(1, 3)
subjects = ['math score', 'reading score', 'writing score']
colours = ['steelblue', 'seagreen', 'coral']

for i, (subject, colour) in enumerate(zip(subjects, colours)):
    sns.boxplot(data=df, x='gender', y=subject,
                color=colour, ax=axes[i])
    axes[i].set_title(subject.title(),
                      fontsize=11, fontweight='bold')
    axes[i].set_xlabel('Gender')
    axes[i].set_ylabel('Score')

plt.suptitle('Score Distribution by Gender',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualisations/chart7_boxplot_gender.png')
plt.close()
print("Chart 7 saved — Boxplot Score Distribution by Gender")

# ============================================================
# CHART 8: Scatter Plot — Math vs Reading Scores
# ============================================================0000

plt.figure()
sns.scatterplot(data=df, x='math score', y='reading score',
                hue='gender', alpha=0.6, palette='Set1')
plt.title('Math Score vs Reading Score by Gender',
          fontsize=14, fontweight='bold')
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.legend(title='Gender')
plt.tight_layout()
plt.savefig('visualisations/chart8_math_vs_reading.png')
plt.close()
print("Chart 8 saved — Math vs Reading Scatter Plot")

# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("ALL 8 VISUALISATIONS SAVED TO 'visualisations' FOLDER")
print("=" * 60)