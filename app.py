from os import read 
from flask import Flask, request, render_template
from markupsafe import escape

import pandas as pd 
import numpy as np 
import neattext.functions as nfx 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from dashboard import get_value_counts, get_level_count
from dashboard import get_subjects_per_level, year_wise_profit

app = Flask(__name__)


# get the course_title in a clean and processed format using
# neattext.functions
def get_clean_title(df):

    # Remove stopwords
    df["clean_title"] = df["course_title"].apply(nfx.remove_stopwords)

    # Remove special characters
    df["clean_title"] = df["course_title"].apply(nfx.remove_special_characters)

    return df


# get count vectorize text data
def get_cv_mat(df): 

    # Instanciate CountVectorivzer()
    count_vect = CountVectorizer()

    # fit transfor text
    cv_matrix = count_vect.fit_transform(df["clean_title"])

    return cv_matrix


# get cosine_similarity matrix
def cosine_sim_mat(cv_matrix):

    # Instanciate cosine_similarity
    cos_sim = cosine_similarity(cv_matrix)

    return cos_sim


# load data
def read_data():

    df = pd.read_csv("udemy_course_data.csv")

    # convert price from Rupee to Dollar
    df["price"] = df["price"] * 0.0121

    # convert course title to lower cases
    df["course_title"] = df["course_title"].apply(lambda x: x.lower())

    return df


# This is the main recommendation system for a selected title
def recommend_course(df, title, cosine_mat, num_rec):

    # get selected course title ad index and drop duplicate
    course_index = pd.Series(df.index, 
                        index=df["course_title"]).drop_duplicates()
    
    # Get the index number of the selected course title
    index = course_index[title]

    # get a list of course index and the cosine similarity score
    scores = list(enumerate(cosine_mat[index]))

    # sort the scores in decending order from highest to lowest
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # get the index of cosine similarity score. we are indexing from [1:] 
    # to exclude the selected course and not recommend it.
    selected_course_index = [i[0] for i in sorted_scores[1:]]

    # Get course cosine similarity score. we are indexing from [1:] 
    # to exclude the selected course and not recommend it.
    selected_course_score = [i[1] for i in sorted_scores[1:]]

    # locate the recommended courses by indexing on the dataframe df
    rec_df = df.iloc[selected_course_index]

    # Add the similarity score to the rec_df dataframe
    rec_df["similarity_score"] = selected_course_score

    # select required columns
    final_recommende_courses = rec_df[[
        'course_title', 'similarity_score', 'url', 'price', 
        'num_subscribers'
    ]]

    return final_recommende_courses.head(num_rec)


# this is called when a part of the title is uesd and not the complete title
def search_term(term, df):
    result_df = df[df["course_title"].str.contains(term)]
    top_6 = result_df.sort_values(by="num_subscribers", ascending=False).head(6)
    return top_6
    

# Extract features from the  recommended dataframe
def extract_features(rec_df):

    # get course url
    course_url = list(rec_df["url"])
    # get course title
    course_title = list(rec_df["course_title"])
    # get course price
    course_price = list(rec_df["price"])

    return course_url, course_title, course_price


# Home page route
@app.route("/", methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":

        # get course title
        my_dict = request.form
        title_name = my_dict["course"]
        print(title_name)

        try:
            # read in the dataframe
            df = read_data()
            # clean the title column
            df = get_clean_title(df)

            # Count vectorize the title column
            cv_mat = get_cv_mat(df)
            # Get cosine similarity matrix
            cosine_mat = cosine_sim_mat(cv_mat)
            # assingn number of recommendation needed
            num_rec = 6

            # get recommended courses dataframe
            rec_df = recommend_course(df, title_name, 
                                      cosine_mat, num_rec)
            
            # get features from recommended dataframe
            course_url, course_title, course_price = extract_features(rec_df)

            dict_map = dict(zip(course_title, course_url))

            if len(dict_map) != 0:
                return render_template('index.html', coursemap=dict_map, coursename=title_name, showtitle=True)
            
            else:
                return render_template("index.html", showerror=True, coursename=title_name)
            
        except:
            result_df = search_term(title_name, df)
            if result_df.shape[0] > 6:
                result_df = result_df.head(6)
                course_url, course_title, course_price = extract_features(result_df)
                course_map = dict(zip(course_title, course_url))
                if len(course_map) != 0:
                    return render_template('index.html', coursemap=course_map, coursename=title_name, showtitle=True)
                
                else:
                    return render_template('index.html', showerror=True, coursename=title_name)

            else:
                course_url, course_title, course_price = extract_features(result_df)
                course_map = dict(zip(course_title, course_url))
                if len(course_map) != 0:
                    return render_template('index.html', coursemap=course_map, coursename=title_name, showtitle=True)
                
                else:
                    return render_template('index.html', showerror=True, coursename=title_name)

    return render_template("index.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    df = read_data()

    value_counts = get_value_counts(df)

    level_counts = get_level_count(df)

    subjects_per_level = get_subjects_per_level(df)

    year_wise_profit_map, subscribers_count_map, profit_month_wise, month_wise_sub = year_wise_profit(df) 

    return render_template('dashboard.html', value_counts=value_counts, level_counts=level_counts,
                           subjects_per_level=subjects_per_level, year_wise_profit_map=year_wise_profit_map, 
                           subscribers_count_map=subscribers_count_map, profit_month_wise=profit_month_wise, 
                           month_wise_sub=month_wise_sub)


if __name__ == "__main__":
    app.run(debug=False)
