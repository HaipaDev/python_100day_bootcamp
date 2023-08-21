# import smtplib

MY_EMAIL="maciejkrefft03@gmail.com"
PASSWORD="mwwnsttuqrcshaxu"
DUMMY_EMAIL="maciejkrefft003@outlook.com"

# #smtplib.SMTP("smtp.live.com",port=587)
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL,password=PASSWORD)
    
#     subject="Sup"
#     message="Sup"
    
#     connection.sendmail(from_addr=MY_EMAIL,to_addrs=DUMMY_EMAIL,msg=f"Subject:{subject}\n\n{message}")



# import datetime as dt

# now=dt.datetime.now()
# year=now.year
# month=now.month
# day_of_week=now.weekday()
# print(day_of_week)

# date_of_birth=dt.datetime(year=2003,month=9,day=10,hour=16)
# print(date_of_birth)



import smtplib
import datetime as dt
import random

with open("quotes.txt","r") as quotes_file:
    quotes=quotes_file.readlines()
random_quote=random.choice(quotes)

now=dt.datetime.now()
weekday=now.weekday()

if weekday==0:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        
        subject="Motivational quote for today"
        message=random_quote
        
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=DUMMY_EMAIL,msg=f"Subject:{subject}\n\n{message}")