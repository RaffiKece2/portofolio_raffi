import  numpy as np


x = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]

              ])


y = np.array([[0] , [1] , [2] , [3]])


ukuran_input = 2
layer_neuron = 5
ukuran_output = 1
kecepatan_belajar = 0.1
learning_training = 50000

np.random.seed(42)
W1 = np.random.randn(ukuran_input,layer_neuron)
b1 = np.zeros((1, layer_neuron))
W2 = np.random.randn(layer_neuron,ukuran_output)
b2 = np.zeros((1, ukuran_output))



def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


for epoch in range(learning_training):

    z1 = np.dot(x,W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1,W2) + b2
    a2 = sigmoid(z2)

    error =  y - a2
    d_a2 = error * sigmoid_derivative(a2)
    d_a1 = np.dot(d_a2,W2.T) * sigmoid_derivative(a1)

    W2 += np.dot(a1.T,d_a2) * kecepatan_belajar
    b2 += np.sum(d_a2,axis=0,keepdims=True) * kecepatan_belajar
    W1 += np.dot(x.T,d_a1) * kecepatan_belajar
    b1 += np.sum(d_a1,axis=0,keepdims=True) * kecepatan_belajar

    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch} | Loss: {loss:.4f}")

print("Training_test: ")
print(a2)


