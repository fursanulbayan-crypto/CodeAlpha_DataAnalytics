import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
pd.set_option('display.max_columns', None)
df = pd.read_csv("data/StudentPerformanceFactors.csv")
df = df.dropna()
os.makedirs('visualisations_round2', exist_ok=True)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Attendance', y='Exam_Score',
                alpha=0.4, color='steelblue')
plt.title('Attendance vs Exam Score (r = 0.58)',
          fontsize=14, fontweight='bold')
plt.xlabel('Attendance (%)')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('visualisations_round2/chart1_attendance_vs_exam.png')
plt.close()
print("Chart 1 saved — Attendance vs Exam Score")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Hours_Studied', y='Exam_Score',
                alpha=0.4, color='seagreen')
plt.title('Hours Studied vs Exam Score (r = 0.45)',
          fontsize=14, fontweight='bold')
plt.xlabel('Hours Studied Per Week')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('visualisations_round2/chart2_hours_studied_vs_exam.png')
plt.close()
print("Chart 2 saved — Hours Studied vs Exam Score")
parental_means = df.groupby(
    'Parental_Involvement')['Exam_Score'].mean().round(2)
parental_means.plot(kind='bar',
                    color=['coral', 'steelblue', 'seagreen'],
                    edgecolor='black')
plt.title('Mean Exam Score by Parental Involvement',
          fontsize=14, fontweight='bold')
plt.xlabel('Parental Involvement Level')
plt.ylabel('Mean Exam Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('visualisations_round2/chart3_parental_involvement.png')
plt.close()
print("Chart 3 saved — Parental Involvement")
plt.figure(figsize=(10, 6))
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd',
            fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap — Numerical Variables',
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('visualisations_round2/chart4_correlation_heatmap.png')
plt.close()
print("Chart 4 saved — Correlation Heatmap")
plt.figure(figsize=(10, 6))
sns.histplot(df['Exam_Score'], bins=20,
             kde=True, color='steelblue')
plt.title('Distribution of Exam Scores',
          fontsize=14, fontweight='bold')
plt.xlabel('Exam Score')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig('visualisations_round2/chart5_exam_score_distribution.png')
plt.close()
print("Chart 5 saved — Exam Score Distribution")
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Motivation_Level',
            y='Exam_Score',
            order=['Low', 'Medium', 'High'],
            palette='Set2')
plt.title('Exam Score Distribution by Motivation Level',
          fontsize=14, fontweight='bold')
plt.xlabel('Motivation Level')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('visualisations_round2/chart6_motivation_boxplot.png')
plt.close()
print("Chart 6 saved — Motivation Level Boxplot")
income_means = df.groupby(
    'Family_Income')['Exam_Score'].mean().round(2)
income_means = income_means.reindex(['Low', 'Medium', 'High'])
income_means.plot(kind='bar',
                  color=['coral', 'steelblue', 'seagreen'],
                  edgecolor='black')
plt.title('Mean Exam Score by Family Income Level',
          fontsize=14, fontweight='bold')
plt.xlabel('Family Income Level')
plt.ylabel('Mean Exam Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('visualisations_round2/chart7_family_income.png')
plt.close()
print("Chart 7 saved — Family Income")
peer_means = df.groupby(
    'Peer_Influence')['Exam_Score'].mean().round(2)
peer_means = peer_means.reindex(['Negative', 'Neutral', 'Positive'])
peer_means.plot(kind='bar',
                color=['coral', 'steelblue', 'seagreen'],
                edgecolor='black')
plt.title('Mean Exam Score by Peer Influence',
          fontsize=14, fontweight='bold')
plt.xlabel('Peer Influence')
plt.ylabel('Mean Exam Score')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('visualisations_round2/chart8_peer_influence.png')
plt.close()
print("Chart 8 saved — Peer Influence")
print("\n" + "=" * 60)
print("ALL 8 CHARTS SAVED TO 'visualisations_round2' FOLDER")
print("=" * 60)