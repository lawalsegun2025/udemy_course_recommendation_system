from os import read 
from flask import Flask, request, render_template

import pandas as pd 
import numpy as np 
import neattext.functions as nfx 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from dashboard import get_value_counts, get_level_count
from dashboard import get_subjects_per_level, yearwise_profit
