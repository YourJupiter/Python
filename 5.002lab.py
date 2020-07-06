import itertools
import math

def my_sqrt(a,n,Epsilon):
    term1=(a+n-1)/2
    term2=(2/3)*term1 +(a/(3*term1**2))
    k=1
    while (abs(term2- term1) > Epsilon):
        term1=term2;
        term2=((k-1)/k)* term1 + a/(k*(term1**(k-1)))
        k+=1
        return term2
    
print(" х ", ": "," y ", " : "," yt", " : "," error " )
print("-- ")
Epsilon=0.0001
a=0.1;b=1
for i in itertools.count(start=a, step=0.2):
    if i>b: break
    n=3
    y= my_sqrt(i,n,Epsilon)
    y1=i**(1/n) # точне значення функції
    error=abs(y-y1)
    print('%.2f' %i, ":", '%.4f' %y, " : ", '%.4f' %y1, " :", '%.4f' %error)
