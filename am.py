import sys
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) > 1:
    vm = 20
    fm = 0.5
    vp = 5
    fp = 5
else:
    inp = input("Ingrese el voltaje de la moduladora: \n")
    try:
        vm = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()
    inp = input("Ingrese la frecuencia de la moduladora: \n")
    try:
        fm = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()
    inp = input("Ingrese el voltaje de la portadora: \n")
    try:
        vp = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()
    inp = input("Ingrese la frecuencia de la portadora: \n")
    try:
        fp = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()

indice_modulacion = (vm/vp)*100


def moduladora(t):
    global vm, fm
    moduladora = vm*np.sin((2*np.pi)*fm*t)
    return moduladora


def portadora(t):
    global vp, fp
    portadora = vp*np.sin((2*np.pi)*fp*t)
    return portadora


def modulada(t):
    global vp, fp, vm, fm
    m = vm/vp
    modulada = vp*np.sin((2*np.pi)*fp*t)+(((m*vp)/2)*np.cos((2*np.pi)
                                                            * (fp-fm)*t))-(((m*vp)/2)*np.cos((2*np.pi)*(fp+fm)*t))
    return modulada


x = np.linspace(0, 10, 1000)
fig, axs = plt.subplots(3, 1, constrained_layout=True, sharex=True)
fig.suptitle('Modulación AM', fontsize=16)
axs[0].plot(x, moduladora(x))
axs[0].set_title('Señal Modulada (Datos)')
axs[0].set_ylabel('Voltaje (V)')
axs[0].grid(True)
axs[1].plot(x, portadora(x))
axs[1].set_title('Señal Portadora')
axs[1].set_ylabel('Voltaje (V)')
axs[1].grid(True)
axs[2].plot(x, modulada(x))
axs[2].set_title('Señal Modulada - Indice de modulación = ' +
                 str(indice_modulacion)+"%")
axs[2].set_ylabel('Voltaje (V)')
axs[2].set_xlabel('Tiempo (s)')
axs[2].grid(True)
plt.show()
