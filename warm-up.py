error = 0

def add(a,b):
    a=(5,6)
    b=(3,2)
    return a+b

def mul(a,b):
    a=(5,6)
    b=(3,2)
    return a*b

def sub(a,b):
    a=(5,6)
    b=(3,2)
    return a-b

def div(a,b):
    a=(5,6)
    b=(3,2)
    return a/b

def create(a,b):
    return a/b

def inp(m,n):
    from fractions import Fraction
    m=(input("M:"))
    n=(input("N:"))
    a=Fraction(m,n)
    return a

def prt(a):
    print(a)

def eq(a,b):
    from fractions import Fraction
    a=Fraction(5,6)
    a=Fraction(10,12)
    if(a==b):
        return true
    else:
        return false

def lt(a,b):
    from fractions import Fraction
    a=Fraction(5,6)
    a=Fraction(4,6)
    if(a<b):
        return true
    else:
        return false

def error(a,b):
    pritn((None,None))


