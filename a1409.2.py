from re import I


n=int(input('n='))
m=int(input('m='))
if n>m:
    def factorial(x):
        f=1
        for i in range(1,x+1):
            f=f*i 
        return f
c= (factorial(n))/(factorial(m)* (factorial(n-m)))
print('c =',c)