score=0
yourName=input("What is your name? ")
theirName=input("What is their name? ")

bothnames_lower=yourName.lower()+theirName.lower()

t_count=bothnames_lower.count("t")
r_count=bothnames_lower.count("r")
u_count=bothnames_lower.count("u")
e_count=bothnames_lower.count("e")
l_count=bothnames_lower.count("l")
o_count=bothnames_lower.count("o")
v_count=bothnames_lower.count("v")
e_count=bothnames_lower.count("e")

score=int(str(t_count+r_count+u_count+e_count)+str(l_count+o_count+v_count+e_count))
if score>100: score=100

if score != 0 and score != 100 and (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
elif score == 0: print("BRUH")
elif score == 100: print("You are made for each other lol")
else: print(f"Your score is {score}.")