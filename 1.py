#chapter 7 Question 32 
from decimal import Decimal
hbar= 1.054571800*10**-34
h= 6.62606979*10**-34
alphamass=6.64424*10**-27
deltav=[0.01*10**-3, 0.0150*10**-3, 0.0200*10**-3, 0.0250*10**-3, 0.0300*10**-3]
deltam=[hbar/(2*alphamass*x) for x in deltav]
#print(deltam)
deltam1=[hbar/(alphamass*x) for x in deltav]
#print(deltam1)
deltam2=[h/(2*alphamass*x) for x in deltav]
#print(deltam2)
deltam3=[h/(alphamass*x) for x in deltav]
#print(deltam3)
deltam4=[h/(2*10**-3*alphamass*x) for x in deltav]
#print(deltam4)
#Each line represents an instance where the first number represents the key, followed by four distractors
for i in range(len(deltav)):
    print("%.4E" %deltam[i], "%.4E" %deltam1[i], "%.4E" %deltam2[i], "%.4E" %deltam3[i], "%.4E" %deltam4[i])
