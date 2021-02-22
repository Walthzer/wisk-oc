#de 'import' commando's importeren modules in het programma. Modules zijn extra verzamelingen met commando's die een specifiek doel dienen, bijvoorbeeld het genereren van willekeurige getallen.

import random    #genereert willekeurige getallen
import time     #meet de tijd
from counting import bubbleSort as Algorithm #hier zit het gekozen algoritme waarvan de gemiddelde complexiteit wordt berekend.
import numpy as np #helpt bij regressie
from sklearn.linear_model import LinearRegression #voert regressies uit
import math #voor additionele wiskundige operaties
import threading #voor parallel uitvoeren functies

#Sla de start tijd op zodat de totale duratie van het programma gerapporteerd kan worden.
starttime = time.time()

#de volgende drie commanod's stellen rijen voor
invoergrootte = []  #bevat straks invoergroottes van lijsten waarop gekozen algoritme wordt uitgevoerd, in toenemende volgorde
uitvoertijd = []    #bevat straks alle uitvoertijden van elke keer dat het gekozen algoritme wordt uitgevoerd, in toenemende volgorde
R_values = []       #bevat straks alle R^2 waarden die door de regressies worden berekend.

for i in range(5,1000,3):
    invoergrootte.append(i) #voegt invoergroottes toe van lijsten die straks worden gebruikt voor uitvoering gekozen algoritme


def listcreator(x): #Deze functie genereert willekeurige lijsten van grootte naar keuze

    A = []
    for i in range(x):
        i = random.randint(1,100)
        A.append(i)
    return A 

#functie gaat tot hier




#in onderstaande code wordt herhaaldelijk het gekozen algoritme uitgevoerd op willekeurig gegenereerde lijsten. De grootte van de lijsten wordt steeds
#uit de lijst 'invoergrootte' gekozen. Bij elke uitvoering wordt ook de tijd gemeten en deze tijd wordt aan 'uitvoergrootte' toegevoegd.
for i in range(5,1000,3):
    begin = time.time()
    Algorithm(listcreator(i))
    end = time.time()
    uitvoertijd.append(end - begin)     

#hier komt de lineaire regressie
    
InputSize = np.array(invoergrootte).reshape((-1,1))   #invoergrootte wordt naar een kolommatrix genaamd InputSize omgezet, wat straks nodig is voor de regressie.
ProcessTime = np.array(uitvoertijd)                   #uitvoergrootte wordt naar een rij genaamd ProcessTime omgezet die in combinatie met de kolommatrix kan worden gebruikt.

#hier wordt de lineaire regressie opgebouwd
def linear():
    Line = LinearRegression(fit_intercept = False)#genereert het regressie-algoritme, zit in de module gebouwd.
    Line.fit(InputSize, ProcessTime)#hier voert die de regressie daadwerkelijk uit. InputSize dient als rij met x-waarden en ProcessTime als rij met y-waarden.
    linear_R = Line.score(InputSize, ProcessTime)#berekening R^2 waarde
    R_values.append(linear_R)#Toevoeging waarde aan R_values
    return linear_R
  
#kwadratische regressie, ook met sklearn
def quadrat():
    InputSize_squared = []
    for i in invoergrootte:
        InputSize_squared.append(i * i) #elk element in InputSize wordt gekwadrateerd en toegevoegd aan InputSize_squared. Zo kan met InputSize_squared
        #als rij met x-waarden, en ProcessTime als rij met y-waarden, in feite weer een lineaire regressie uitgevoerd worden. Het enige verschil is nu dat 
        #hoe dichter die R^2-waarde in die proces bij de 1 zit, hoe groter de kans dat het gekozen algoritme een kwadratische complexiteit heeft.

    InputSize_totde2de = np.array(InputSize_squared).reshape((-1,1))#Zelfde principe als bij omzetting InputSize naar kolommatrix

    Quadratic = LinearRegression(fit_intercept = False)
    Quadratic.fit(InputSize_totde2de, ProcessTime)
    Quadratic_R = Quadratic.score(InputSize_totde2de, ProcessTime)
    #zelfde principe als bij lineaire regressie
    R_values.append(Quadratic_R)#R^2 waarde berekenen van kwadratische regressie
    return Quadratic_R



#logaritmische regressie, deze regressie heeft dezelfde werking als bij de kwadratische regressie, alleen wordt nu van elke invoergrootte het logaritme genomen 
#met grondtal 2. Grondtal 2 werd gekozen omdat de meeste logaritmische algoritmes een complexiteit hebben van log n met als grondtal 2.
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



#exponentiele regressie, weer zelfde principe als bij kwadratische regressie.
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

#linearitmische regressie, ook deze regressie werkt op dezelfde manier als de kwadratische regressie. Uit deze regressie kan bepaald worden of het gekozen
#algoritme een complexiteit heeft van n maal log n, met als grondtal 2. 
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


#de daadwerkelijke uitvoering van alle algoritmes.
threading.Thread(target=linear).start()
threading.Thread(target=quadrat).start()
threading.Thread(target=logarithm).start()
threading.Thread(target=expo).start()
threading.Thread(target=linarithm).start()


Rs = np.array(R_values)
comps = ["n", "n^2", "log (n)", "2^n", "n * log(n)"]    #rij met mogelijke complexiteiten
confidence = np.amax(Rs)    #hier wordt de grootste R^2-waarde gekozen.
complexity = ""

for i in range(len(R_values)):
    if R_values[i] == confidence:
        complexity = comps[i]
    else:
        continue

print("------Took {}------".format(time.time() - starttime))    #Toon de totale tijd die het programma nodig had.
print("the time complexity of this algorithm is {} with an R^2 value of {}".format(complexity, confidence))   #dit commando toont de uitkomst van het programma
