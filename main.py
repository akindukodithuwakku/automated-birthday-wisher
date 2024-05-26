import datetime as dt
import random
import smtplib
import pandas as pd

# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
#
# with open("quotes.txt")as data:
#     quotes = data.readlines() #this line read the data from the data set
#     motivation = random.choice(quotes) #this line chose a random quote from the list
#     if day_of_week == 1:
#         print(motivation)
#         my_email = "akinduscience@gmail.com"
#         password = "yix"
#
#         with smtplib.SMTP("smtp.gmail.com") as connect:
#             connect.starttls()  # this will create a secure connection
#             connect.login(user=my_email , password=password)
#             connect.sendmail(from_addr=my_email ,
#                              to_addrs="akindukodithuwakku@gmail.com" ,
#                              msg=f"subject: hello akindu \n\n {motivation} ")


 # take the date time
 # take the emails , names, birthdays
 # create a connection
 # write the email

my_email = "akinduscience@gmail.com"
password = "Your password"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("userdata.csv")

# This is the format of the birthday dictionary
# birthday_dict = {
#     (birthday_month, birthday_day) : data_row
# }

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_location = f"templates/letter{random.randint(1,5)}.txt"
    with open(file_location) as birthday_wish:
        content = birthday_wish.read()
        content = content.replace("[name]" , birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],msg=f"subject: Happy Birthday!"
                                                                                      f"\n\n {content}")
