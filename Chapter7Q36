#chapter 7 Question 36 
from decimal import Decimal
hbar= 1.054571800*10**-34
h= 6.62606979*10**-34
deltat=[4.2*10**-3, 2.5*10**-3, 3*10**-3, 3.7*10**-3, 5*10**-3]
deltaE=[hbar/(2*x) for x in deltat]
#print(deltaE)
#deltaE1 to deltaE4 repesents all the distractors for the four instances
deltaE1=[h/(2*x*10**3) for x in deltat]
#print(deltaE1)
deltaE2=[h/(2*x) for x in deltat]
#print(deltaE2)
deltaE3=[h/(x) for x in deltat]
#print(deltaE3)
deltaE4=[hbar/(x) for x in deltat]
#print(deltaE4)
#Each line represents an instance where the first number represents the key, followed by four distractors
for i in range(len(deltat)):
    print("%.1E" %deltaE[i], "%.1E" %deltaE1[i], "%.1E" %deltaE2[i], "%.1E" %deltaE3[i], "%.1E" %deltaE4[i])
