############# INSTALACIÓN DE PAQUETES ####### (Sólo instalar si no lo tiene ya)
#pip install wooldridge
#pip install statsmodels

############# IMPORTACIÓN DEL PAQUETE Y DATOS ########
import wooldridge
#wooldridge.data()
wooldridge.data('barium', description=True)
data = wooldridge.data('barium')
impclo_chn = data['chnimp'] 

############ ANALISIS PRELIMINAR ####
import matplotlib.pyplot as plt
plt.plot(impclo_chn)
plt.show()

############ ESTACIONARIEDAD #######

import statsmodels.tsa.stattools as tstest
tstest.adfuller(impclo_chn)

###### TRANSFORMACIONES #####
import numpy as np
impclo_chn1 = np.log(impclo_chn)
impclo_chn2 = np.sqrt(impclo_chn)
impclo_chn3 = np.diff(impclo_chn)
adfuller(impclo_chn1)
adfuller(impclo_chn2)
adfuller(impclo_chn3)

import statsmodels.graphics.tsaplots as tsplot
tsplot.plot_acf(impclo_chn3)
plt.show()
tsplot.plot_pacf(impclo_chn3)
plt.show()

########### ESTIMACIÓN #######
model.fit()
results.aic
results.bic
results.plot_diagnostics()
results.summary()
results.get_forecast()
