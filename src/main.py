import genetic as gen
import globVars
    
path = "data/headlines.csv"

print('init...')
globVars.init(path) 
print('init done.')

ga = gen.GeneticAlgorithm(
    globVars.AllWords,
    population_size = 25, 
    elite_size = 3,
    num_to_mutate = 7,
    max_mutations_per = 5,
    num_words_per_candidate = 800)

for _ in range(20):
    ga.create_next_gen()
    print('---')



#all_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
