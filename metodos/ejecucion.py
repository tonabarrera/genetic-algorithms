#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ga import GeneticAlgorithm
from population import Population


population = Population(5, True)
algorithm = GeneticAlgorithm()

for i in range(20):
    print('Generation: ' + str(i) + ' Fitness: ' + str(population.get_total_population()))
    print(population)
    population = algorithm.get_next_generation(population)
