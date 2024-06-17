import numpy as np
import matplotlib.pyplot as plt

def leakyrelu(x, alpha=0.1):
    return np.where(x > 0, x, alpha * x)

def D_leakyrelu(x, alpha=0.1):
    return np.where(x > 0, 1, alpha)


def grafica_doble(x1, y1, x2, y2):
    plt.figure()

    # Primer gráfico
    plt.subplot(2, 1, 1)
    #plt.plot(x1, y1)
    plt.scatter(x1, y1)
    plt.title('')

    # Segundo gráfico
    plt.subplot(2, 1, 2)
    #plt.plot(x2, y2)
    plt.scatter(x2, y2)
    plt.title('Regresión')

    plt.tight_layout()
    plt.show()



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
    #plt.plot(x, y, c='red')
    plt.scatter(x, y, c='blue', marker='o')
    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axhline(0, color='red',linewidth=0.5)
    plt.axvline(0, color='red',linewidth=0.5)
    plt.show()

#IO
def guardar_matrices(archivo, matrices):
    """
    Guarda varias matrices en un archivo de texto con rótulos.
    """
    with open(archivo, 'w') as f:
        for i, matriz in enumerate(matrices):
            f.write(f'matriz{i+1}\n')
            np.savetxt(f, matriz, fmt='%f')
            f.write('\n')  # Añadir una línea en blanco entre matrices

def leer_matrices(archivo):
    """
    Lee matrices desde un archivo de texto con rótulos y devuelve una lista de matrices.
    """
    matrices = []
    with open(archivo, 'r') as f:
        content = f.read().strip().split('\n')
        current_matrix = []
        for line in content:
            if line.startswith('matriz'):
                if current_matrix:
                    matrices.append(np.array(current_matrix))
                    current_matrix = []
            else:
                if line:
                    current_matrix.append(list(map(float, line.split())))
        if current_matrix:
            matrices.append(np.array(current_matrix))
    return matrices

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
W1 = W1.astype(np.float64)

B1 = np.zeros((1, n))
B1 = B1.astype(np.float64)

#W2 = np.random.uniform(-0.1, 0.1, (n, 1))
W2 = np.ones((n, 1))
W2 = W2.astype(np.float64)

B2 = np.zeros((1, 1))
B2 = B2.astype(np.float64)

epoch = 10000
lr = 0.1



def train(W1, B1, W2, B2, lr, epoch):
    ls = []
    for i in range(epoch):
        dL_dW2 = 0
        dL_dB2 = 0
        dL_dB1 = 0
        dL_dW1 = 0
        L = 0
        for j in range(X.shape[1]):
            #Forward pass
            Z = X[0][j] * W1 + B1
            A = leakyrelu(Z)
            Y = A @ W2 + B2
        
            #Back propagation
            dL_dW2 += (Y - T[0][j]) * A 
            dL_dB2 += (Y - T[0][j])

            dL_dZ1 = (Y - T[0][j]) @ W2.T * D_leakyrelu(Z)
            dL_dW1 += np.outer(dL_dZ1, X[0][j])
            dL_dB1 += dL_dZ1

            L += 0.5*(T[0][j] - Y)**2


        dL_dW2 = dL_dW2/X.shape[1]
        dL_dB2 = dL_dB2/X.shape[1]
        dL_dW1 = dL_dW1/X.shape[1]
        dL_dB1 = dL_dB1/X.shape[1]

        L = L/X.shape[1]
        print(L)
        ls.append(L)

        #Gradient descent
        W1 -= lr*dL_dW1.T
        B1 -= lr*dL_dB1
        W2 -= lr*dL_dW2.T
        B2 -= lr*dL_dB2

    return W1, B1, W2, B2, ls    


def guardar_m(W2, B2, W1, B1):
    #Guarda las matrices en un txt
    archivo = r'C:\Users\usuario\Desktop\matrices.txt'
    matrices = []
    matrices.append(W2)
    matrices.append(B2)
    matrices.append(W1)
    matrices.append(B1)
    guardar_matrices(archivo, matrices)


def test(W2, B2, W1, B1):
    archivo = r'C:\Users\usuario\Desktop\matrices.txt'
    matrices = leer_matrices(archivo)
    W2 = matrices[0]
    B2 = matrices[1]
    W1 = matrices[2]
    B1 = matrices[3]
    return W2, B2, W1, B1


#W1, B1, W2, B2, ls = train(W1, B1, W2, B2, lr, epoch)
#guardar_m(W2, B2, W1, B1)

W2, B2, W1, B1 = test(W2, B2, W1, B1)

#X = np.linspace(-3, 3, 500)
#X = X.reshape(1, 500)

Y = []
for j in range(X.shape[1]):
        #Forward pass
        Z = X[0][j] * W1 + B1
        A = leakyrelu(Z)
        Y.append(A @ W2 + B2)
        
Y = np.array(Y)
Y = Y.reshape(1, 500)       

#graficar_vectores(X, T, "Puntos")
graficar_vectores(X, Y, "Prediccion")

grafica_doble(X[0], T[0], X[0], Y[0])

#ep = np.linspace(0, epoch, epoch)
#ls = np.array(ls)
#L = ls.reshape(epoch, 1)
#ep = ep.reshape(epoch, 1)
#graficar_vectores(ep, ls)











