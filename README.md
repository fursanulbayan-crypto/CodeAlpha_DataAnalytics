# CodeAlpha Data Analytics Internship
## Exploratory Data Analysis & Data Visualisation
**Intern:** Abubakar Abdulahi Olayinka  
**Organisation:** CodeAlpha  
**Domain:** Data Analytics  
**Tools:** Python 3.14, Pandas, Matplotlib, Seaborn, PyCharm

---

## Overview

This repository contains my submission for the CodeAlpha Data 
Analytics Internship. I completed Tasks 2 and 3 from the 
internship task list — Exploratory Data Analysis (EDA) and 
Data Visualisation — across two separate datasets. The first 
dataset fulfilled the minimum internship requirement. The second 
was undertaken independently to deepen practical understanding 
of Python-based data analysis beyond the required submission.

---

## Repository Structure
CodeAlpha_DataAnalytics/
├── data/
│   ├── StudentsPerformance.csv
│   └── StudentPerformanceFactors.csv
├── visualisations/
├── visualisations_round2/
├── task2_eda.py
├── task3_visualisation.py
├── task2b_eda_round2.py
└── task3b_visualisation_round2.py
---

## ROUND 1 — Students Performance in Exams

### Dataset
- **Source:** Kaggle — spscientist/students-performance-in-exams
- **Records:** 1,000 students
- **Variables:** 8 (gender, parental education, test preparation,
  math score, reading score, writing score)
- **Missing Values:** None

### Key Findings — Round 1
- Students who completed test preparation consistently 
  outperformed those who did not across all three subjects
- Reading and Writing scores correlate more strongly with 
  each other than either does with Math
- Gender differences in scores were modest but directional

---

## ROUND 2 — Student Performance Factors

### Dataset
- **Source:** Kaggle — lainguyen123/student-performance-factors
- **Records:** 6,607 students (6,378 after cleaning)
- **Variables:** 20 across behavioural, environmental,
  and demographic categories
- **Missing Values:** Teacher_Quality (78), 
  Parental_Education_Level (90), Distance_from_Home (67)
- **Cleaning Decision:** Rows with missing values dropped

### Key Findings — Round 2

**Attendance is the strongest predictor** (r = 0.58), 
stronger than study hours or prior academic record.

**Hours Studied is the second strongest predictor** (r = 0.45).

**Sleep and Physical Activity show negligible correlation** 
with exam scores (r = -0.02 and r = 0.03 respectively).

**Parental Education drives the largest group gap** — 
postgraduate-educated parents' children score 1.08 marks 
higher on average than high-school-educated parents' children.

**Exam score distribution is positively skewed** — most 
students score between 60 and 70, with a thin tail of high 
performers above 80.

**Peer influence has measurable academic impact** — students 
with positive peer influence score 1.06 marks higher on 
average than those with negative peer influence.

---

## Tools and Libraries

| Tool | Purpose |
|---|---|
| Python 3.14 | Core programming language |
| Pandas | Data loading, cleaning, and analysis |
| Matplotlib | Chart generation and formatting |
| Seaborn | Statistical visualisation |
| PyCharm | Development environment |
| Microsoft Excel | Initial data inspection and blank-cell verification |

---

## Author

**Abubakar Abdulahi Olayinka**  
Educator | Islamic Studies Scholar | Data Analytics Intern  
Al-Mafaazat Arabic and Islamic Training Centre, Lagos, Nigeria  
[LinkedIn Profile](https://www.linkedin.com/in/abdulahi-olayinka-abubakar-441a73322)

---

*Submitted as part of the CodeAlpha Data Analytics Internship.*  
*Certificate-qualifying tasks: Task 2 and Task 3 (Round 1).*  
*Round 2 completed independently for skills development.*