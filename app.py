from os import read 
from flask import Flask, request, render_template

import pandas as pd 
import numpy as np 
import neattext.functions as nfx 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from dashboard import get_value_counts, get_level_count
from dashboard import get_subjects_per_level, yearwise_profit

app = Flask(__name__)

# get count vectorize text data
def get_cv_mat(df): 

    count_vect = CountVectorizer()
    cv_matrix = count_vect.fit_transform(df["clean_title"])
    return cv_matrix

# get the course_title in a clean and processed format using
# neattext.functions
def get_clean_title(df):

    # Remove stopwords
    df["clean_title"] = df["course_title"].apply(nfx.remove_stopwords)

    # Remove special characters
    df["clean_title"] = df["course_title"].apply(nfx.remove_special_characters)

    return df

