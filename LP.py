#from tkinter import E
import numpy as np
import matplotlib.pyplot as plt

#Signal Sample
S = np.loadtxt("DataSuara.txt", usecols = 1, dtype= 'str')    
S = S.astype('float16')
Ndata = len(S)
Sample = np.arange(Ndata)

# plt.plot(Sample, S, 'r')
# plt.xlabel("Sample Number")
# plt.ylabel("Amplitude")
# plt.title("Signal Sample")
# plt.show()

#auto correlation
def signal(timelag):
    rxx = np.zeros(timelag)
    for i in range (timelag) :
        sum = 0
        for j in range (Ndata) :
            sum += S[j]*S[j-i]
        
        rxx[i] = sum
        rxx[-i] = rxx[i]

        print(f"rxx[{i}] = {rxx[i]}\n")

    return rxx, S
    
#Matrik Rxx
def Main(rxx, timelag, S):
    #Matrix
    MatrixSize = timelag
    Matrix1 = np.zeros((MatrixSize, MatrixSize))

    for i in range(MatrixSize):
        for j in range(MatrixSize):
            Matrix1[i][j] = rxx[(i-1) - (j-1)]
        
    print(Matrix1)

    #Inverse matrix
    InvMatrix1 = np.linalg.inv(Matrix1)

    #Koef Predictor (a)
    MatrixSize2 = timelag
    Matrix2 = np.zeros((1, MatrixSize2))

    for i in range(MatrixSize2):
        result = 0
        a = np.zeros(MatrixSize2)
        for j in range(MatrixSize2):
            result += InvMatrix1[j][i]*rxx[j]
   
        a[i] = result
    
        print(f"a[{i}] = {result}")

    #invers filtering
    a_inv = np.zeros(MatrixSize2)
    e = np.zeros(2000)

    for i in range(MatrixSize2):
        a_inv[i] = -a[i]

    
    #error [e(m)]
    for i in range (Ndata) :
        x_hat = 0
        for j in range(timelag):
            x_hat += (a_inv[j]*S[i-j])
        
        e[i] = S[i]+x_hat

    return e, a

def LinierPrediction(a, timelag, SJ, e):
    Ndata = 2000
    jmlh = np.arange(2000)
    x_baru = np.zeros(Ndata)
    for i in range(-timelag, 0):

        x_baru[i] = 0
        
    
    for i in range(Ndata):
        sum2 = 0
        for j in range(timelag):

            sum2 += a[j]*S[i-j]

        x_baru[i] = sum2 + e[i]
    
    # plt.plot(jmlh, x_baru)
    # plt.show()

    return x_baru

TimeLag= int(input())

Ndata = np.arange(2000)
print("Jumlah Time Lag = ")
rxx, s= signal(TimeLag)

e, a = Main(rxx, TimeLag, S)
LP = LinierPrediction(a, TimeLag, S)