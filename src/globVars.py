import pandas as pd


def init(path):
    df = pd.read_csv(path,names=['Labels','Headlines'])

    global Labels
    Labels = list(df["Labels"])

    global Headlines
    Headlines = list(df["Headlines"])


    global AllWords
    AllWords = []
    for row in Headlines:
        for word in row.split():
            if word not in AllWords:
                AllWords.append(word)