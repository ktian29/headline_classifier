import pandas as pd
import numpy as np

def init(path):
    df = pd.read_csv(path,names=['Labels','Headlines'])

    global Labels, Headlines, zipped, AllWords, Categories
    Labels = list(df["Labels"])
    Headlines = list(df["Headlines"])
    Categories = list(np.unique(Labels))
    zipped = list(zip(Headlines, Labels))
    AllWords = []
    for headline in Headlines:
        for word in headline.split(' '):
            word = ''.join(filter(str.isalpha, word))
            if len(word) > 1:
                AllWords.append(word)
