def importarbcr():
  import pandas as pd
  import requests
  from io import StringIO
  import random
  from datetime import datetime
  from google.colab import files
  import numpy as np
  nombre = input("Ingrese el nombre corto de variable BCRP (sin espacios): ")
  variable = input("Ingrese el código de variable BCRP (PN####NM): ")
  inicio = input("Ingrese la fecha de inicio (AAAA-MM): ")
  fin = input("Ingrese la fecha de fin (AAAA-MM): ")
  link = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/"+variable+"/csv/"+inicio+"/"+fin
  global datos
  datos = pd.read_csv(StringIO(requests.get(link, verify=True).text.replace("<br>","\n").strip()))
  datos = datos.iloc[:,[1]]; datos.columns = [nombre]
  datos.index = pd.date_range(start = inicio, freq = "ME", periods = len(datos))
  datos_log = np.log(datos); datos_log.columns = ['log_' + col for col in datos_log.columns]
  datos = pd.concat([datos, datos_log], axis=1)
  datos_diff = datos.diff(); datos_diff.columns = ['d_' + col for col in datos_diff.columns]
  datos = pd.concat([datos, datos_diff], axis=1)
  display(datos)
  return datos