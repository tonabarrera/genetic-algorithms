#!/usr/bin/env python
# -*- coding: utf-8 -*-
from genotype import Genotype


class Population:
    def __init__(self, size, init):
        self.genotypes = list()
        self.size = size
        self.population_fitness = 0
        if init:
            self.create_population()

    def __str__(self):
        return self.genotypes.__str__()

    def create_population(self):
        for i in range(self.size):
            genotype = Genotype()
            genotype.generate_genotype()
            self.genotypes.append(genotype)

    def add_genotype(self, genotype):
        self.genotypes.append(genotype)

    def set_genotype(self, position, genotype):
        self.genotypes[position] = genotype

    def get_total_population(self):
        for i in range(self.size):
            self.population_fitness += self.genotypes[i].get_fitness()
        return self.population_fitness

    def get_fitesst(self):
        element = self.genotypes[0]

        for i in range(1, self.size):
            if element.get_fitness() < self.genotypes[i].get_fitness():
                element = self.genotypes[i]

        return element
