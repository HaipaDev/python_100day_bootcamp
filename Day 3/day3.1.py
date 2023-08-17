inputNum=int(input("What number to check odd or even? "))

if inputNum%2==0: even=True
else: even=False

if even: print(f"{inputNum} is an even number.")
else: print(f"{inputNum} is an odd number.")