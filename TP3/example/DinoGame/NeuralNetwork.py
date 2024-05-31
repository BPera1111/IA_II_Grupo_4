import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.w1 = None # Weights for the first layer
        self.b1 = None
        self.w2 = None
        self.b2 = None
        self.w3 = None
        self.b3 = None
        self.initialize(5,7,3)

    def initialize(self, input_size, hidden_size, output_size):
        # ======================== INITIALIZE NETWORK WEIGTHS AND BIASES =============================
        self.w1 = np.random.randn(input_size, hidden_size) / np.sqrt(input_size) # pesos de la primera capa 
        self.b1 = np.zeros((1, hidden_size)) # bias de la primera capa
        self.w2 = np.random.randn(hidden_size, hidden_size) / np.sqrt(hidden_size) # pesos de las capas ocultas
        self.b2 = np.zeros((1, hidden_size)) # bias de las capas ocultas
        self.w3 = np.random.randn(hidden_size, output_size) / np.sqrt(output_size) # pesos de las capas ocultas
        self.b3 = np.zeros((1, output_size)) # bias de las capas ocultas
        #np.random.randn genera una matriz de tamaño (input_size, hidden_size) con valores aleatorios de una distribución normal

    def think(self, x_obs, y_obs, h_obs, speed, y_dino):
         # ================================== NORMALIZADO =========================================
        x_obs = x_obs / 1100 #ancho de la pantalla
        y_obs = y_obs / 390 #alto de la pantalla hasta el suelo
        h_obs = h_obs / 100 #altura del obstaculo
        speed = speed / 1000
        y_dino = y_dino / 390 #alto de la pantalla hasta el suelo
        # ======================== PROCESS INFORMATION SENSED TO ACT =============================
        input = np.array([[x_obs, y_obs, h_obs, speed, y_dino]]) # Convert input parameters to a numpy array
        hidden_layer = np.maximum(0, np.dot(input, self.w1) + self.b1) # Hidden layer with ReLU activation
        hidden_layer2 = np.maximum(0, np.dot(hidden_layer, self.w2) + self.b2)
        #np.maximun 
        output = np.dot(hidden_layer2, self.w3) + self.b3 # Output layer without activation
        return self.act(output)

    def act(self, output):
        # ======================== USE THE ACTIVATION FUNCTION TO ACT =============================
        action =np.argmax(output) # Return the index of the maximum value in the output array
        if (action == 0):
            return "JUMP"
        elif (action == 1):
            return "DUCK"
        elif (action == 2):
            return "RUN"
