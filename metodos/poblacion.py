#!/usr/bin/env python
# -*- coding: utf-8 -*-
from genotipo import Genotipo


class Poblacion:
    def __init__(self, tam, inicial, calcfitness):
        self.genotipos = list()
        self.tam_poblacion = tam
        self.fitness_total = 0
        self.calc = calcfitness
        if inicial:
            self.crear_poblacion()

    def __str__(self):
        return self.genotipos.__str__()

    def crear_poblacion(self):
        """Inicializamos toda nuestra poblacion"""
        for i in range(self.tam_poblacion):
            genotipo = Genotipo(self.calc)
            genotipo.generar_genotipo()
            self.genotipos.append(genotipo)

    def agregar_genotipo(self, genotipo):
        """Agrega un genotipo"""
        self.genotipos.append(genotipo)

    def set_genotipo(self, position, genotipo):
        """Ponemos un genotipo en una posicion en especifico"""
        self.genotipos[position] = genotipo

    def get_fitness_total(self):
        """Obtenemos la fitness total de la cadena para hacer nuestra seleccion"""
        self.fitness_total = 0
        for i in range(self.tam_poblacion):
            self.fitness_total += self.genotipos[i].get_fitness()
        return self.fitness_total

    def get_fittest(self):
        """Obtenemos el elemento con el mayor fitness para que pase a la siguiente ronda"""
        element = self.genotipos[0]

        for i in range(1, self.tam_poblacion):
            if element.get_fitness() < self.genotipos[i].get_fitness():
                element = self.genotipos[i]

        return element
