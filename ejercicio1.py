#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pdb
import math
import random


class Ejercicio():
    """docstring for Ejercicio"""
    def __init__(self):
        self.x = 1
        self.y = 1
        self.x_aj = 0
        self.x_bj = 3
        self.y_aj = 0
        self.y_bj = 5
        self.precision = 1
        self.x_mj = 0
        self.y_mj = 0
        self.poblacion = list()
        self.tam_poblacion = 3
        self.tam_cadena = 0
        self.tabla_fitness = list()
        self.pm = 0
        self.pc = .7
        self.iteraciones = 5
        self.iniciar_poblacion()

    def obtener_mj(self):
        aux_x = (self.x_bj-self.x_aj) * (math.pow(10, self.precision))
        aux_y = (self.y_bj-self.y_aj) * (math.pow(10, self.precision))
        self.x_mj = math.ceil(math.log(aux_x)/math.log(2))
        self.y_mj = math.ceil(math.log(aux_y)/math.log(2))
        self.tam_cadena = self.x_mj + self.y_mj
        self.pm = 1 / self.tam_cadena

    def iniciar_poblacion(self):
        self.obtener_mj()
        formato = '0' + str(self.tam_cadena) + 'b'
        for i in range(self.tam_poblacion):
            cadena = format(random.getrandbits(self.tam_cadena), formato)
            self.poblacion.append(cadena)
            self.tabla_fitness.append(self.calcular_fitness(cadena))

    def calcular_fitness(self, cadena):
        subcadena_x = int(cadena[:self.x_mj], 2)
        subcadena_y = int(cadena[self.y_mj:], 2)
        x_resta = self.x_bj-self.x_aj
        y_resta = self.y_bj-self.y_aj
        x = self.x_aj + (subcadena_x * (x_resta/(math.pow(2, self.x_mj)-1)))
        y = self.y_aj + (subcadena_y * (y_resta/(math.pow(2, self.y_mj)-1)))

        return (self.x * x) + (self.y * y)

    def roulette_selection(self):
        suma_fit = 0
        suma_probabilidades = 0
        tabla_probabiliades = list()
        nueva_poblacion = list()
        for fit in self.tabla_fitness:
            suma_fit += fit

        for fit in self.tabla_fitness:
            probabilidad = round(fit / suma_fit, 2)
            suma_probabilidades = suma_probabilidades + probabilidad
            tabla_probabiliades.append(suma_probabilidades)

        i = 0
        while i < self.tam_poblacion:
            number = random.random()
            for j in range(len(tabla_probabiliades)):
                if number < tabla_probabiliades[j]:
                    nueva_poblacion.append(self.poblacion[j])
                    i += 1

                if not (i < self.tam_poblacion):
                    break

        return nueva_poblacion

    def crossover(self):
        nueva_poblacion = self.poblacion
        for x in range(1, self.tam_poblacion, 2):
            number = random.random()
            if number <= self.pc:
                n = random.randrange(0, self.tam_cadena, 1)
                uno = self.poblacion[0][:n] + self.poblacion[1][n:]
                dos = self.poblacion[1][:n] + self.poblacion[0][n:]
                nueva_poblacion[0] = uno
                nueva_poblacion[1] = dos
        return nueva_poblacion

    def mutation(self):
        nueva_poblacion = list()
        for element in self.poblacion:
            p = random.random()
            if p <= self.pm:
                position = random.randrange(0, self.tam_cadena, 1)
                if (element[position] == '0'):
                    element = element[:position] + '1' + element[position+1:]
                else:
                    element = element[:position] + '0' + element[position+1:]
            nueva_poblacion.append(element)
        return nueva_poblacion

    def iterar(self):
        for i in range(self.iteraciones):
            self.poblacion = self.roulette_selection()
            print('ruleta ' + str(len(self.poblacion)))
            self.poblacion = self.crossover()
            print('crossover ' + str(len(self.poblacion)))

            self.poblacion = self.mutation()
            print('mutacion ' + str(len(self.poblacion)))

            k = 0
            for p in self.poblacion:
                self.tabla_fitness[k] = self.calcular_fitness(p)
                k += 1
