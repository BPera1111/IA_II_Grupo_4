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

def corte(value, mf):
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
    if option == 'centroid': # default option centroid, bisector, MOM, SOM, LOM
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
            
