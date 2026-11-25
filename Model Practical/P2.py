import random

items = [(2, 10), (3, 15), (5, 30), (7, 45), (1, 5)]
CAPACITY = 10
POP_SIZE = 20
GENERATIONS = 50
MUTATION_RATE = 0.1

def fitness(chromosome):
    total_weight = sum(items[i][0] for i in range(len(items)) if chromosome[i] == 1)
    total_value = sum(items[i][1] for i in range(len(items)) if chromosome[i] == 1)
    return total_value if total_weight <= CAPACITY else 0

def create_individual():
    return [random.randint(0, 1) for _ in range(len(items))]

def crossover(parent1, parent2):
    point = random.randint(1, len(items) - 1)
    return parent1[:point] + parent2[point:]

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

population = [create_individual() for _ in range(POP_SIZE)]

for _ in range(GENERATIONS):
    population.sort(key=fitness, reverse=True)
    next_gen = population[:2]
    
    while len(next_gen) < POP_SIZE:
        p1, p2 = random.sample(population[:10], 2)
        child = mutate(crossover(p1, p2))
        next_gen.append(child)
        
    population = next_gen

best_solution = max(population, key=fitness)
selected_items = [items[i] for i in range(len(items)) if best_solution[i] == 1]

print("Best Chromosome:", best_solution)
print("Selected Items (Weight, Value):", selected_items)
print("Maximum Fitness Value:", fitness(best_solution))
