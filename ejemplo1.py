#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

polulation_size = 4
string_len = 8
generations = 1000
pc = .7
pm = 1/string_len

def get_fitness(cadena):
    fitness = 0
    for c in cadena:
        if c == '1':
            fitness = fitness + 1
    return fitness

def roulette_selection(fitness_table, population):
    sum_fit = 0
    sum_probabilities = 0
    table_probabilities = list()
    new_population = list()
    for fit in fitness_table:
        sum_fit += fit

    for fit in fitness_table:
        p = round(fit / sum_fit, 2)
        sum_probabilities = sum_probabilities + p
        table_probabilities.append(sum_probabilities)

    i = 0
    while i < polulation_size:
        for j in range(2):
            number = random.random()
            if number < table_probabilities[0]:
                new_population.append(population[0])
                i = i + 1
            elif number < table_probabilities[1]:
                new_population.append(population[1])
                i += 1
            elif number < table_probabilities[2]:
                new_population.append(population[2])
                i += 1
            elif number < table_probabilities[3]:
                new_population.append(population[3])
                i += 1
            if not (i < polulation_size):
                break
    
    return new_population

def crossover(population):
    number = random.random()
    if number <= pc:
        n = random.randrange(0, string_len, 1)
        uno = population[0][:n] + population[1][n:]
        dos = population[1][:n] + population[0][n:]
        population[0] = uno
        population[1] = dos

    number = random.random()

    if number <= pc:
        n = random.randrange(0, string_len, 1)
        uno = population[2][:n] + population[3][n:]
        dos = population[3][:n] + population[2][n:]
        population[2] = uno
        population[3] = dos

    return population

def mutation(population):
    new_population = list()
    for element in population:
        p = random.random()
        if (p <= pm):
            position = random.randrange(0, string_len, 1)
            if (element[position] == '0'):
                element = element[:position] + '1' + element[position+1:]
            else:
                element = element[:position] + '0' + element[position+1:]
        new_population.append(element)
    return new_population


def init():
    population = list()
    fitness_table = list()
    for i in range(polulation_size):
        string = format(random.getrandbits(string_len), '08b')
        population.append(string)
        fitness = get_fitness(string)
        fitness_table.append(fitness)

    print(population)
    print(fitness_table)

    for iteracion in range(generations):
        #print(population)
        population = roulette_selection(fitness_table, population)
        population = crossover(population)

        population = mutation(population)

        k = 0
        for i in population:
            fitness_table[k] = get_fitness(i)
            k += 1

    print(population)
    print(fitness_table)

init()