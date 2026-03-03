#create reservations csv file
#add AI generated data to file 

import pandas as pd

file = "reservations.csv"
df = pd.read_csv(file) # read csv file 


def show_menu(): # function show_menu() => print options
    print("~"*40)
    print("Grand Hotel***** reservation system")
    print("~"*40)
    print("Options:")
    print("1. View all reservations")
    print("2. Create a new reservation")
    print("3. Modify reservation")
    print("4. Cancel reservation")
    print("5. Search for reservation(s)")
    print("6. Exit")
    print("~"*40)
    return input("Please choose from options 1-6 by typing the corresponding number, e.g 3 = Modify reservation: ")

def load_reservations(file): # function load_reservation() as a table 
    
    reservations =[] #empty list
    try: #error handling
        with open(file, "r") as f: #read file
            columns = f.readline().split(",") # create header by reading first line and removing commas
            reservations.append(columns)

            rows = f.read().split("\n") # split lines so it's not one long string

            for row in rows:
                values = line.split(",")
                reservations.append(values)
    except FileNotFoundError:
        print("File not found")

    input("Press enter to continue")

#input validation 
def name_val(name):
    if name.isalpha() and len(name)>=1 and len(name)<=30: #check name has only letters and between 1 and 30 characters
        return name.title()
    else:
        print("Please input only letters, no symbols or numbers")

def room_val(room):
    if room.isalnum() and len(room)>=3: #check room only has letters and numbers and is at least 3 characters long
        return room
    else:
        print("Invalid room number")

def guest_type_val(guest_type):

def room_type_val(room_type):

def integer_val(int):

def date_val(date):


# menu function if option == 1 add, else if option == 2 view ... 3 modify, 4 delete, 5 search, 6 break
def options():
   while True:
    choice = show_menu()

    if choice == "1":
        load_reservations()

    elif choice == "2":
        print("ADD FUNCTION NOT YET CREATED")
        input("Press enter to continue")

    elif choice == "3":
        print("MODIFY FUNCTION NOT YET CREATED")
        input("Press enter to continue")

    elif choice == "4":
        print("DELETE FUNCTION NOT YET CREATED")
        input("Press enter to continue")

    elif choice == "5":
        print("SEARCH FUNCTION NOT YET CREATED")
        input("Press enter to continue")

    elif choice == "6":
        print("Bye, have a great day!")
        break

    else:
        print("Invalid input, please choose a number between 1 and 6")

if __name__ == "__main__":
   options()


# create reservation dictionary
# function id_generator()
# function room_generator()
# function num_nights()
# function room_cat()
# function add_reservation()
# functions save_reservation()
# function modify_reservation()
# function delete_reservation()
# function search()

