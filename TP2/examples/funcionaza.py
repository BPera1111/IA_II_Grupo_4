import numpy as np
from matplotlib import pyplot as plt

def vec_medio(inicio, fin, dominio):    
    #armar vector que abarque todo el dominio y sea triangular desde inicio hasta fin
    medio = np.zeros(len(dominio))
    for i in range(len(dominio)):
        if dominio[i] <= inicio:
            medio[i] = 0
        elif dominio[i] >= fin:
            medio[i] = 0
        elif dominio[i] < (inicio + fin)/2:
            medio[i] = 2*(dominio[i] - inicio)/(fin - inicio)
        else:
            medio[i] = 2*(fin - dominio[i])/(fin - inicio)
    return medio

def vec_extremo(inicio, fin, dominio,lado):    
    #armar vector que sea 1 en uno de los extremos y 0 en el otro, yendo la diagonal desde inicio hasta fin(valor 1 a 0)
    if lado=='izq':
        extremo = np.zeros(len(dominio))
        for i in range(len(dominio)):
            if dominio[i] <= inicio:
                extremo[i] = 1
            elif dominio[i] >= fin:
                extremo[i] = 0
            else:
                extremo[i] = 1 - (dominio[i] - inicio)/(fin - inicio)
        return extremo
    elif lado=='der':
        extremo = np.zeros(len(dominio))
        for i in range(len(dominio)):
            if dominio[i] <= inicio:
                extremo[i] = 0
            elif dominio[i] >= fin:
                extremo[i] = 1
            else:
                extremo[i] = (dominio[i] - inicio)/(fin - inicio)
        return extremo

def cut(value, mf):
    value = float(value)
    aux = np.zeros(mf.size)
    if (type(value) is int) or (type(value) is float):
        for i in range(mf.size):
            aux[i] = min(value, mf[i])
        return aux
    else:
        return -1

def union(data):
    aux = np.zeros(data[0].size)
    for j in range(len(data)):
        for i in range(aux.size):
            aux[i] = max(aux[i], data[j][i])
    return aux

def defuzz(y, mf, option):
    if option == 'centroid':
        num = 0
        den = 0
        for i in range(y.size):
            num = num + y[i]*mf[i]
            den = den + mf[i]
        y0 = num/den
        return y0
    
    elif option == 'bisector':
        area = 0
        aux = 0
        for i in range(y.size - 1):
            area = area + (y[i+1] - y[i]) * ((mf[i+1] + mf[i])/2)
        for i in range(y.size):
            aux = aux + (y[i+1] - y[i]) * ((mf[i+1] + mf[i])/2)
            if (aux >= area/2):
                return y[i]
        
    elif option == 'MOM':
        mf_max = max(mf)
        acum = 0
        n = 0
        for i in range(y.size):
            if (mf[i] == mf_max):
                acum = acum + y[i]
                n = n + 1
        return acum/n

    elif option == 'SOM':
        mf_max = max(mf)
        for i in range(y.size):
            if (mf[i] == mf_max):
                return y[i]
        
    elif option == 'LOM':
        mf_max = max(mf)
        for i in range(y.size):
            if (mf[y.size - i -1] == mf_max):
                return y[y.size - i -1]
            
    else:
        return -1
    
        
