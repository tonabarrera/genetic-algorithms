#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class CalcFitness:
    """Falta el como manejar las restricciones"""
    def __init__(self):
        self.z = list()  # Coeficientos de la funcion objetivo
        self.mj = list()  # Longitud de las subcadenas
        self.long = 0  # Longitud total de la cadena
        self.aj = list()  # Limite inferior
        self.bj = list()  # Limite superior
        self.precision = 0  # Precision

    def get_mj(self):
        """Obtencion de la longitud de las cadenas"""
        i = 0
        while i < len(self.z):
            aux = (self.bj[i]-self.aj[i]) * (10**self.precision)
            self.mj.append(math.ceil(math.log(aux)/math.log(2)))
            self.long += self.mj[i]
            i = i+1

    def get_fitness(self, string):
        """Obtine el fitness de una cadena partiendola en la longitud
        de cada variable de la funcion objetivo"""
        fitness = 0
        anterior = 0
        i = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i]+anterior]
            anterior = self.mj[i]
            aux = self.obtener_coeficiente(i, sub)
            fitness += self.z[i] * aux
            i = i+1

        return round(fitness, 2)

    def obtener_coeficiente(self, i, sub):
        producto = (self.bj[i]-self.aj[i])/((2**self.mj[i])-1)
        return self.aj[i] + self.binary_to_int(sub)*producto

    def binary_to_int(self, substring):
        """Convertir binario a decimal"""
        return int(substring, 2)

    def get_funtion(self, expresion):
        """Aqui se obtendran los coeficientes de la funcion objetivo"""
        pass

    def validate_limit(self, substring, position):
        """Aqui se validara una subcadana que cumpla las restricciones
        correspondientes"""
        aux = self.obtener_coeficiente(position, substring)
        if position == 0:
            if aux > 3:
                print('No ' + str(aux))
                return False
        else:
            if aux > 5:
                print('No ' + str(aux))
                return False
        return True

    def validate_genes(self, string):
        """Esta funcion se llamara cuando 
        se realice un crossover o una mutacion"""
        anterior = 0
        i = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i] + anterior]
            anterior = self.mj[i]
            if not self.validate_limit(sub, i):
                return False
            i = i + 1

        return True
