import random
import math

def tanh(x):
    return math.tanh(x)

input1 = 0.05
input2 = 0.10

w1 = random.uniform(-0.5, 0.5)
w2 = random.uniform(-0.5, 0.5)
w3 = random.uniform(-0.5, 0.5)
w4 = random.uniform(-0.5, 0.5)
w5 = random.uniform(-0.5, 0.5)
w6 = random.uniform(-0.5, 0.5)
w7 = random.uniform(-0.5, 0.5)
w8 = random.uniform(-0.5, 0.5)

b1 = 0.5
b2 = 0.7

hidden1 = tanh(input1*w1 + input2*w2 + b1)
hidden2 = tanh(input1*w3 + input2*w4 + b1)

output1 = tanh(hidden1*w5 + hidden2*w6 + b2)
output2 = tanh(hidden1*w7 + hidden2*w8 + b2)

print("Output  1 =", output1)
print("Output 2 =", output2)