#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ga import GeneticAlgorithm
from population import Population


population = Population(5, True)
algorithm = GeneticAlgorithm(True)
print(population.genotypes)

for i in range(100):
    print('Generation: '+str(i) + ' ' + str(population.get_total_population()))
    population = algorithm.get_next_generation(population)

print(population.genotypes)
