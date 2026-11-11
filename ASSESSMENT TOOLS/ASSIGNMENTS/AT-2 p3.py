import math, random

cities = [(0, 0), (0, 1), (1, 1), (1, 0)]
dist = lambda t: sum(math.dist(cities[t[i]], cities[t[i-1]]) for i in range(len(t)))

def simulated_annealing(tour, temp, cooling):
    while temp > 1:
        i, j = sorted(random.sample(range(len(tour)), 2))
        new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
        delta = dist(new_tour) - dist(tour)
        if delta < 0 or random.random() < math.exp(-delta / temp):
            tour = new_tour
        temp *= cooling
    return tour

best_tour = simulated_annealing([0, 2, 1, 3], 100, 0.9)
print(f"Optimized Tour: {best_tour}\nCost: {dist(best_tour)}")
