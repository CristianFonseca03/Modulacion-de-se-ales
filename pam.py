import sys
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) > 1:
    vm = 20
    fm = 0.05
    i_m = 4
else:
    inp = input("Ingrese el voltaje de la señal: \n")
    try:
        vm = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()
    inp = input("Ingrese la frecuencia de la señal: \n")
    try:
        fm = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()
    inp = input("Ingrese la intervalo de muestreo: \n")
    try:
        i_m = float(inp)
    except ValueError:
        print("Ingrese un numero valido")
        sys.exit()

t_t = 50
x_m = []
y_v = []


def moduladora(t):
    global vm, fm
    moduladora = vm*np.sin((2*np.pi)*fm*t)
    return moduladora


def modulada():
    global i_m, t_t
    y_v.append(0)
    y_v.append(i_m)
    while(True):
        if y_v[-1] >= t_t:
            break
        else:
            y_v.append(y_v[-1]+i_m)
    for i in y_v:
        x_m.append(moduladora(i))


x = np.linspace(0, t_t, 1000)
modulada()
fig, axs = plt.subplots(2, 1, constrained_layout=True, sharex=True)
fig.suptitle('Modulación PAM', fontsize=16)
axs[0].plot(x, moduladora(x))
axs[0].set_title('Señal Modulada (Datos)')
axs[0].set_ylabel('Voltaje (V)')
axs[0].grid(True)
axs[1].stem(y_v, x_m)
axs[1].set_title('Señal Modulada')
axs[1].set_ylabel('Voltaje (V)')
axs[1].set_xlabel('Tiempo (s)')
axs[1].grid(True)
plt.show()
