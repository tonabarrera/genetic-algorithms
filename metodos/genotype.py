#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Genotype(object):
    """docstring for Genotype"""
    def __init__(self):
        self.length = 10
        self.genes = ''
        self.fitness = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.genes

    def generate_genotype(self):
        formato = '0' + str(self.length) + 'b'
        self.genes = format(random.getrandbits(self.length), formato)

    def set_gen(self, i, value):
        self.genes = self.genes[:i] + value + self.genes[i+1:]

    def set_genes(self, string):
        if (len(string) <= self.length):
            self.genes = string
        else:
            raise Exception

    def get_fitness(self):
        """Obtener el fitness aqui o en otra clase"""
        self.fitness = int(self.genes, 2)
        return self.fitness
