#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calcularfitness import CalcFitness
from ga import GeneticAlgorithm
from poblacion import Poblacion


def iniciar():
    calcular = CalcFitness()
    calcular.precision = 10
    # Los coeficientes de z
    calcular.z = [.1, .07]
    calcular.get_limites()
    calcular.get_mj()
    poblacion = Poblacion(6, True, calcular)
    algorithm = GeneticAlgorithm(True)
    print(poblacion)

    for i in range(100):
        poblacion = algorithm.get_next_generation(poblacion)

    print(poblacion)


iniciar()
