---
title: Course organisation and getting started
description: Course organisation, data in Python, study designs, sampling and randomized experiments.
---

# Course organisation and getting started

Mathematical Statistics builds on Descriptive Statistics and develops the methods needed to draw conclusions from data. This opening chapter explains how the course is organised, how to prepare for classes and how the first lecture connects to the rest of the semester. Practical work links statistical reasoning with data analysis in Python or other statistical software.

Consult the course page on eNauczanie for announcements and confirmed assessment dates for the **2026/27 academic year**.

## Teaching and contact

| Item | Details |
| --- | --- |
| Lecturer | dr inż. Karol Flisikowski, prof. PG |
| Department | Statistics and Econometrics |
| Office | Room 708 B |
| Office hours | Tuesday, 13:00–14:00 |
| Email | karflisi@pg.edu.pl; alternative: karol@ctbu.edu.cn |
| Telephone | 58 348 63 12 |
| Course resources | eNauczanie |

Office hours are normally held in person. Online consultations can also be arranged; confirm the meeting platform when booking.

## Course aims and learning pathway

The course covers sampling, estimation, hypothesis testing and analysis of variance, with extensions to nonparametric and multivariate methods. Linear regression is also part of the broader course scope. These methods support later work in econometrics, forecasting, statistical quality control and data analysis.

The following sequence shows how the topics build on one another throughout the semester.

| Stage | Lecture topics | Practical work |
| --- | --- | --- |
| Introduction and revision | Course organisation; review of Statistics I and descriptive statistics | Software orientation and descriptive reports |
| Probability and sampling | Probability distributions; sampling | Distribution calculations and sampling exercises |
| Estimation | Point and interval estimation | Parametric estimation |
| Hypothesis testing | Tests for one parameter; two independent samples; two dependent samples | Test selection, calculations and interpretation; mid-term assessment |
| Analysis of variance | ANOVA and multiple comparisons | Comparing several groups |
| Nonparametric methods | Goodness of fit; normality; tests for independent and dependent samples; nonparametric ANOVA | Choosing and applying methods with different assumptions |
| Further comparisons and multivariate methods | Tests for three or more means and proportions; ANCOVA; MANOVA; MANCOVA | Revision, multivariate analysis and final assessment |

Check the class schedule on eNauczanie for the dates of the mid-term and final assessments.

## Assessment and passing the course

| Component | Weight | Assessment |
| --- | --- | --- |
| Lecture final exam | 34% | Final examination; a score **strictly above 60%** is required |
| Laboratories | 33% | Mid-term and final tests; quizzes are for practice and carry no points |
| Seminars | 33% | In-class activity, mid-term and final tests, and homework |

**Passing the lecture final exam is a separate condition for passing the course.** A high weighted result does not replace the requirement to score more than 60% on that exam. Extra credit is available during the semester. Check the course announcements for the conditions and final grading scale.

## Attendance and preparation

Attendance is obligatory. You are permitted at most **one unjustified absence in each class type**: lectures, laboratories and seminars.

Before a laboratory or seminar, review the theory for the topic and prepare the solved tasks from the previous class. During practical classes, work through problems with the teacher and explain what each calculation means. Lecture notes, statistical tables and e-books can support this classwork.

Before each assessment, check the rules on permitted resources. Where restricted-resource rules apply, you may use tools built into Python libraries, **one page of formulas** and printed statistical tables; other resources are prohibited. Permission to use learning resources during ordinary classes does not automatically extend to assessments.

## Software and learning materials

This book uses **Python** for practical computation. The examples use pandas for data tables, NumPy for randomization and Matplotlib for plots.

Lecture notes and laboratory and seminar resources are available on eNauczanie. Use the **Course Website** link in the book navigation to access the configured course page.

The main course textbook is *Foundations of Statistics for Data Scientists with R and Python* by Alan Agresti and Maria Kateri (Chapman & Hall, 2021). The semester reading covers **chapters 1–5 and appendices 1–3**.

Supplementary reading includes:

- *Statistical Inference for Data Science* by Brian Caffo.
- *Introduction to Probability and Statistics Using R*.
- *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python*.
- *Statistical Inference*, second edition, by George Casella and Roger L. Berger.
- *Mathematical Statistics and Data Analysis*, third edition, by John A. Rice.
- *Data Science from Scratch: First Principles with Python*, second edition, by Joel Grus.

The supplementary titles offer further explanations and examples; they are optional reading.

## The first class

The first class, *Statistics, Data and Statistical Thinking*, lasts **120 minutes**. It combines individual reasoning, pair discussion, short group decisions and whole-class checks. Record both your answers and the reasoning behind them.

The guiding question is: **When can data support a useful conclusion about a larger population, and what can go wrong between data collection and inference?**

By the end of the first lecture, you should be able to:

1. Distinguish descriptive statistics from inferential statistics.
2. Identify an experimental unit, population, sample and variable in a research scenario.
3. Distinguish quantitative and qualitative data.
4. Recognise published sources, designed experiments, surveys and observational studies.
5. Explain representativeness and simple random sampling.
6. Identify selection bias, nonresponse bias and measurement error.
7. Separate a description of observed data from a claim about a wider population, and explain why that claim needs information about uncertainty.

### Preparation and class activities

Start by reviewing the course pathway and assessment rules. Write down one study habit you will use throughout the semester. Then work through the classification and scenario tasks in order: descriptive versus inferential statements, the elements of a statistical study, variable types, data collection and sampling.

Consider a university that surveys 600 students about their commuting habits. Identify the population of all currently enrolled students and the sample of 600 surveyed students. A summary of those 600 responses describes the observed sample; extending it to all students requires an inferential argument.

Next, consider a city transport office that wants to estimate the average one-way commuting time of all adult residents. It sends questionnaires to 800 selected addresses and receives 360 responses. Distinguish the selected addresses from the returned questionnaires, and consider how household selection relates to the target population of adult residents. Identify possible sources of bias. Record what the responses directly show before considering what they might imply about the population.

### Recap and self-check

Finish by writing a five-sentence summary covering descriptive statistics, inferential statistics, population and sample, sampling bias, and the checks needed before accepting a statistical claim. Then review each learning outcome and mark it “Yes”, “Almost” or “Not yet”. For any outcome you have not yet mastered, return to a relevant scenario and explain it in your own words before the next class.

Keep the following questions beside your notes throughout the course:

- What population does the question concern, and which units actually supplied data?
- How were units selected, and who did not respond?
- How were the variables measured, and what types of data resulted?
- Does the conclusion describe the observed data or extend beyond them?
- What uncertainty accompanies the inference?

These questions prepare you for estimation and testing: a numerical result is useful only when you understand what it measures and which conclusions the data support.

## Data and study design

Continue with the following sections:

- [Language of data](01_1_language_of_data.md)
- [Types of studies and the scope of inference](01_2_types_of_studies.md)
- [Sampling strategies and experimental design](01_3_sampling_and_experiments.md)
