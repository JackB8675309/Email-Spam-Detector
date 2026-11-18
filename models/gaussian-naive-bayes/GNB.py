import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.naive_bayes import GaussianNB

emails = pd.read_csv("email-phishsing-data.csv").dropna