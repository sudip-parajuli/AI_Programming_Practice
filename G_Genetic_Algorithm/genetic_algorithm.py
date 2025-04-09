"""A Genetic Algorithm is a nature-inspired optimization technique based on:
Selection: Choosing the best solutions.
Crossover: Combining two parents to make offspring.
Mutation: Introducing random changes."""


import random


# Function to maximize
def fitness(x):
    return x ** 2


# Convert binary string to integer
def decode(chromosome):
    return int(chromosome, 2)


# Generate initial population of binary strings
def generate_population(size, bits):
    return [format(random.randint(0, 2 ** bits - 1), f'0{bits}b') for _ in range(size)]


# Selection: Tournament Selection
def select(population):
    selected = random.choices(population, k=2)
    return max(selected, key=lambda c: fitness(decode(c)))


# Crossover: Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]


# Mutation: Flip one random bit
def mutate(chromosome, mutation_rate=0.1):
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return ''.join(chromosome)


# GA main function
def genetic_algorithm(pop_size=10, bits=5, generations=20):
    population = generate_population(pop_size, bits)
    print("Initial Population:")
    for c in population:
        print(f"{c} = {decode(c)}, Fitness: {fitness(decode(c))}")
    print("-" * 40)

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size):
            p1 = select(population)
            p2 = select(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population

        best = max(population, key=lambda c: fitness(decode(c)))
        print(f"Generation {gen + 1}: Best = {best}, Value = {decode(best)}, Fitness = {fitness(decode(best))}")

    best_solution = max(population, key=lambda c: fitness(decode(c)))
    print("\nBest Solution Found:")
    print(f"{best_solution} → x = {decode(best_solution)} → f(x) = {fitness(decode(best_solution))}")


# Run the GA
if __name__ == "__main__":
    genetic_algorithm()
