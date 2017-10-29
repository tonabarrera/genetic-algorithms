# Caso 1
20 y 10
self.z = [1, 1]  # Coeficientos de la funcion objetivo

self.restricciones += [{'variables': [2, 1, 0, 0], 'limite': 20, 'signo': 3},
                       {'variables': [1, 1, 0, 0], 'limite': 10, 'signo': 4}, ]  # Lista de restricciones
# Caso 2
65 y 0
No poner una de no negatividad
self.z = [1, 1, 1]
self.restricciones += [{'variables': [1, 0, 1, 0], 'limite': 50, 'signo': 3},
                               {'variables': [2, 1, 0, 0], 'limite': 75, 'signo': 3},
                               {'variables': [1, 0, -1, 0], 'limite': 10, 'signo': 4},
                               {'variables': [0, 0, 1, 0], 'limite': -5, 'signo': 4}, ]  # Lista de restricciones
# Caso 3
100 y 40
self.z = [1, -1, 1, 1]  # Coeficientos de la funcion objetivo

self.restricciones += [{'variables': [1, 1, 0, 0], 'limite': 30, 'signo': 3},
                               {'variables': [1, 0, 0, 1], 'limite': 40, 'signo': 3},
                               {'variables': [1, 1, 1, 1], 'limite': 100, 'signo': 0},]  # Lista de restricciones
# Caso 4
125 y -70
self.z = [1, 1, -2, 1]  # Coeficientos de la funcion objetivo
self.restricciones += [{'variables': [1, 0, 1, 0], 'limite': 50, 'signo': 3},
                       {'variables': [0, 1, 0, 1], 'limite': 75, 'signo': 3},
                       {'variables': [1, 0, 0, 0], 'limite': 10, 'signo': 4},
                       {'variables': [0, 1, 0, 1], 'limite': 100, 'signo': 3},]  # Lista de restricciones