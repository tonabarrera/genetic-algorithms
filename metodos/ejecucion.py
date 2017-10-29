#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calcularfitness import CalcFitness
from ga import GeneticAlgorithm
from poblacion import Poblacion


def iniciar():
    calcular = CalcFitness()
    calcular.precision = 0
    # Los coeficientes de z
    calcular.get_limites()
    calcular.get_mj()
    poblacion = Poblacion(10, True, calcular)
    algorithm = GeneticAlgorithm(True)
    i = 0
    print(calcular.longitud)
    for i in range(50):
        print('Poblacion: ' + str(i+1))
        print(poblacion)
        poblacion = algorithm.get_next_generation(poblacion)

    print('Poblacion: ' + str(i + 1))
    print(poblacion)


iniciar()
