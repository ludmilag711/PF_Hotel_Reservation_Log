#create reservations csv file
#add AI generated data to file 

import pandas as pd
import random

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

    try: #error handling
        print(df.to_string(index=False))

    except FileNotFoundError:
        print("File not found")

    input("Press enter to continue")

#input validation 
def name_val(name):
    if name.isalpha() and len(name)>=1 and len(name)<=30: #check name has only letters and between 1 and 30 characters
        return name.title()
    else:
        print("Please input only letters, no symbols or numbers")
        return False
    
def adults_val(adults):
    if 1<= int(adults) <=4:
        return adults
    else:
        print("1 to 4 adults authorised per booking")
        return False
    
def child_val(children):
    if 0<= int(children)<=3:
        return children
    else:
        print("Maximum 3 children per booking")
        return False
    
def total_guests_val(adults, children):
    total = int(adults) + int(children)
    if 1<= total <= 4:
        return total
    else:
        print("No more than 4 guests in total per booking")
        return False
    
def children_with_adults_val(adults, children):
    if int(children)>0 and int(adults)>0:
        return True
    else:
        print("Children must be accompanied by at least 1 adult")
        return False
    
def room_val(room):
    if room.isnumeric() and len(room)>=3: #check room only has numbers and is at least 3 characters long
        return room
    else:
        print("Invalid room number")
        return False
    
def guest_type_val(guest_type):
    types = ['Leisure', 'Business', 'Walk-in', 'Conference', 'Group', 'Return Guest'] # check no other guest types inserted
    if guest_type.title() in types:
        return guest_type.title()
    else:
        print("Please only choose from the following options: Leisure, Business, Walk-in, Conference, Group, Return Guest")
        return False
    
def room_type_val(room_type):
    categories = ['twin', 'double', 'family'] #check no other room type inserted
    if room_type.lower() in categories:
        return room_type.lower()
    else:
        print("invalid room type, please choose from: twin, double or family")
        return False 
    

def family_room_val(total_guests, room_type):
    if int(total_guests)>2:  #check all bookings with more than 2 guests get family rooms 
        return room_type == "family"
    

def positive_integer_val(num): #not AI but I did google how to do this
    try:
        if int(num)>0: #check if number is and integer and bigger than 0
            return int(num)
    except ValueError:
        print("Please insert a whole positive number")
        return False

def date_val(date):  #AI generated code, searched what map does, once fully understood included in my code, only modification is adapting from yyyy-mm-dd format to dd-mm-yyyy format
    try: # DD-MM-YYYY format validation
        parts = date.split("/")
        if len(parts) != 3:
            return False
        
        day, month, year = map(int, parts)
        if 1<= day <=31 and 1<= month <=12 and 2026<= year <=2030:
            return date
    except:
        print("Please insert date in format DD/MM/YYYY")

def room_num_generator(): #random number generator in a range 
    return random.randint(101, 428)

def id_generator(file): #generate random ids that don't already exist in csv under 'id'
    existing_ids = []     #debugged here using AI as my inital approach was taking a string as an argument, took inspiration but wanted to make minimal changes to my code so didn't incorporate full solution
    with open(file, "r") as f:
        f.readline()
        for res in f:
            existing_ids.append(res.split(",")[0])

    new_id = random.randint(1, 1000)
    while str(new_id) in existing_ids:
        new_id = random.randint(1, 1000) #keep generating until number isn't in existing ids
    return new_id

def add_reservation(): # function add_reservation()

    print("Sections marked with * are mandatory")

    new_id = id_generator(file) #generate id

    first_name = name_val(input("First name* :")) #first name input
    while not first_name: #principle behind this came from asking AI how to incorporate optional and required user inputs. Minor changes only to adapt to my specific variables, fully understood
        first_name = name_val(input("First name cannot be empty :")) 

    last_name =  name_val(input("Last name* : ")) #last name input
    while not last_name: 
        last_name = name_val(input("Last name cannot be empty : ")) 

    checkin_date = date_val(input("Check-in date DD/MM/YYYY* : "))
    while not checkin_date:
        checkin_date = date_val(input("Check-in date required: "))
    
    checkout_date = date_val(input("Check-out date DD/MM/YYYY* : "))
    while not checkout_date:
        checkout_date = date_val(input("Check-out date required: "))
    
    num_nights = positive_integer_val(input("Number of nights*: "))
    while not num_nights:
        num_nights = positive_integer_val(input("Number of nights required: "))

    num_adults = adults_val(input("Number of adults*: "))
    while not num_adults:
        num_adults = adults_val(input("Number of adults required: "))
    
    while not positive_integer_val(num_adults):
        num_adults = adults_val(input("Number of adults*: "))

    num_children = child_val(input("Number of children*: "))
    while not num_children:
        num_children = child_val(input("Number of children required: "))

    while not positive_integer_val(num_children):
        num_children =  child_val(input("Number of children*: "))

    while not children_with_adults_val(num_adults, num_children):
        num_adults = adults_val(input("Number of adults*: "))
        num_children = child_val(input("Number of children*: "))

    while not total_guests_val(num_adults, num_children):
        num_adults = adults_val(input("Number of adults*: "))
        num_children = child_val(input("Number of children*: "))

    room_type = room_type_val(input("Room type preference, double, twin or family (for bookings with more than 2 guests family rooms will be assigned automatically): "))

    total = int(num_adults)+ int(num_children)
    if total>2:
        room_type = "family"
    #family_room_val(total_guests_val(num_adults, num_children), room_type)

    room_num = room_num_generator()

    guest_type= guest_type_val(input("Guest type (Leisure/ Business/ Walk-in/ Conference/ Group/ Return Guest): "))

    comments = input("Comments or special requests: ")
    
    new_reservation = f"{new_id}, {first_name.title()}, {last_name.title()}, {checkin_date}, {checkout_date}, {num_nights}, {num_adults}, {num_children}, {room_type}, {room_num}, {guest_type}, {comments}"

    with open(file, "a") as f: #add reservation to csv
        f.write(new_reservation)
    
    return new_reservation

# menu function if option == 1 add, else if option == 2 view ... 3 modify, 4 delete, 5 search, 6 break
def options():
    while True:
        choice = show_menu()

        if choice == "1":
            print("Active reservations:")
            load_reservations(file) 

        elif choice == "2":
            print("Add reservation. Press enter to skip optional fields: ")
            add_reservation()
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



# function modify_reservation()
# function delete_reservation()
# function search()

