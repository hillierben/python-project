import re
import sys
import datetime
import csv


def main():

    # check for command-line arg
    if len(sys.argv) == 3 and sys.argv[1] == "search":
        search_contact(sys.argv[2])
        sys.exit(0)
    elif len(sys.argv) == 4 and sys.argv[1] == "search":
        search_contact(f"{sys.argv[2]}-{sys.argv[3]}")
        sys.exit(0)
    elif len(sys.argv) == 2 or len(sys.argv)> 3:
        print("Invalid command-line-arg")
        sys.exit(1)
    else:
        pass

    # create contact dictionary
    contact = {}

    # prompt user for contact information
    name = name_split(input("Name: "))
    contact = {
        "first": name[0],
        "last": name[1]
    }
    contact["email"] = check_email(input("Email: "))
    contact["mobile"] = check_number(input("Number: "))
    
    # write contact to csv file
    update_csv(contact)
    print("Contact Details Updated")


def name_split(name):
    """separate name to first, last"""
    try:
        f, l = name.title().split(" ")
        list = [f, l]
    except ValueError:
        print("Invalid name")
        sys.exit(1)

    return list


def check_number(number):
    """check mobile is valid"""
    if len(number) != 11 or number[0] != '0':
        print("invalid number")
        sys.exit(1)
    return number


def check_email(email):
    """confirm email is valid"""
    try:
        echeck = re.search(r"(\w+)@(\w+\.)?\w+\.(com|co\.uk|ac\.uk|edu)", email)
        confirm = echeck.group(0)
    except:
        print("Invalid Email")
        sys.exit(1)
        
    return confirm


def update_csv(contact):
    try:
        with open("contacts.csv", "a") as file:
            # fieldnames = ["first_name", "last_name", "email", "mobile", "date_added"]
            writer = csv.DictWriter(file, contact.keys())
            writer.writerow(contact)
        
        return True
    except:
        print("Could not update Contacts")
        sys.exit(1)


def search_contact(name):
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        try:
            first, last = name.title().split("-")
            for row in reader:
                if first == row[0] or last == row[1]:
                    print(row)
        except:
            person = name.title()
            for row in reader:
                if person == row[0] or person == row[1]:
                    print(row)


if __name__ == "__main__":
    main()


