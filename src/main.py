import genetic as gen
import globVars
    
path = "/Users/Nico/Documents/GitHub/headline_classifier/data/headlines.csv"

globVars.init(path) 

ga = gen.GeneticAlgorithm(
    globVars.AllWords,
    population_size = 25, 
    elite_size = 3,
    num_to_mutate = 7,
    max_mutations_per = 5,
    num_words_per_candidate = 10)

for _ in range(20):
    ga.create_next_gen()
    print('---')



#all_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];