'''
https://www.estadistica.net/Algoritmos2/pau-programacion.pdf


'''
from ortools.sat.python import cp_model

#Inicializamos el modelo y el solucionador
modelo = cp_model.CpModel()
solucionador = cp_model.CpSolver()
#Variables
'''EN ESTE PROBLEMA VAMOS A TRABAJAN EN TONELADAS'''
piensoA = modelo.NewIntVar(1, 6, "piensoA")
piensoB = modelo.NewIntVar(1, 4, "piensoB")

#Restricciones
modelo.Add(piensoB <= 2*piensoA)
modelo.Add(2*piensoA + piensoB >= 4)

#Epresión a optimizar
modelo.Minimize(1000*piensoA + 2000*piensoB)

#Accionamos el solucionador
estado = solucionador.Solve(modelo)

#Solución
if estado == cp_model.OPTIMAL:
  print("**********************Solución**********************")
print()
print("El valor óptimo es:")
print(f'pienso A = {solucionador.Value(piensoA)}')
print(f'pienso B = {solucionador.Value(piensoB)}')