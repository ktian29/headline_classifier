from random import randint, shuffle

NUM_WORDS = 500

class Candidate:
  def __init___(words):
    self.words = words
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
        new_words[randint(0, len(new_words))] = all_words[randint(0, len(all_words))]
    return Candidate(new_words)
  
  # return crossover of self and other
  def crossover(self, other):
    all_words = list(set(self.words) | set(other.words))
    all_words.shuffle()
    if len(all_words) > NUM_WORDS:
        return all_words[0:500]
    else:
        return all_words


