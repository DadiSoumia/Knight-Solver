import random
from Knight import Knight

class Population:
    def __init__(self, population_size):
        self.population_size = population_size
        self.knights = [Knight() for _ in range(population_size)]
        self.generations = 1

    def check_population(self):
        """Vérifie la validité des mouvements de chaque chevalier."""
        for knight in self.knights:
            knight.check_moves()

    def evaluate(self):
        """Évalue la fitness de chaque chevalier et retourne le meilleur."""
        best_knight = None
        best_fitness = -1
        for knight in self.knights:
            knight.evaluate_fitness()
            if knight.fitness > best_fitness:
                best_fitness = knight.fitness
                best_knight = knight
        return best_knight, best_fitness

    def tournament_selection(self, size=3):
        """Sélectionne les deux meilleurs parents parmi un échantillon aléatoire de n chevaliers."""
        sample = random.sample(self.knights, size)
        sample.sort(key=lambda k: k.fitness, reverse=True)
        return sample[0], sample[1]

    def create_new_generation(self):
        """Crée une nouvelle génération avec crossover et mutation."""
        new_knights = []
        while len(new_knights) < self.population_size:
            # Sélection des parents
            parent1, parent2 = self.tournament_selection()

            # Crossover pour générer deux enfants
            child1_chrom = parent1.chromosome.crossover(parent2.chromosome)
            child2_chrom = parent2.chromosome.crossover(parent1.chromosome)

            # Mutation
            child1_chrom.mutate()
            child2_chrom.mutate()

            # Créer les nouveaux chevaliers
            new_knights.append(Knight(child1_chrom))
            new_knights.append(Knight(child2_chrom))

        # Ajuster si la population est trop grande
        self.knights = new_knights[:self.population_size]
        self.generations += 1
