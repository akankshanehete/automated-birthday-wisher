import smtplib
import random
import pandas
import datetime as dt

my_email = "akankshanehete8@gmail.com"
password = "//////" # password not given here for security reasons


# getting quotes from file as lists
filename = 'quotes.txt'
f = open(filename, 'r')
lines = f.read()
lines_list = lines.splitlines()
f.close()


now = dt.datetime.now()
current_weekday = now.weekday()
current_month = now.month()
current_day = now.day()

if current_weekday == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nehetea@mcmaster.ca",
                            msg='Subject:Hello, Tuesday!\n\n' + random.choice(lines_list)
                            )

date_of_birth= dt.datetime(year=2002, month=9, day=29)





