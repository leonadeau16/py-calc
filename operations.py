def multiplication(a ,b=1):
    return a*b

def addition(a, b=0):
    return a + b

def soustraction(a, b=0):
    return a - b

def division(a,b=1):
    if b == 0:
        raise ZeroDivisionError
    return a/b

def power(a,b=2):
    return a**b

def root(a, b=2):
    if b==0:
        return 1
    return a**( 1/b )

def percentage(a):
    return a/100
