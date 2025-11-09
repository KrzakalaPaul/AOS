import numpy as np

###### Magic and dispell probabilities ######
 
rolls1 = np.random.randint(1, 7, size=(10000,2)).sum(axis=1) 
rolls2 = np.random.randint(1, 7, size=(10000,2)).sum(axis=1)

for t in range(2, 13):
    print(f'Proba that roll1 >= roll2 AND roll 1 >= {t}:', np.mean((rolls1 >= rolls2) & (rolls1 >= t)))


###### Charges probabilities ######

rolls1 = np.random.randint(1, 7, size=(10000,2)).sum(axis=1) 

for t in range(2, 13):
    print(f'Proba that rroll 1 >= {t}:',np.mean(rolls1 >= t))
