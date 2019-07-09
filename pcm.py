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
intervalos_f = []
bin_fin = []


def moduladora(t):
    global vm, fm
    moduladora = vm*np.sin((2*np.pi)*fm*t)
    return moduladora


def intervalos():
    global vm, intervalos_f
    inicio = -(vm+0.5)
    final = vm + 0.5
    intervalos_f = np.linspace(inicio, final, 8)


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


def binario():
    global x_m, y_v, intervalos_f, bin_fin
    j = 0
    for i in x_m:
        if i >= intervalos_f[0] and i <= intervalos_f[1]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 1 = 001")
            bin_fin.append(0)
            bin_fin.append(0)
            bin_fin.append(1)
        elif i >= intervalos_f[1] and i <= intervalos_f[2]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 2 = 010")
            bin_fin.append(0)
            bin_fin.append(1)
            bin_fin.append(0)
        elif i >= intervalos_f[2] and i <= intervalos_f[3]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 3 = 011")
            bin_fin.append(0)
            bin_fin.append(1)
            bin_fin.append(1)
        elif i >= intervalos_f[3] and i <= intervalos_f[4]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 4 = 100")
            bin_fin.append(1)
            bin_fin.append(0)
            bin_fin.append(0)
        elif i >= intervalos_f[4] and i <= intervalos_f[5]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 5 = 101")
            bin_fin.append(1)
            bin_fin.append(0)
            bin_fin.append(1)
        elif i >= intervalos_f[5] and i <= intervalos_f[6]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 6 = 110")
            bin_fin.append(1)
            bin_fin.append(1)
            bin_fin.append(0)
        elif i >= intervalos_f[6] and i <= intervalos_f[7]:
            print("[ "+str(y_v[j])+" , "+str(i) +
                  " ] esta en el intervalo 7 = 111")
            bin_fin.append(1)
            bin_fin.append(1)
            bin_fin.append(1)
        j = j + 1


x = np.linspace(0, t_t, 1000)
fig, axs = plt.subplots(2, 1, constrained_layout=True, sharex=True)
fig.suptitle('Modulación PCM', fontsize=16)
intervalos()
modulada()
binario()
axs[0].plot(x, moduladora(x))
axs[0].set_title('Señal Modulada (Datos)')
axs[0].set_ylabel('Voltaje (V)')
axs[0].grid(True)
axs[1].plot(x, moduladora(x), color='m', linestyle='dotted')
for i in intervalos_f:
    axs[1].axhline(y=i, color='k', linestyle='dotted')
axs[1].stem(y_v, x_m)
axs[1].set_title('Señal Modulada')
axs[1].set_ylabel('Voltaje (V)')
axs[1].set_xlabel('Tiempo (s)')
axs[1].grid(True)
print("*"*100)
print(bin_fin)
print("*"*100)
plt.show()
