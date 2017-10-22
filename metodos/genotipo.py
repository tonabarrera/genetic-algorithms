#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Genotipo:
    """docstring for Genotype"""
    def __init__(self, calcfitness):
        self.longitud = calcfitness.longitud
        self.genes = ''
        self.fitness = 0
        self.calc = calcfitness

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.fitness)
        # return self.genes

    def generar_genotipo(self):
        """Generamos cada parte del genotipo, validamos que cumpla las restricciones
        y lo concatenamos con el resto del genotipo"""
        i = 0
        while i < len(self.calc.z):
            formato = '0' + str(self.calc.mj[i]) + 'b'
            substring = format(random.getrandbits(self.calc.mj[i]), formato)
            if self.calc.validar_gen(substring, i):
                i += 1
                self.genes += substring
        self.get_fitness()

    def set_gen(self, i, value):
        """Modificamos un gen en especifico de la cadena"""
        self.genes = self.genes[:i] + value + self.genes[i+1:]

    def set_genes(self, string):
        """Modificamos la cadena"""
        if len(string) <= self.longitud:
            if self.calc.validar_cadena(string):
                self.genes = string
                self.get_fitness()
            else:
                self.generar_genotipo()
        else:
            raise Exception

    def get_fitness(self):
        """Obtener el fitness de toda la cadena"""
        self.fitness = self.calc.get_fitness(self.genes)
        return self.fitness

    def genotipo_a_fenotipo(self):
        """La representacion de la cadena con base a sus variables (A, B, C, D)"""
        i = 0
        anterior = 0
        representacion = ''
        while i < len(self.calc.z):
            representacion += self.calc.etiquetas[i] + '='
            sub = self.genes[anterior:self.calc.mj[i] + anterior]
            anterior += self.calc.mj[i]
            representacion += str(self.calc.obtener_coeficiente(i, sub)) + ' '
            i += 1

        return representacion