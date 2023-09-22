import numpy as np
import matplotlib.pyplot as plt


# OPG 1
# Lav en grundlæggende linjegraf med nogle fiktive datapunkter
plt.figure(1)
plt.plot([1,4,3,4])
plt.xlabel("noget")
plt.ylabel("noget andet")

plt.figure(2)
plt.grid(True)
x = np.arange(0,2*np.pi,0.2)
plt.plot(x,np.sin(x))




# OPG 2 
# Opret et stolpediagram med priser for forskellige produkter.
plt.figure(3)
x = ["stol","lampe","bord"]
y = [100,50,200]
plt.bar(x,y)
plt.xlabel("produkt")
plt.ylabel("pris (DKK)")

# OPG 3
# Opret et cirkeldiagram der viser fordelingen af emner i en undersøgelse
plt.figure(4)
x = np.random.rand(3)
farve = np.random.rand(100)
plt.pie(x,labels=["mad","vand", "Jens"])

# OPG 4 
# Lav en linjestilkurve

#Jeg ved ikke hvad en linjestilkurve er.


# OPG 5
# Lav et stablet stolpediagram med flere datasæt
plt.figure(5)
x = ["A" , "B" , "C" , "D"]
y1 = [1,2,3,4]
y2 = [2,4,3,5]
plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')

# OPG 6
# Opret en linjetabel

#Jeg ved ikke hvad en linjetabel er, og det gør google heller ikke.

# OPG 7
# Lav et scatterplot med tilfældige datapunkter
plt.figure(7)
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x,y)

# OPG 8
# Opret et histogram over en samling af forskellige tal.
plt.figure(8)
plt.hist(x)

# OPG 9
# Lav et cirkeldiagram og vis fordelingen af kategorier i en samling af data.

# Jeg forstår ikke opgavebeskrivelsen.

# OPG 10
# Opret et vandret stolpediagram med navn


# Skjul tidligere opgavers plots
for i in range(1,7):
    plt.close(i)
plt.show()


