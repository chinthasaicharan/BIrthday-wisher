import datetime
import csv
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import random

today = datetime.datetime.now()


with open("birthdays.csv") as file:
    data = csv.reader(file)
    for row in data:
        if row[3].lstrip("0") == str(today.month) and row[4].lstrip("0") == str(today.day):
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
                letter_list = letter.readlines()
                new_letter = letter_list[0].replace("[NAME]", row[0])
                letter_list.pop(0)
                letter_list.insert(0, new_letter)
                matter = ""
                for l in letter_list:
                    matter += l
                email = "test8acc8.sai@gmail.com"
                password = "8888saich"

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(from_addr=email, to_addrs=row[1], msg=f"subject: HAPPY BIRTHDAY \n\n {matter}")
                    connection.close()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.




