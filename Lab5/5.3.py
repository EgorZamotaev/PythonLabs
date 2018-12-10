import matplotlib.pyplot as plt
import numpy as np

zita = float(input("Введите значение коэффициента затухания: "))
T = float(input("Введите значение коэффициента времени: "))
k = float(input("Введите значение коэффициента k: "))

omega = np.arange(0, 10, 0.001)
phi = np.arctan((-2 * zita * T * omega)/(1 - T ** 2 * omega ** 2))
w0 = np.nonzero(omega == (1 / T))[0][0]
phi = phi * 180 / np.pi
phi[w0:] = phi[w0:] - 180
for i in range(len(omega)-1):
    if -phi[i+1]+phi[i] > 10:
        phi[i+1] = phi[i]

amplituda = k / np.sqrt((1 - T ** 2 * omega ** 2) ** 2 + 4 * zita ** 2 * T ** 2 * omega ** 2)

plt.subplots(figsize=(16, 12))
plt.subplot(121)
plt.plot(omega, amplituda)
plt.title("АЧХ")
plt.xlabel("$\omega$")
plt.ylabel("$A(\omega)$")
plt.grid(True)
plt.subplot(122)
plt.plot(omega, phi)
plt.title("ФЧХ")
plt.xlabel("$\omega$")
plt.ylabel("$\phi(\omega)$")
plt.grid(True)
plt.show()
