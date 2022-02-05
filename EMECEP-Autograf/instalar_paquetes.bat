@echo off
ECHO ==================================
ECHO == EMECEP Python Instalador 1.0 ==
ECHO ==================================
ECHO Si aun no tiene python, ir a https://www.python.org/downloads/
ECHO A continuacion, se instalaran los paquetes MATPLOTLIB y PANDAS
@Pause
ECHO Instalando paquetes de Python. Por favor, espere ...
pip install matplotlib
pip install pandas
pip install xlrd
pip install openpyxl
@Pause