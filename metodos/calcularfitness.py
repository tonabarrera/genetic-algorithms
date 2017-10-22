#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


class CalcFitness:

    def __init__(self):
        self.z = list()  # Coeficientos de la funcion objetivo
        self.mj = list()  # Longitud de las subcadenas
        self.longitud = 0  # Longitud total de la cadena
        self.aj = list()  # Limite inferior
        self.bj = list()  # Limite superior
        self.precision = 0  # Precision
        self.productos = list()  # Lista que guardara los valores de (bj-aj)/(2**mj-1)
        self.etiquetas = ['A', 'B', 'C', 'D']

    def get_mj(self):
        """Obtencion de la longitud de las cadenas"""
        i = 0
        while i < len(self.z):
            aux = (self.bj[i] - self.aj[i]) * (10 ** self.precision)
            self.mj.append(math.ceil(math.log(aux) / math.log(2)))
            self.longitud += self.mj[i]
            i = i + 1
        self.productos = [0] * len(self.z)

    def get_fitness(self, string):
        """Obtine el fitness de una cadena partiendola en la longitud
        de cada variable de la funcion objetivo"""
        fitness = 0
        anterior = 0
        i = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i] + anterior]
            anterior += self.mj[i]
            aux = self.obtener_coeficiente(i, sub)
            fitness += self.z[i] * aux
            i = i + 1

        return round(fitness, 2)

    def obtener_coeficiente(self, i, sub):
        """Calcula el valor del coeficiente, utilizamos una lista para no calcular
        el producto mas de una vez"""
        if self.productos[i] == 0:
            producto = (self.bj[i] - self.aj[i]) / ((2 ** self.mj[i]) - 1)
            self.productos[i] = producto
        else:
            producto = self.productos[i]
        return round(self.aj[i] + self.binary_to_int(sub) * producto, 2)

    @staticmethod
    def binary_to_int(substring):
        """Convertir binario a decimal"""
        return int(substring, 2)

    def validar_gen(self, substring, position):
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

    def validar_cadena(self, string):
        """Metodo que valida todo un genotipo haciendo validaciones sobre las subcadenas
        que lo conforman"""
        anterior = 0
        i = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i] + anterior]
            anterior += self.mj[i]
            if not self.validar_gen(sub, i):
                return False
            i += 1

        return True
