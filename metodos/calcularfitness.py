#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


class CalcFitness:

    SIGNOS = {'IGUAL': 0, 'MENOR': 1, 'MAYOR': 2, 'MENOR_IGUAL':3, 'MAYOR_IGUAL':4}

    def __init__(self):
        self.z = list()  # Coeficientos de la funcion objetivo
        self.mj = list()  # Longitud de las subcadenas
        self.longitud = 0  # Longitud total de la cadena
        self.aj = list()  # Limite inferior
        self.bj = list()  # Limite superior
        self.precision = 0  # Precision
        self.productos = list()  # Lista que guardara los valores de (bj-aj)/(2**mj-1)
        self.etiquetas = ['A', 'B', 'C', 'D']
        self.restriciones = [{'valores': [.1, .6, 0, 0, 2000], 'signo': 3},
                             {'valores': [1, 1, 0, 0, 6000], 'signo': 3},
                             {'valores': [1, 0, 0, 0, 4000], 'signo': 3}]  # Lista de restricciones


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

    def validar_cadena(self, string):
        coeficientes = [0] * 4
        i = 0
        anterior = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i] + anterior]
            anterior += self.mj[i]
            coeficientes[i] =self.obtener_coeficiente(i, sub)
            i += 1
        #print('EVALUACION')
        #print(coeficientes)
        for r in self.restriciones:
            evaluacion = (r['valores'][0] * coeficientes[0]) + (r['valores'][1] * coeficientes[1])
            evaluacion += (r['valores'][2] * coeficientes[2]) + (r['valores'][3] * coeficientes[3])
            if r['signo'] == CalcFitness.SIGNOS['IGUAL']:
                if not evaluacion == r['valores'][4]:
                    return False
            elif r['signo'] == CalcFitness.SIGNOS['MAYOR']:
                if not evaluacion > r['valores'][4]:
                    return False
            elif r['signo'] == CalcFitness.SIGNOS['MENOR']:
                if not evaluacion < r['valores'][4]:
                    return False
            elif r['signo'] == CalcFitness.SIGNOS['MENOR_IGUAL']:
                if not evaluacion <= r['valores'][4]:
                    return False
            else:
                if not evaluacion >= r['valores'][4]:
                    return False
        return True
