import random

class Chromosome:

    def __init__(self, genes=None):
        
         
        if genes is not None :
            self.genes = genes
        else :   
            self.genes = [random.randint(0, 7) for _ in range(63)]

    def crossover(self, partner):
        
        point = random.randint(1, 62)   

        child = self.genes[:point] + partner.genes[point:]

        return Chromosome(child)

    def mutate(self, mutation_rate=0.05):
        
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.randint(0, 7)