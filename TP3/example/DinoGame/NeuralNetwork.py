import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.w1 = None # Weights for the first layer
        self.w2 = None # Weights for the second layer
        self.w3 = None # Weights for the third layer
        self.b1 = None # Biases for the first layer
        self.b2 = None # Biases for the second layer
        self.b3 = None # Biases for the third layer
        self.initialize()

    def initialize(self):
        # ======================== INITIALIZE NETWORK WEIGTHS AND BIASES =============================
        self.w1 = np.random.rand(3, 3) # hace una matriz de 3x3 con valores random entre 0 y 1
        self.b1 = np.random.rand(3) # hace un vector de 3 con valores random entre 0 y 1
        self.w2 = np.random.rand(3, 3) # hace una matriz de 3x3 con valores random entre 0 y 1
        self.b2 = np.random.rand(3) # hace un vector de 3 con valores random entre 0 y 1
        self.w3 = np.random.rand(3, 3) # hace una matriz de 3x3 con valores random entre 0 y 1
        self.b3 = np.random.rand(3) # hace un vector de 3 con valores random entre 0 y 1
        # ============================================================================================

    def think(self,posx,speed,posy):
        # ======================== PROCESS INFORMATION SENSED TO ACT =============================
        input = np.array([posx, speed, posy])
        z1 = np.dot(self.w1, input) + self.b1 # hace el producto punto de w1 y el input y le suma b1 ej de 3x3 * 3x1 = 3x1 + 3x1 = 3x1
        a1 = self.relu(z1)
        z2 = np.dot(self.w2, a1) + self.b2
        a2 = self.relu(z2)
        z3 = np.dot(self.w3, a2) + self.b3
        output = z3
        #manito angora no entiendo nada
        
        # ========================================================================================
        return self.act(output)
    
    def relu(self, x):
        for i in range(len(x)):
            if x[i] < 0:
                x[i] = 0
        return x
        

    def act(self, output):
        # ======================== USE THE ACTIVATION FUNCTION TO ACT =============================
        action = np.argmax(output)
        # =========================================================================================
        if (action == 0):
            return "JUMP"
        elif (action == 1):
            return "DUCK"
        elif (action == 2):
            return "RUN"
