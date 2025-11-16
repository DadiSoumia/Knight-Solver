from Population import Population

def main():
    population_size = 50
    # Créer la population initiale
    population = Population(population_size)

    generation = 1
    while True:
        # Vérifier la validité de la population actuelle
        population.check_population()

        # Évaluer la génération actuelle et obtenir le meilleur chevalier avec sa fitness
        best_knight, maxFit = population.evaluate()
        print(f"Generation {generation}, Best fitness: {maxFit}")
        
        # Si la solution parfaite est trouvée (64 cases), arrêter
        if maxFit == 64:
            print("Solution trouvée !")
            break

        # Générer la nouvelle population
        population.create_new_generation()
        generation += 1

    # Créer l'interface utilisateur pour afficher la solution
    # Ici tu peux appeler une fonction comme display_solution(best_knight) si tu as une interface graphique
    print("Meilleur chemin du chevalier :", best_knight.path)
    print("Chromosome du chevalier :", best_knight.chromosome.genes)

if __name__ == "__main__":
    main()
