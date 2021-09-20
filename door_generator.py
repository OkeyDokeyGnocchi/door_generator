# Generate 52 weeks worth of codes for ATL and Bonderson
import csv
import platform
import os
import random
import sys
from datetime import date, timedelta

# Generate a new set of 52
def access_nsite():
    # Check for output directory, create if needed
    current_platform = platform.system()

    if current_platform == 'Windows':
        output_directory = os.getcwd() + "\Output"
        access_output = output_directory + "\AccessNsiteCodes" + "_" + str(date.today()) + ".csv"
        remote_output = output_directory + "\RemoteLinkCodes" + "_" + str(date.today()) + ".txt"
    else:
        output_directory = os.getcwd() + "/Output"
        access_output = output_directory + "/AccessNsiteCodes" + "_" + str(date.today()) + ".csv"
        remote_output = output_directory + "/RemoteLinkCodes" + "_" + str(date.today()) + ".txt"

    check_output_exists = os.path.exists(output_directory)

    if not check_output_exists:
        os.makedirs(output_directory)

    codes = []
    while True:
        try:
            year = int(input("What is the starting year?\n"))
            month = int(input("What is the starting month? (ex: 09)\n"))
            day = int(input("What is the starting day?\n"))
            break
        except ValueError:
            print("Please enter only numbers.\n")

    start_date = date(year, month, day)

    last_name = input("What is the 'last name' you would like to use? (ex: week)\n")

    while True:
        try:
            first_name = int(input("What is the starting number for 'first name'?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    access_level = input("\nPlease enter the access level that you want added. "
                            "(Can be left blank if unsure)\n"
                            "**CENG Bonderson Events is "
                            "'+CENG Event Spaces (Bondo-Lobby,104,107,203)**'\n")

    # Set the headers
    header = [
        "Card Number", "Pin", "Personnel ID",
        "Last Name", "First Name", "Effective",
        "Expires", "Access Level"
        ]


    with open(access_output, 'w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

    while True:
        try:
            num_codes = int(input("How many codes would you like?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    while True:
        print("Would you like to Create Records[1] or Update Existing[2]?")
        access_mode = input()

        if access_mode not in ['1', '2']:
            print("Please select 1 or 2.\n")
        else:
            if access_mode == '2':
                while True:
                    print("\nPlease provide the name of the csv file with personnel "
                            "IDs to update (needs to be in the same folder as this"
                            " program and should have a single column with no header\n")
                    existing_csv = input()
                    if '.csv' not in existing_csv:
                        existing_csv += '.csv'

                    try:
                        with open(existing_csv, 'r') as f:
                            reader = csv.reader(f, delimiter=',')
                            personnel_id_list = []

                            for row in f:
                                personnel_id_list.append(row)
                        break
                    except FileNotFoundError:
                        print("File could not be found, please double check "
                            "the file name and location.")

            break


    # Make the CSV for AccessNsite
    print("\n####Creating AccessNsite csv file####\n")

    for i in range(num_codes):
        code = random.randint(10000, 99999)
        codes.append(code)

        if access_mode == '1':
            personnel_id = code
        else:
            personnel_id = personnel_id_list[i]

        # Convert date to AccessNsite format
        effective_date = start_date.strftime("%m/%d/%Y")

        # Add 6 days for the rest of the week
        expires_date = start_date + timedelta(days=6)

        # Convert to AccessNsite format
        expires_date_formatted = expires_date.strftime("%m/%d/%Y")

        data = [
            code, code, personnel_id,
            last_name, first_name, effective_date,
            expires_date_formatted, access_level
            ]

        with open(access_output, 'a', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        start_date += timedelta(days=7)
        first_name += 1

    if access_mode == '1':
        print("\n**To import new records, import into AccessNsite and load"
            " the python_generate configuration**")
    elif access_mode == '2':
        print("\n**To update records, import into AccessNsite and load"
            " the python_update configuration**")


    # Remote Link
    print("\n####Running Remote Link####\n")
    print("Please enter the starting USER # for this run\n"
            "***Make sure that there are enough open numbers in a row***\n")


    while True:
        try:
            remote_user_start = int(input("What is the starting USER #?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    remote_last_name = input("What is the 'last name' you would like to use? (ex: week)\n")

    while True:
        try:
            remote_first_name = int(input("What is the starting number for 'first name'?\n"))
            break
        except ValueError:
            print("Numbers only, please.\n")

    remote_profile = input("\nPlease enter the access level that you want added. "
                            "(Can be left blank if unsure)\n"
                            "**Keck Lab (ATL Room 2) + Lobby door is 17**\n")

    # Make the TXT file for Remote Link
    print("\n####Creating Remote Link txt file####\n")
    for i in range(num_codes):
        code = codes[i]

        with open(remote_output, 'a') as f:
            f.write(f"{remote_user_start}      {remote_last_name} {remote_first_name}  {code}   {remote_profile}\n")

        remote_first_name += 1
        remote_user_start += 1

    print("\n**To import new records, go into User Codes in Remote Link and "
        " select Batch>File Name>Import**")



if __name__ == '__main__':
    while True:
        print("#### Welcome ####\n")
        print('Would you like (1)Create codes/files or (2)Exit '
              '[1/2]')
        user_mode = input()
        if user_mode == '1':
            print("\n####Running AccessNsite####\n")
            access_nsite()
            print("\n**Files are located in the Output folder**\n")
            input("\nFinished, press any key to exit.")
            sys.exit()
        elif user_mode == '2':
            print('Exiting.\n')
            sys.exit()
        else:
            print('Please select either (1)Create codes/files or (2)Exit.\n')
