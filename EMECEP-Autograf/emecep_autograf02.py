ruta = 'C:/Users/José-Manuel/Dropbox/Python'
año0= 2003
mes0= 1
añoT= 2028
mesT= 8
variable = 'IPBI'

import os.path
import datetime
import pandas as pd
import matplotlib.pytplot as plt

inicio = datetime.datetime(año0,mes0,1)
fin = datetime.datetime(añoT,mesT,1)

os.chdir(ruta)
data = pd.read_excel("data.xls")
print(data)