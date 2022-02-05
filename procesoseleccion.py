#procedimiento de selección
def procseleccion(data):
    promediotot = {}
    for id, x1 in data.items():
        promedio = sum(x1) / len(x1)
        promediotot[id]  = promedio

    seleccion = sorted(promediotot.values(), reverse=True)

    maxprom = seleccion[0]

    for id, promedio in promediotot.items():
        if maxprom == promedio:
            print("el código es {0} y el promedio es {1}".format(id, promedio))

if __name__ == '__main__':
	data = {2021001:[50,20,35], 2021002:[40,35,35], 2021003:[30,35,35],
			2021004:[45,40,35], 2021005: [25,30,35], 2021006:[40,45,35]}
	procseleccion(data)
