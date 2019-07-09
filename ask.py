import sys
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) > 1:
    entrada = "P"
    vp = 5
    fp = 5
else:
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
    inp = input("Ingrese una letra: \n")
    try:
        entrada = str(inp)
    except ValueError:
        print("Ingrese una letra")
        sys.exit()

char = ord(entrada[0])
char_bin = bin(char)[2:]
char_list = [int(char_bin[0])]
for i in range(len(char_bin)):
    char_list.append(int(char_bin[i]))


def portadora(t):
    global vp, fp
    port = vp*np.sin((2*np.pi)*fp*t)
    return port


def modulada(t):
    global char_list, vp, fp
    if t < 1:
        if char_list[1] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 1 and t < 2:
        if char_list[2] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 2 and t < 3:
        if char_list[3] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 3 and t < 4:
        if char_list[4] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 4 and t < 5:
        if char_list[5] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 5 and t < 6:
        if char_list[6] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 6 and t < 7:
        if char_list[7] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 7 and t < 8:
        if char_list[8] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 8 and t < 9:
        if char_list[9] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 9 and t < 10:
        if char_list[10] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 10 and t < 11:
        if char_list[11] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 11 and t < 12:
        if char_list[12] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 12 and t < 13:
        if char_list[13] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 13 and t < 14:
        if char_list[14] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    elif t > 14 and t < 15:
        if char_list[15] == 1:
            mod = vp*np.sin((2*np.pi)*fp*t)
        else:
            mod = 0
    else:
        mod = 0
    return mod


x = np.linspace(0, len(char_list)-1, 1000)
x_2 = np.arange(0, len(char_list))
fig, axs = plt.subplots(3, 1, constrained_layout=True, sharex=True)
fig.suptitle('Modulación ASK', fontsize=16)
axs[0].plot(x, portadora(x))
axs[0].set_title('Portadora')
axs[0].set_ylabel('Voltaje (V)')
axs[0].grid(True)
axs[1].step(x_2, char_list)
axs[1].set_title("'"+entrada+"' --> "+str(char)+" ---> "+char_bin)
axs[1].grid(True)
modulada = np.vectorize(modulada)
axs[2].plot(x, modulada(x))
axs[2].set_title('Modulada')
axs[2].set_ylabel('Voltaje (V)')
axs[2].set_xlabel('Tiempo (s)')
axs[2].grid(True)
plt.show()
