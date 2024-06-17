import numpy as np
import matplotlib.pyplot as plt

def leakyrelu(x, alpha=0.1):
    return np.where(x > 0, x, alpha * x)

def D_leakyrelu(x, alpha=0.1):
    return np.where(x > 0, 1, alpha)

def relu(x):
    return np.maximum(0, x)

def D_relu(x):
    return np.where(x > 0, 1, 0)

sigm = (lambda x: 1 / (1 + np.exp(-x)), lambda x: x * (1 - x))

def graficar_vectores(x, y, titulo):

    if isinstance(x, np.ndarray) and x.ndim == 2 and x.shape[0] == 1:
        x = x.flatten()
    else:
        x = x

    if isinstance(y, np.ndarray) and y.ndim == 2 and y.shape[0] == 1:
        y = y.flatten()
    else:
        y = y

    plt.figure(figsize=(12, 6))
    #plt.plot(x, y)
    plt.scatter(x, y, c='blue', marker='o')
    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(0, color='red',linewidth=0.5)
    plt.axvline(0, color='red',linewidth=0.5)
    plt.show()


def leer_vectores(archivo):
    vectores = []
    with open(archivo, 'r') as f:
        for line in f:
            line = line.strip().replace('(', '').replace(')', '')
            coords = tuple(map(float, line.split(',')))
            vectores.append(coords)

    x = []
    y = []
    for i in vectores:
        x.append(i[0])
        y.append(i[1])
    
    return x, y

archivo = r'C:\Users\usuario\Desktop\puntos_catedra.txt'
X, T = leer_vectores(archivo)

X = np.array(X)
T = np.array(T)

X = X.reshape(1, len(X))
T = T.reshape(1, len(T))

n = 10
W1 = np.random.uniform(-0.1, 0.1, (1, n))
#W1 = np.ones((1, n))
W1 = W1.astype(np.float64)

B1 = np.zeros((1, n))
B1 = B1.astype(np.float64)


W2 = np.random.uniform(-0.1, 0.1, (n, 5))
#W2 = np.ones((n, 5))
W2 = W2.astype(np.float64)

B2 = np.zeros((1, 5))
B2 = B2.astype(np.float64)

W3 = np.random.uniform(-0.1, 0.1, (5, 1))
#W3 = np.ones((5, 1))
W3 = W3.astype(np.float64)

B3 = np.zeros((1, 1))
B3 = B3.astype(np.float64)

epoch = 3000
lr = 0.1
ls = []

for i in range(epoch):
    dL_dW1 = 0
    dL_dB1 = 0
    dL_dW2 = 0
    dL_dB2 = 0
    dL_dW3 = 0
    dL_dB3 = 0
    L = 0
    for j in range(X.shape[1]):  
        #Forward pass
        Z1 = X[0][j] * W1 + B1
        A1 = leakyrelu(Z1)
        Z2 = A1 @ W2 + B2
        A2 = leakyrelu(Z2)
        Y = A2 @ W3 + B3.T

        #Back propagation
        dL_dW3 += (Y - T[0][j]) * A2 
        dL_dB3 += (Y - T[0][j])

        dL_dZ2 = (Y - T[0][j]) @ W3.T * D_leakyrelu(Z2)
        dL_dW2 += np.outer(dL_dZ2, A1)
        dL_dB2 += dL_dZ2

        dL_dZ1 = dL_dZ2 @ W2.T * D_leakyrelu(Z1)
        dL_dW1 += np.outer(dL_dZ1, X[0][j])

        L += 0.5*(T[0][j] - Y)**2


    dL_dW3 = dL_dW3/X.shape[1]
    dL_dB3 = dL_dB3/X.shape[1]
    dL_dW2 = dL_dW2/X.shape[1]
    dL_dB2 = dL_dB2/X.shape[1]
    dL_dW1 = dL_dW1/X.shape[1]
    dL_dB1 = dL_dB1/X.shape[1]

    L = L/X.shape[1]
    #print(L)
    ls.append(L)

    #Gradient descent
    W1 -= lr*dL_dW1.T
    B1 -= lr*dL_dB1
    W2 -= lr*dL_dW2.T
    B2 -= lr*dL_dB2
    W3 -= lr*dL_dW3.T
    B3 -= lr*dL_dB3

    
Y = []
for j in range(X.shape[1]):
        #Forward pass
        Z1 = X[0][j] * W1 + B1
        A1 = leakyrelu(Z1)
        Z2 = A1 @ W2 + B2
        A2 = leakyrelu(Z2)
        Y.append(A2 @ W3 + B3.T)

Y = np.array(Y)
Y = Y.reshape(1, 500)       

graficar_vectores(X, T, "")
graficar_vectores(X, Y, "Predicción")

ls = np.array(ls)
ls = ls.reshape(epoch, 1)
ep = np.linspace(0, epoch, epoch)
ep = ep.reshape(epoch, 1)

graficar_vectores(ep, ls, "Función de pérdida")