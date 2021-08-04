import datetime as dt
import pandas
import random
import smtplib
now=dt.datetime.now()
today_month=now.month
today_day=now.day
today = (today_month, today_day)
My_email="******"
password="*****"
data=pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if (today_month, today_day) in birthday_dict:
    britday_person=birthday_dict[today]
    letter_number=random.randint(1,3)
    with open(f"letter_templates\letter_{letter_number}.txt","r") as letterfile:
        contents=letterfile.read()
        letter=contents.replace("[NAME]",britday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(My_email,password)
        connection.sendmail(
            from_addr=My_email,
            to_addrs=britday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{letter}"
        )


