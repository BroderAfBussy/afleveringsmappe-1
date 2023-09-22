import numpy as np

# OPG 1 
# Importer numpy og print versionen (hint: np.version)
print(np.version)
# idk, det virker ikke.


# OPG 2
# Lav to 1-dimensionelle arrays med 6 elementer og lav elementvis addition. Print resultatet ud.
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,10,11,12])
#print(a+b)

# OPG 3
# Lav et 1-dimensionalt array og print resultatet af en multiplikation med en skalar 2.
a = np.array([1,2,3,4,5,6])
#print(2*a)

# OPG 4
a = np.array([x for x in range(81)])
# Lav nu et ny array hvor du re-dimensionerer så det består af 9 rækker og 9 kolonner. 
# Hint: brug reshape på a. Print resultatet ud.

b = np.reshape(a,(9,9))
#print(b)

# OPG 5
a = np.array([x for x in range(27)])
# Gør det samme som OPG4 men gør det til 3 matricer med hver 3 rækker og 3 kolonner.
b = np.reshape(a,(3,3,3))
#print(b)

# OPG 6
# Konverter et numpy array af decimaltal til heltal.
# Hint brug astype('int') på arrayet. Print det nye array ud.
a = np.array([1.1,2.2,3.3,4.4,5.5,6.6,7.7])
b = a.astype(int)
#print (b) #hm, bliver altid rundet ned... hvorfor mon det.

# OPG 7
# Koden konverterer 0 til false og 1 til true, så arrayet bliver fyldt med 'True'er og 'False'er

# OPG 8
# Hvad gør følgende kode?
o = np.linspace(0, 100, 5)
#print(o)
# np.linspace() deler tilsyneladende et interval [0 ; 100] op i 5 tal med samme interval imellem sig.

# OPG 9
# Spring over

# OPG 10
# Prøv at lave en en såkaldt identitetsmatrice med 1'taller på diagonalen.

#hvad er en identitetsmatrice??? 
#Nårh vent, det er den
i=np.eye(2)
i2 = np.array([[0,1],[1,0]])

k = np.array([[2,3],[4,5]])
np.dot(i,k)
np.dot(i2,k)

# hvorfor skal man bruge prikprodukt??? Mystisk. Men nu kan jeg spejlvende en matrix, så det er da cool nok


# OPG 11
# brug np.where til at undersøge om to 1D matricer har ens elementer.
# Prøv derefter a og b fra opg 9

a = np.array([3])
b = np.array([3])
#print(np.where(a==b))
# den giver mig et array med det index, hvor de er lig hinanden (tomt hvis a != b)

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
#print(np.where(a==b))
# Her er de tilsyneladende ikke ens nogen steder.

# OPG 12
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

a_transpose = a.T
print(a_transpose)