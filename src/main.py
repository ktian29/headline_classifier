import pandas as pd
import genetic as gen



def CreateData(path):
    df = pd.read_csv(path,names=['Labels','Headlines'])
    Labels = list(df["Labels"])
    Headlines = list(df["Headlines"])

    all_words = []
    for row in Headlines:
        for word in row.split():
            if word not in all_words:
                all_words.append(word)

    return Labels, Headlines, all_words
            
    
path = "/Users/Nico/Documents/GitHub/headline_classifier/data/headlines.csv"

Labels, Headlines, all_words = CreateData(path)
            
ga = gen.GeneticAlgorithm(
    Labels,
    Headlines,
    all_words,
    population_size = 25, 
    elite_size = 3,
    num_to_mutate = 7,
    max_mutations_per = 5,
    num_words_per_candidate = 3)

for _ in range(20):
    ga.create_next_gen()
    print('---')



#all_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];