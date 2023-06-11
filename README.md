# Udemy Course Recomendation System

## Table of Content
* [Demo](#demo)
* [Overview](#overview)
* [Motivation](#motivation)
* [Problem Solving Steps](#problem-solving-steps)
* [Source of Dataset](#source-of-dataset)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Recommendation System](#recommendation-system)
* [Data Cleaning Techniques](#data-cleaning-techniques)
* [Model Building](#model-building)
* [Model Performance](#model-performance)
* [Deployment](#deployment)
* [Future scope of project](#future-scope-of-project)

## Demo




https://github.com/lawalsegun2025/udemy_course_recommendation_system/assets/94943377/a7decaed-11a9-4a44-a5c9-9960f0aa13ab



## Overview

This project helps recommend similar courses on udemy for which the user is searching for. The user enters the name or phrase of a subject of interest and related courses will be recommended and displayed. There is also and analysis dashboard that gives all the analysis of the udemy courses available in the dataset. </br></br>
<img src="img/udemy_courses.png">

## Motivation

## Problem Solving Steps

1. Import the dataset
2. Peform Text Preprocessing 
3. Perform Exploratory Data Analysis (EDA) an generate insights.
4. Convert text to numveric values and calculate the cosine similarity score.
5. After finding the similarity score, sort the values which have similar similarity score and recommend the course.
6. Integrate the Recommendation System with Flask Framework.
7. Deploy the web Application on a cloud platform

## Source of Dataset

This dataset contains 3683 records of courses from 4 subjects (Business Finance, Graphic Design, Musical Instruments and Web Design) taken from Udemy.

Udemy is a massive online open course (MOOC) platform that offers both free and paid courses. Anybody can create a course, a business model by which allowed Udemy to have hundreds of thousands of courses.
This version modifies column names, removes empty columns and aggregates everything into a single csv file for ease of use.

## Exploratory Data Analysis

For the exploratory data analysis, we explored the dataset by trying to answer the following question to have a better understanding of the data;
### Questions to Solve

* **Course Title**
    - What is the most frequent words in course title?
    - Longest/Shortest course title?
    - How can we build recommendation systems via title using similarity?
    - Most famous courses by number of subscribers?
* **Subjects/Categories**
    - What is the distribution of subjects?
    - How many courses per subject?
    - Distribution of subjects per year?
    - How many people purchase a particular subject?
    - Which subjects is the most popular?
* **Published Year**
    - Number of courses per year?
    - Which year has the highest number of courses?
    - What is the trend of courses per year?
* **Levels**
    - How many levels do we have?
    - What is the distribution of courses per level?
    - Which subject have the highest levels?
    - How many subscribers per level?
    - How many courses per level?
* **Duration of Course**
    - Which courses have the highest duration (paid and free)?
    - Which courses have higher durations?
    - Duration vs number of subscribers?
* **Subscribers**
    - Which course have the highest number of subscribers?
    - Average number of subscribers?
    - Number of subscribers per subject?
    - Number of subscribers per year?
* **Price**
    - What is the average price of a course?
    - What is the minimum and maximum price?
    - How much does Udemy earn?
    - The most profitable courses?
* **Correlation**
    - Does number of subscribers depend on;
        - Number of reviews?
        - Price?
        - Number of lectures?
        - Content duration?
* **Question on Time**
    - Published Year
        - Number of courses per year?
        - Distribution of subjects per year?
        - Which year has the highest number of courses?
        - What is the trend of courses per year?

## Recommendation System

**Algorithms**
* Cosine Similarity
* Linear Similarity

**Workflow**
* Import Dataset
* Vectorize Dataset
* Cosine Similarity Matrix
* ID Score
* Recommend

## Data Cleaning Techniques

## Model Building

## Model Performance

## Deployment

## Future scope of project
