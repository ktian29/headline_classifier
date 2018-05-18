class Candidate:
  def __init___():
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
  def mutate(self, num_mutations):
    return None
  
  # return crossover of self and other
  def crossover(self, other):
    return None
