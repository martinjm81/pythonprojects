print("Importando Pandas ...")
import pandas as pd
print("Importando Matplotlib ...")
import matplotlib.pyplot as plt
print("Importando Módulo Path")
import os.path
print("Importando DateTime")
import datetime
print("Módulos importados satisfactoriamente!")
variable = input("Indique el nombre de la variable: ")
año0= input("Indique el año de inicio: ")
mes0= input("Indique el mes de inicio (#): ")
añoT= input("Indique el año de fin: ")
mesT= input("Indique el mes de fin (#): ")
print("La variable es ", variable,"desde ", año0, "mes", mes0, "hasta el", añoT, "m", mesT)
data = pd.read_excel("data.xlsx")
print(data)

inicio=año0+'-'+mes0
periodos=len(data)

tiempo = pd.date_range(start=inicio, periods=periodos, freq='M')


grafico = plt.figure(figsize=(6, 4), dpi=100, facecolor='maroon')
ax = plt.axes() 
ax.set_facecolor('maroon') 
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='x', colors='white')
plt.plot(tiempo, data[variable], color="white")
plt.title('Evolución de '+ variable + ' del ' + año0 + ' al ' + añoT, color="white")
plt.ylabel(variable, color="white")
plt.xlabel('Fuente: BCRP | Elaboración: EMECEP Consultoría', color="white")
plt.show()
grafico.savefig('grafico.png')