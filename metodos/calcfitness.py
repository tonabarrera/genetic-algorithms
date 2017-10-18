#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CalcFitness:
    """Falta el como manejar las restricciones"""
    def __init__(self, arg):
        self.z = list()  # Coeficientos de la funcion objetivo
        self.mj = list()  # Longitud de las subcadenas
        self.long = 0  # Longitud total de la cadena
        self.aj = list()  # Limite inferior
        self.bj = list()  # Limite superior
        self.precision = 0  # Precision

    def get_mj(self):
        """Obtencion de la longitud de las cadenas"""
        while i < len(z):
            aux = (self.bj[i]-self.aj[i]) * (math.pow(10, self.precision))
            mj[i] = math.ceil(math.log(aux)/math.log(2))
            self.long += mj[i]

    def get_fitness(self, string):
        """Obtine el fitness de una cadena partiendola en la longitud
        de cada variable de la funcion objetivo"""
        fitness = 0
        anterior = 0
        while i < len(self.z):
            sub = string[anterior:self.mj[i]]
            anterior = self.mj[i]
            aux = self.aj[i] + binary_to_int(sub)*((self.bj[i]-self.bj)/(2**self.mj[i])-1)
            fitness += self.z[i] * aux

    def binary_to_int(self, substring):
        """Convertir binario a decimal"""
        return int(sub, 2)

    def get_funtion(self, expresion):
        """Aqui se obtendran los coeficientes de la funcion objetivo"""
        pass

    def validate_limit(self, substring, position):
        """Aqui se validara una subcadana que cumpla las restricciones
        correspondientes"""
        pass

    def validate_all_limits(self):
        """Esta funcion se llamara cuando 
        se realice un crossover o una mutacion"""
        pass
