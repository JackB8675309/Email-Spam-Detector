# Luke Uhlir
# 10/19/2026
# test.py
# a script to get the mock-up of what we need done

import pandas as pd
import numpy as np
from sklearn.neighbors import  KNeighborsClassifier

emails = pd.read_csv("../data/raw/email_phishing_data.csv").dropna()

