@echo off
TITLE Modulaciones
MODE con:cols=80 lines=40

:inicio
SET var=0
cls
echo ******************************************************************************
echo.
echo                            %DATE% ^| %TIME% 
echo.
echo ******************************************************************************
echo.
echo                                Modulaciones:
echo.
echo ******************************************************************************
echo.
echo  1)    AM      
echo  2)    FM      
echo  3)    ASK     
echo  4)    FSK     
echo  5)    PSK  
echo  6)    PAM  
echo  7)    PCM    
echo  8)    Salir
echo.
echo ******************************************************************************
echo.

SET /p var= ^> Seleccione una opcion [1-8]: 

if "%var%"=="0" goto inicio
if "%var%"=="1" goto op1
if "%var%"=="2" goto op2
if "%var%"=="3" goto op3
if "%var%"=="4" goto op4
if "%var%"=="5" goto op5
if "%var%"=="6" goto op6
if "%var%"=="7" goto op7
if "%var%"=="8" goto salir

echo. El numero "%var%" no es una opcion valida, por favor intente de nuevo.
echo.
pause
echo.
goto:inicio

:op1
    echo.
    echo. Modulacion AM
    echo.
        python am.py
    echo.
    pause
    goto:inicio

:op2
    echo.
    echo. Modulacion FM
    echo.
        python fm.py
    echo.
    pause
    goto:inicio

:op3
    echo.
    echo.Modulacion ASK
    echo.
        python ask.py
    echo.
    pause
    goto:inicio
   
:op4
    echo.
    echo. Modulacion FSK
    echo.
        python fsk.py
    echo.
    pause
    goto:inicio

:op5
    echo.
    echo. Modulacion PSK
    echo.
        python psk.py
    echo.
    pause
    goto:inicio

:op6
    echo.
    echo. Modulacion PAM
    echo.
        python pam.py
    echo.
    pause
    goto:inicio

:op7
    echo.
    echo. Modulacion PCM
    echo.
        python pcm.py
    echo.
    pause
    goto:inicio

:salir
    @cls&exit