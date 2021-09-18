# Generate 52 weeks worth of codes for ATL and Bonderson
import csv
import random
from datetime import date, timedelta

# Generate a new set of 52
def main():
    while True:
        try:
            year = int(input("What is the starting year?\n"))
            month = int(input("What is the starting month?\n"))
            day = int(input("What is the starting day?\n"))
            break
        except ValueError:
            print("Please enter only numbers.\n")

    start_date = date(year, month, day)

    last_name = input("What is the last name you would like to use? (ex: week)\n")

    while True:
        try:
            first_name = int(input("What is the starting number for first name?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    access_level = input("Please enter the access level that you want added.\n")

    # Set the headers
    header = [
        "Card Number", "Pin", "Personnel ID",
        "Last Name", "First Name", "Effective",
        "Expires", "Access Level"
        ]

    with open("codes2021.csv", 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    while True:
        try:
            num_codes = int(input("How many codes would you like?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    # Make the 52
    for i in range(num_codes):
        code = random.randint(10000, 99999)

        # Convert date to AccessNsite format
        effective_date = start_date.strftime("%m/%d/%Y")

        # Add 6 days for the rest of the week
        expires_date = start_date + timedelta(days=6)

        # Convert to AccessNsite format
        expires_date_formatted = expires_date.strftime("%m/%d/%Y")

        data = [
            code, code, code,
            last_name, first_name, effective_date,
            expires_date_formatted, access_level
            ]

        with open("codes2021.csv", 'a', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        start_date += timedelta(days=7)
        first_name += 1


if __name__ == '__main__':
    while True:
        print('Would you like (1)Remote Link, (2)AccessNsite, or '
              '(3)Exit? [1/2/3]')
        user_mode = input()
        if user_mode == '1':
            print("TODO Update existing.\n")

            print("To update records, import into AccessNsite and load"
                " the python_update configuration.")
            break
        elif user_mode == '2':
            print("Running Generate New.\n")
            main()
            print("To import new records, import into AccessNsite and load"
                " the python_gen configuration.")
            print("Finished, quitting.")
            exit()
        elif user_mode == '3':
            print('Exiting.\n')
            exit()
        else:
            print('Please select either (1)Remote Link, (2)AccessNsite, or '
                  '(3)Exit.\n')
