import smtplib
import datetime as dt
import pandas
import random


now=dt.datetime.now()
today=(now.month, now.day)

birthdays_data=pandas.read_csv("birthdays.csv")
birthdays_dict={
    (data_row["month"], data_row["day"]):data_row for (index,data_row) in birthdays_data.iterrows()
}

if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    birthday_person_name=birthday_person["name"]
    birthday_person_email=birthday_person["email"]
    random_id=random.randint(1,3)
    with open(f"letter_templates/letter_{random_id}.txt","r") as letter_file:
        letter_contents=letter_file.read().replace("[NAME]",birthday_person_name)
        
    MY_EMAIL="maciejkrefft03@gmail.com"
    PASSWORD="mwwnsttuqrcshaxu"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        
        subject=f"Happy birthday {birthday_person_name}!"
        message=letter_contents
        
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person_email,msg=f"Subject:{subject}\n\n{message}")