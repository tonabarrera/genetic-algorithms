#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calcularfitness import CalcFitness
from ga import GeneticAlgorithm
from poblacion import Poblacion


def iniciar():
    calcular = CalcFitness()
    calcular.precision = 10



    calcular.z = [.2, .5]
    calcular.bj = [20000, 6000]
    calcular.aj = [0, 0]
    calcular.get_mj()
    poblacion = Poblacion(3, True, calcular)
    algorithm = GeneticAlgorithm(True)
    print(poblacion)

    for i in range(50):
        poblacion = algorithm.get_next_generation(poblacion)

    print(poblacion)


iniciar()
