#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calcfitness import CalcFitness
from ga import GeneticAlgorithm
from population import Population


def iniciar():
    calculate = CalcFitness()
    calculate.precision = 10

    calculate.z = [1, 1]
    calculate.bj = [3, 5]
    calculate.aj = [0, 0]
    calculate.get_mj()
    population = Population(10, True, calculate)
    algorithm = GeneticAlgorithm(True)
    print(population.genotypes)
    for i in range(100):
         population = algorithm.get_next_generation(population)

    print(population.genotypes)



iniciar()
