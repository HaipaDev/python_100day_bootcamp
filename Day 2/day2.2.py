weight=int(input("Your weight in kg?: \n"))
height=float(input("Your height in m?: \n"))
if(height>3): # if height in cm?
    height/=100
bmi=round(weight/(height**2),2)
print("Your BMI is: ",bmi)