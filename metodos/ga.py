#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import random

from calcularfitness import CalcFitness
from genotipo import Genotipo
from poblacion import Poblacion


class GeneticAlgorithm:
    def __init__(self, elitismo):
        self.p_cruce = 0.7
        self.p_mutacion = 0.01
        self.elitismo = elitismo
        self.calc = None

    def get_next_generation(self, poblacion):
        """Obtiene una nueva poblacion con base a mutaciones y cruces"""
        self.calc = poblacion.calc
        if self.p_mutacion == 0:
            self.p_mutacion = round(1 / (self.calc.longitud), 2)
        nueva_poblacion = Poblacion(poblacion.tam_poblacion, False, self.calc)

        offset = 0
        if self.elitismo:
            offset = 1
            nueva_poblacion.agregar_genotipo(poblacion.get_fittest())
        # crossover
        temp_genotypes = self.roulette_selection(poblacion)
        for i in range(poblacion.tam_poblacion):
            if i == (poblacion.tam_poblacion - 1):
                aux = self.cruzar(temp_genotypes[i], temp_genotypes[0])
            else:
                aux = self.cruzar(temp_genotypes[i], temp_genotypes[i + 1])
            aux.get_fitness()
            poblacion.genotipos[i] = aux
        # mutation
        i = offset

        while i < poblacion.tam_poblacion:
            # pdb.set_trace()
            aux = copy.deepcopy(poblacion.genotipos[i])
            self.mutar(aux)
            aux.get_fitness()
            nueva_poblacion.agregar_genotipo(aux)
            i += 1

        return nueva_poblacion

    # Validar que cumpla las condiciones
    def mutar(self, genotype):
        """mutate over all genes"""
        for i in range(self.calc.longitud):
            p = random.random()
            if p <= self.p_mutacion:
                i = random.randrange(0, self.calc.longitud)
                if genotype.genes[i] == '0':
                    genotype.set_gen(i, '1')
                else:
                    genotype.set_gen(i, '0')
            if not self.calc.validar_cadena(genotype.genes):
                genotype.generar_genotipo()

    # Validar que cumpla las condiciones
    def cruzar(self, genotype1, genotype2):
        """Crossover over all genes"""
        new_genotype = Genotipo(self.calc)

        if random.random() <= self.p_cruce:
            n = random.randrange(0, genotype1.longitud)
            uno = genotype1.genes[:n] + genotype2.genes[n:]
            new_genotype.set_genes(uno)
            return new_genotype
        else:
            return genotype1

    @staticmethod
    def roulette_selection(population):
        """Algoritmo de seleccion de la siguiete poblacion"""
        sum_fit = population.get_fitness_total()
        sum_proba = 0
        proba_table = list()
        nueva_poblacion = list()

        for genotype in population.genotipos:
            proba = round(genotype.fitness / sum_fit, 2)
            sum_proba += proba
            proba_table.append(sum_proba)
        i = 0
        while i < population.tam_poblacion:
            number = random.random()
            for j in range(len(proba_table)):
                if number <= proba_table[j]:
                    nueva_poblacion.append(population.genotipos[j])
                    i += 1

                if not (i < population.tam_poblacion):
                    break

        return nueva_poblacion
