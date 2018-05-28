import genetic as gen
import globVars

path = "../data/headlines.csv"

print('init...')
globVars.init(path) 
print('init done.')

ga = gen.GeneticAlgorithm(
    globVars.AllWords,
    population_size = 30, 
    elite_size = 2,
    num_to_mutate = 15,
    max_mutations_per = 10,
    num_words_per_candidate = 100)

for _ in range(200):
    ga.create_next_gen()
    print('---')

