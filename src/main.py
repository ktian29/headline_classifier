import genetic as gen
import globVars

path = "/Users/Nico/Documents/GitHub/headline_classifier/data/headlines2.csv"

print('init...')
globVars.init(path) 
print('init done.')

ga = gen.GeneticAlgorithm(
    globVars.AllWords,
    population_size = 30, 
    elite_size = 5,
    num_to_mutate = 15,
    max_mutations_per = 10,
    num_words_per_candidate = 20)

for _ in range(20):
    ga.create_next_gen()
    print('---')



#all_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
