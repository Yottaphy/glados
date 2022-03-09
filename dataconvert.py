import numpy as np

_,n,z,alpha,deltaalpha = np.genfromtxt("alphas.txt", skip_header=1, unpack=True)
n1,z1,halflife= np.genfromtxt("data1.csv", skip_header=1, delimiter=',', unpack=True)

dic_halflife = {}
for i in range(len(n1)):
    dic_halflife[(int(n1[i]),int(z1[i]))] = halflife[i]

#print(dic_halflife)
print('n\t z\t alphaE(keV)\t deltaAlphaE(keV)\t halflife(s)')
for i in range(len(n)):
    try:
        print(int(n[i]), int(z[i]), alpha[i], deltaalpha[i], dic_halflife[(int(n[i]), int(z[i]))])
    except:
        print(int(n[i]), int(z[i]), alpha[i], deltaalpha[i], -1)
