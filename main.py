import smtplib
import random
import pandas
import datetime as dt

my_email = "test@gmail.com"
password = "//////" # password not given here for obvious reasons


# getting quotes from file as lists
filename = 'quotes.txt'
f = open(filename, 'r')
lines = f.read()
lines_list = lines.splitlines()
f.close()

letters_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# reading csv using pandas and extracting dataframe
bdays_df = pandas.read_csv('birthdays.csv')
bdays_df = pandas.DataFrame(bdays_df)
print(bdays_df)

# getting current day and month
now = dt.datetime.now()
current_weekday = now.weekday()
current_month = now.month
current_day = now.day

# for each birthday in the csv, checking if the current day matches the birthday. If so, bday email is sent
for ind in bdays_df.index:
    if current_month == bdays_df['month'][ind] and current_day == bdays_df['day'][ind]:
        f = open(random.choice(letters_list), 'r')
        f_contents = f.read()
        f_contents = f_contents.replace("[NAME]", bdays_df['name'][ind])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=bdays_df['email'][ind],
                                msg='Subject:Happy Birthday' + str(bdays_df['name'][ind]) +'!' + '\n\n' + f_contents
                                )
        print("email sent!")






