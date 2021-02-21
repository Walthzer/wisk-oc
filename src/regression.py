import random
import time
import matplotlib.pyplot as plt
from Algorithm_File import Algorithm
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import threading


invoergrootte = []
uitvoertijd = []
R_values = []

for i in range(5,1000,3):
    invoergrootte.append(i)


def listcreator(x):

    A = []
    for i in range(x):
        i = random.randint(1,100)
        A.append(i)
    return A







for i in range(5,1000,3):
    begin = time.time()
    Algorithm(listcreator(i))
    end = time.time()
    uitvoertijd.append(end - begin)     


InputSize = np.array(invoergrootte).reshape((-1,1))
ProcessTime = np.array(uitvoertijd)








#hier komt de lineaire regressie
def linear():
    Line = LinearRegression(fit_intercept = False)
    Line.fit(InputSize, ProcessTime)
    linear_R = Line.score(InputSize, ProcessTime)
    R_values.append(linear_R)
    return linear_R
#kwadratische regressie, ook met sklearn
def quadrat():
    InputSize_squared = []
    for i in invoergrootte:
        InputSize_squared.append(i * i)

    InputSize_totde2de = np.array(InputSize_squared).reshape((-1,1))

    Quadratic = LinearRegression(fit_intercept = False)
    Quadratic.fit(InputSize_totde2de, ProcessTime)
    Quadratic_R = Quadratic.score(InputSize_totde2de, ProcessTime)

    R_values.append(Quadratic_R)
    return Quadratic_R
#logaritmische regressie


def logarithm():
    InputSize_logarithmic = []
    for i in invoergrootte:
        InputSize_logarithmic.append(math.log2(i))

    InputSize_logged= np.array(InputSize_logarithmic).reshape((-1,1))

    logaritmic = LinearRegression(fit_intercept = False)
    logaritmic.fit(InputSize_logged, ProcessTime)
    logaritmic_R = logaritmic.score(InputSize_logged, ProcessTime)

    R_values.append(logaritmic_R)
    return logaritmic_R
#exponentiele regressie

def expo():
    InputSize_exponential = []
    for i in invoergrootte:
        InputSize_exponential.append(2 ** i)

    InputSize_exp= np.array(InputSize_exponential).reshape((-1,1))

    exponential = LinearRegression(fit_intercept = False)
    exponential.fit(InputSize_exp, ProcessTime)
    exponential_R = exponential.score(InputSize_exp, ProcessTime)

    R_values.append(exponential_R)
    return exponential_R

#linearitmische regressie
def linarithm():
    InputSize_linar= []
    for i in invoergrootte:
        InputSize_linar.append(i * math.log2(i))

    InputSize_linearitmic= np.array(InputSize_linar).reshape((-1,1))

    linearitmic = LinearRegression(fit_intercept = False)
    linearitmic.fit(InputSize_linearitmic, ProcessTime)
    linearitmic_R = linearitmic.score(InputSize_linearitmic, ProcessTime)

    R_values.append(linearitmic_R)
    return linearitmic_R

threading.Thread(target=linear).start()
threading.Thread(target=quadrat).start()
threading.Thread(target=logarithm).start()
threading.Thread(target=expo).start()
threading.Thread(target=linarithm).start()


Rs = np.array(R_values)
comps = ["n", "n^2", "log (n)", "2^n", "n * log(n)"]
REEE = np.amax(Rs)
answer = ""
for i in range(len(R_values)):
    if R_values[i] == REEE:
        answer = comps[i]
    else:
        continue

print("the time complexity of this algorithm is " + answer + "with an R^2 value of" + str(REEE))

