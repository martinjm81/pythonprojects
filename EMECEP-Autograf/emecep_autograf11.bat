echo off
CLS

:MENU
ECHO ==================================
ECHO == EMECEP Python Autograf 1.0 ===
ECHO ==================================
ECHO INSTRUCCIONES: Ejecutar este programa en la misma carpeta que el script de python
ECHO ---------------------------------
ECHO.
ECHO Digite 1, si desea instalar los paquetes de Python
ECHO Digite 2, si desea ejecutar EMECEP Autograf1.1
ECHO Digite R, para regresar al Menú Principal
ECHO Digite S, para salir.
ECHO.
SET /P M = Digite 1, 2, R ó S y luego presione ENTER:
IF %M%==1 GOTO INTALADOR
IF %M%==2 GOTO AUTOGRAF
IF %M%==R GOTO MAIN
IF %M%==S GOTO SALIR

:INSTALADOR
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
@Pause
GOTO MENU

:AUTOGRAF
@pause
python emecep_autograf10.py
@pause
GOTO MENU