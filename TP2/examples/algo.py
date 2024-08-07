import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from funcionaza import *
CONSTANTE_M = 2 # Masa del carro
CONSTANTE_m = 1 # Masa de la pertiga
CONSTANTE_l = 1 # Longitud dela pertiga

# Simula el modelo del carro-pendulo.
# Parametros:
#   t_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   theta_0: Angulo inicial (grados)
#   v_0: Velocidad angular inicial (radianes/s)
#   a_0: Aceleracion angular inicial (radianes/s2)
def simular(t_max, delta_t, theta_0, v_0, a_0):
  theta = (theta_0 * np.pi) / 180
  v = v_0
  a = a_0

  # Simular
  y = []
  x = np.arange(0, t_max, delta_t)

  for t in x:
    a = calcula_aceleracion(theta, v)
    print("Tiempo: ",t)
    print("angulo: ",theta*180/np.pi)
    print("velocidad: ",v)
    v = v + a * delta_t
    theta = theta + v * delta_t + a * np.power(delta_t, 2) / 2
    y.append(theta)


  	
  # fig, ax = plt.subplots()
  # # fig.suptitle("Pendulo")
  # ax.plot(x, y)

  # ax.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(delta_t) + " s")
  # ax.grid()
  
  # plt.show()  
  return x,y
  

# Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
def calcula_aceleracion(theta, v): 
    f=anashe(theta*180/np.pi,v*180/np.pi)
    fuerza=-f
    numerador = constants.g * np.sin(theta) + np.cos(theta) * ((-fuerza - CONSTANTE_m * CONSTANTE_l * np.power(v, 2) * np.sin(theta)) / (CONSTANTE_M + CONSTANTE_m))
    denominador = CONSTANTE_l * (4/3 - (CONSTANTE_m * np.power(np.cos(theta), 2) / (CONSTANTE_M + CONSTANTE_m)))
    return numerador / denominador


#x1,y1 = simular(50, 0.1, 45, 0, 0)

#x2,y2 = simular(50, 0.01, 45, 0, 0)

x3,y3 = simular(50, 0.001, -150, 0, 0)

#x4,y4 = simular(50, 0.0001, 45, 0, 0)


fig, (ax1, ax2,ax3,ax4) = plt.subplots(4)
fig.suptitle(' Pendulos ')

# ax1.plot(x1, y1, '.', label='simulación 1',markersize=1)
# ax2.plot(x2, y2, '.', label='simulación 2',markersize=1)
ax3.plot(x3, y3, '.', label='Simulación 3',markersize=1)
# ax4.plot(x4, y4, '.', label='Simulación 4',markersize=1)
ax1.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(0.1) + " s")
ax2.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(0.01) + " s")
ax3.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(0.001) + " s")
ax4.set(xlabel='time (s)', ylabel='theta', title='Delta t = ' + str(0.0001) + " s")
plt.show(block=False)

input("Press Enter to continue...")