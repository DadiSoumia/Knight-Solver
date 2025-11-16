import random
from Chromosome import Chromosome

class Knight:
    def __init__(self, chromosome=None):
        # Position initiale
        self.position = (0, 0)
        self.path = [self.position]  # liste des positions visitées
        self.fitness = 0  # nombre de cases visitées sans répétition

        # Initialisation du chromosome
        if chromosome:
            self.chromosome = chromosome
        else:
            self.chromosome = Chromosome()  # objet Chromosome aléatoire

    def move_forward(self, direction):
        """Retourne la nouvelle position après le mouvement sans modifier path."""
        x, y = self.position
        moves = {
            0: (x + 2, y + 1), 1: (x + 1, y + 2), 2: (x + 1, y - 2), 3: (x + 2, y - 1),
            4: (x - 2, y - 1), 5: (x - 1, y - 2), 6: (x - 1, y + 2), 7: (x - 2, y + 1)
        }
        return moves.get(direction, (x, y))

    def move_backward(self):
        """Annule le dernier mouvement."""
        if len(self.path) > 1:
            self.path.pop()
            self.position = self.path[-1]

    def check_moves(self):
      cycle_forward = random.choice([True, False])
      for i in range(len(self.chromosome.genes)):
        new_pos = self.move_forward(self.chromosome.genes[i])

        if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8 and new_pos not in self.path:
            self.position = new_pos
            self.path.append(new_pos)
        else:
            found = False
            for j in range(1, 8):
                new_dir = (self.chromosome.genes[i] + j) % 8 if cycle_forward else (self.chromosome.genes[i] - j) % 8
                candidate_pos = self.move_forward(new_dir)
                if 0 <= candidate_pos[0] < 8 and 0 <= candidate_pos[1] < 8 and candidate_pos not in self.path:
                    self.chromosome.genes[i] = new_dir
                    self.position = candidate_pos
                    self.path.append(candidate_pos)
                    found = True
                    break
            if not found:
                 x, y = new_pos
                 x = min(max(x, 0), 7)
                 y = min(max(y, 0), 7)
                 new_pos = (x, y)
                 self.position = new_pos
                 if new_pos not in self.path:
                    self.path.append(new_pos)

                   

    def evaluate_fitness(self):
        self.fitness = 0
        visited = set()
        for pos in self.path:
            if pos not in visited:
                self.fitness += 1
                visited.add(pos)
            else:
                break  # Arrêter à la première case revisitée