def anashe(pos,vel):
    # Variables de entrada
    #pos = 0.5
    #vel = -0.2

    # Conjuntos difusos
    # Define tus conjuntos difusos aquí
    dominio_pos = np.linspace(-180, 180, 3600)
    dominio_vel = np.linspace(-20,20,400)
    rango_fuerza=10
    dominio_fuerza = np.linspace(-rango_fuerza,rango_fuerza,400)

    pos_z = vec_medio(-45, 45, dominio_pos)
    pos_np = vec_medio(-90, 0, dominio_pos)
    pos_ng = vec_extremo(-90, -45, dominio_pos,'izq')
    pos_pp = vec_medio(0, 90, dominio_pos)
    pos_pg = vec_extremo(45, 90, dominio_pos,'der')
 

    vel_z = vec_medio(-5, 5, dominio_vel)
    vel_np = vec_medio(-10, 0, dominio_vel)
    vel_ng = vec_extremo(-10, -5, dominio_vel,'izq')
    vel_pp = vec_medio(0, 10, dominio_vel)
    vel_pg = vec_extremo(5, 10, dominio_vel,'der')


    fuerza_z = vec_medio(-0.25*rango_fuerza, 0.25*rango_fuerza, dominio_fuerza)
    fuerza_np = vec_medio(-0.50*rango_fuerza, 0, dominio_fuerza)
    fuerza_ng = vec_extremo(-0.50*rango_fuerza, -0.25*rango_fuerza, dominio_fuerza,'izq')
    fuerza_pp = vec_medio(0, 0.50*rango_fuerza, dominio_fuerza)
    fuerza_pg = vec_extremo(0.25*rango_fuerza, 0.50*rango_fuerza, dominio_fuerza,'der')

    #fuzzificar: encontrar la pertencnec ade pos a cada conjunto difuso de entrada
    pert_pos_z = np.interp(pos, dominio_pos, pos_z)
    pert_pos_np = np.interp(pos, dominio_pos, pos_np)
    pert_pos_ng = np.interp(pos, dominio_pos, pos_ng)
    pert_pos_pp = np.interp(pos, dominio_pos, pos_pp)
    pert_pos_pg = np.interp(pos, dominio_pos, pos_pg)

    pert_vel_z = np.interp(vel, dominio_vel, vel_z)
    pert_vel_np = np.interp(vel, dominio_vel, vel_np)
    pert_vel_ng = np.interp(vel, dominio_vel, vel_ng)
    pert_vel_pp = np.interp(vel, dominio_vel, vel_pp)
    pert_vel_pg = np.interp(vel, dominio_vel, vel_pg)

    #Reglas de inferencia
    # Define tus reglas de inferencia aquí
    FZ=[min(pert_pos_z, pert_vel_z)]
    FPP=[min(pert_pos_z, pert_pos_np), min(pert_pos_np, pert_vel_pg)]
    FPG=[min(pert_pos_ng, pert_vel_ng),min(pert_pos_ng, pert_vel_np),min(pert_pos_ng, pert_vel_z),min(pert_pos_np, pert_vel_ng),min(pert_pos_np,pert_vel_np),min(pert_pos_np, pert_vel_z),min(pert_pos_np, pert_vel_pp),min(pert_pos_z,pert_vel_ng),min(pert_pos_pg, pert_vel_ng),min(pert_pos_pg,pert_vel_np)]
    FNP=[min(pert_pos_pp, pert_vel_ng),min(pert_pos_z, pert_vel_pp)]
    FNG=[min(pert_pos_ng, pert_vel_pp),min(pert_pos_ng, pert_vel_pg),min(pert_pos_z, pert_vel_pg),min(pert_pos_pp, pert_vel_np),min(pert_pos_pp,pert_vel_z),min(pert_pos_pp, pert_vel_pp),min(pert_pos_pp, pert_vel_pg),min(pert_pos_pg,pert_vel_z),min(pert_pos_pg, pert_vel_pp),min(pert_pos_pg,pert_vel_pg)]


    fuerza_z_c = cut(FZ[0],fuerza_z)
    fuerza_pp_c = cut(max(FPP),fuerza_pp)
    fuerza_pg_c = cut(max(FPG),fuerza_pg)
    fuerza_np_c = cut(max(FNP),fuerza_np)
    fuerza_ng_c = cut(max(FNG),fuerza_ng)
    fuerza=union([fuerza_z_c,fuerza_pp_c,fuerza_pg_c,fuerza_np_c,fuerza_ng_c])
    # plt.plot(dominio_fuerza,fuerza, label='Fuerza')
    # plt.show()
    algo=defuzz(dominio_fuerza,fuerza,'centroid')
    print("\n\n\n\n\nPRINTIANTO ALGO: \n\n\n\n",algo)
    return algo


