#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Genotype:
    """docstring for Genotype"""
    def __init__(self, calcfitness):
        self.length = calcfitness.long
        self.genes = ''
        self.fitness = 0
        self.calcfitness = calcfitness

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.fitness)
        # return self.genes

    def generate_genotype(self):
        """Generamos cada parte del genotipo, validamos que cumpla las restricciones
        y lo concatenamos con el resto del genotipo"""
        i = 0
        while i < len(self.calcfitness.z):
            formato = '0' + str(self.calcfitness.mj[i]) + 'b'
            substring = format(random.getrandbits(self.calcfitness.mj[i]), formato)
            if self.calcfitness.validate_limit(substring, i):
                i += 1
                self.genes += substring
        self.get_fitness()

    def set_gen(self, i, value):
        """Modificamos un gen en especifico de la cadena"""
        self.genes = self.genes[:i] + value + self.genes[i+1:]

    def set_genes(self, string):
        """Modificamos la cadena"""
        if len(string) <= self.length:
            if self.calcfitness.validate_genes(string):
                self.genes = string
                self.get_fitness()
            else:
                self.generate_genotype()
        else:
            raise Exception

    def get_fitness(self):
        """Obtener el fitness de toda la cadena"""
        self.fitness = self.calcfitness.get_fitness(self.genes)
        return self.fitness
