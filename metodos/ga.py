#!/usr/bin/env python
# -*- coding: utf-8 -*-
from population import Population
from genotype import Genotype
import random
import pdb
import copy


class GeneticAlgorithm:
    def __init__(self, elitism):
        self.p_crossover = 0.7
        self.p_mutation = 1/20
        self.elitism = elitism

    def get_next_generation(self, population):
        new_population = Population(population.size, False)

        offset = 0
        if self.elitism:
            offset = 1
            new_population.add_genotype(population.get_fitesst())
        # crossover
        temp_genotypes = self.roulette_selection(population)
        for i in range(population.size):
            if i == (population.size - 1):
                aux = self.crossover(temp_genotypes[i], temp_genotypes[0])
            else:
                aux = self.crossover(temp_genotypes[i], temp_genotypes[i+1])
            aux.get_fitness()
            population.genotypes[i] = aux
        # mutation
        i = offset

        while (i < population.size):
            # pdb.set_trace()
            aux = copy.deepcopy(population.genotypes[i])
            self.mutate(aux)
            aux.get_fitness()
            new_population.add_genotype(aux)
            i += 1

        return new_population

    def mutate(self, genotype):
        """mutate over all genes"""
        for i in range(genotype.length):
            if random.random() <= self.p_mutation:
                if (genotype.genes[i] == '0'):
                    genotype.set_gen(i, '1')
                else:
                    genotype.set_gen(i, '0')

    def crossover(self, genotype1, genotype2):
        """Crossover over all genes"""
        new_genotype = Genotype()

        if random.random() <= self.p_crossover:
            n = random.randrange(0, genotype1.length)
            uno = genotype1.genes[:n] + genotype2.genes[n:]
            new_genotype.set_genes(uno)
            return new_genotype
        else:
            return genotype1

    def roulette_selection(self, population):
        sum_fit = population.get_total_population()
        sum_proba = 0
        proba_table = list()
        nueva_poblacion = list()

        for genotype in population.genotypes:
            proba = round(genotype.fitness / sum_fit, 2)
            sum_proba += proba
            proba_table.append(sum_proba)
        i = 0
        while i < population.size:
            number = random.random()
            for j in range(len(proba_table)):
                if number <= proba_table[j]:
                    nueva_poblacion.append(population.genotypes[j])
                    i += 1

                if not (i < population.size):
                    break

        return nueva_poblacion
