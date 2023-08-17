import subprocess ##subprocess.run('cls',shell=True)##

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def power(n1,n2):
    return n1**n2
def root(n1,n2):
    return n1**(1/n2)
def sqrt(n1):
    return root(n1,2)
def modulo(n1,n2):
    return n1%n2
def factorial(n1):
    f=n1
    for i in range(n1-1,1,-1):
        print(i)
        f*=i
    return f

def calculate(n1,n2,operation):
    if(operation=="+"): return add(n1,n2)
    elif(operation=="-"): return subtract(n1,n2)
    elif(operation=="*"): return multiply(n1,n2)
    elif(operation=="/"): return divide(n1,n2)
    elif(operation=="^" or operation=="**" or operation=="pow"): return power(n1,n2)
    elif(operation=="√" or operation=="r" or operation=="root"): return root(n1,n2)
    elif(operation=="s" or operation=="sqrt"): return sqrt(n1)
    elif(operation=="%" or operation=="mod"): return modulo(n1,n2)
    elif(operation=="!" or operation=="fac"): return factorial(n1)

from art import logo

newCalculator=True
continueCalculator=True

while(continueCalculator or newCalculator):
    if(newCalculator):
        subprocess.run('cls',shell=True)
        print(logo)
        n1=0
        n2=0

        n1Message=""
        while(not n1Message.replace(".", "").isnumeric()):
            n1Message=input("\nInput the first number: ")
        n1=float(n1Message)
        newCalculator=False
    
    operation=""
    while(not operation=="+" and not operation=="-" and not operation=="*" and not operation=="/"
    and not operation=="^" and not operation=="**" and not operation=="pow"
    and not operation=="√" and not operation=="s" and not operation=="sqrt" and not operation=="r" and not operation=="root"
    and not operation=="%" and not operation=="mod"
    and not operation=="!" and not operation=="fac"):
        operation=input("Input the operation type (+  -  *  / \nor **[^ pow]\nor √[r root (s sqrt)]\nor %[mod]\nor ![fac]): ")

    if(not operation=="!" and not operation=="fac" and not operation=="s" and not operation=="sqrt"):
        n2Message=""
        while(not n2Message.replace(".", "").isnumeric()):
            n2Message=input("Input the second number: ")
        n2=float(n2Message)

    result=calculate(n1,n2,operation)
    if(operation=="!" or operation=="fac"):
        print(f"The result of: {n1}! = {result}")
    elif(operation=="√" or operation=="s" or operation=="sqrt" or operation=="r" or operation=="root"):
        if(not operation=="s" and not operation=="sqrt"):print(f"The result of: {n2}√{n1} = {result}")
        else: print(f"The result of: √{n1} = {result}")
    else:
        print(f"The result of: {n1} {operation} {n2} = {result}")
    n1=result

    contCalcMessage=input("\nContinue calculating? (y to continue | n to start new) ")
    if(contCalcMessage=="" or contCalcMessage=="y" or contCalcMessage=="Y" or contCalcMessage=="yes" or contCalcMessage=="Yes"):
        continueCalculator=True
    elif(contCalcMessage=="n" or contCalcMessage=="N" or contCalcMessage=="new" or contCalcMessage=="New"):
        continueCalculator=False
        newCalculator=True
    else:
        continueCalculator=False
        newCalculator=False