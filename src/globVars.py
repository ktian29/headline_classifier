import pandas as pd
import random

def init(path):
    df = pd.read_csv(path,names=['Labels','Headlines'])

    global Labels, Headlines, zipped, AllWords
    Labels = list(df["Labels"])
    Headlines = list(df["Headlines"])
    zipped = list(zip(Headlines, Labels))
    AllWords = []
    for row in Headlines:
        for word in row.split():
            if len(word) > 3 and word not in AllWords:
                AllWords.append(word)

def sample(size):
    return random.sample(zipped, size)
