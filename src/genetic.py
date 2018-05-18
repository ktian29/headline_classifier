from random import randint, shuffle, random

class Candidate:
    def __init__(self, words, max_words = 500):
        self.words = words
        self.max_words = max_words
        self.fitness = None
  
    # calculate fitness once and store it
    def get_fitness(self):
        if self.fitness is None:
            self.fitness = self._calculate_accuracy()
        return self.fitness
  
    # train neural network on headlines and cross validate, returning the
    # accuracy as the fitness for the genetic algorithm
    def _calculate_accuracy(self):
        return 0.0
  
    # return randomly mutated version of a candidate
    def mutate(self, num_mutations, all_words):
        new_words = self.words[:]
        for _ in range(0, num_mutations):
            new_words[randint(0, len(new_words)) - 1] = all_words[randint(0, len(all_words)) - 1]
        return Candidate(new_words)
    
    # mutate mutably
    def mutate_in_place(self, num_mutations, all_words):
        for _ in range(0, num_mutations):
            self.words[randint(0, len(new_words)) - 1] = all_words[randint(0, len(all_words)) - 1]
        
    # return crossover of self and other
    def crossover(self, other):
        all_words = list(set(self.words) | set(other.words))
        shuffle(all_words)
        if len(all_words) > self.max_words:
            return Candidate(all_words[0:self.max_words], self.max_words)
        else:
            return Candidate(all_words, self.max_words)
    
    def __lt__(self, other):
        return self.get_fitness() < other.get_fitness()


class GeneticAlgorithm:
    def __init__(self, words, population_size, elite_size, num_to_mutate, max_mutations_per):
        self.words = words
        self.population_size = population_size
        self.elite_size = elite_size
        self.population = [] # random population
        self.num_to_mutate = num_to_mutate
        self.max_mutations_per = self.num_mutations_per
    
    def create_next_gen(self):
        self.population.sort(reverse = true)
        # a fixed number of 'elites,' the best ones, survive automatically
        next_gen = self.population[0:self.elite_size]
        others = self.population[self.elite_size:]
        # select random survivors from outside the elites, with higher
        # probability for higher fitnesses
        for i in range(0, len(others)):
            if random() > i / len(others):
                next_gen.append(others[i])
        # repopulate with crossover
        while len(next_gen) < self.population_size:
            lim = randint(0, len(next_gen) - 1)
            parent1 = next_gen[randint(0, lim)]
            parent2 = next_gen[randint(0, lim)]
            next_gen.append(parent1.crossover(parent2))
        # mutate
        for _ in range(0, self.num_to_mutate):
            i = randint(0, len(next_gen) - 1)
            next_gen[i].mutate_in_place(1, randint(self.max_mutations_per), self.words) 
        
        self.population = next_gen
        
#all_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
#             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
#             's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
#c1 = Candidate(['a', 'b', 'c', 'd', 'e'], 5)
#c2 = Candidate(['v', 'w', 'x', 'y', 'z'], 5)
#print(c1.mutate(2, all_words).words)
#print(c1.mutate(2, all_words).words)
#print(c1.mutate(2, all_words).words)
#print(c1.mutate(2, all_words).words)
#print(c1.crossover(c2).words)
