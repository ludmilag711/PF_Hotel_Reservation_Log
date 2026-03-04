#create reservations csv file
#add AI generated data to file 

import pandas as pd
import random

file = "reservations.csv"
df = pd.read_csv(file) # read csv file 
#the 3 lines below are AI generated as I did not understand why all of a sudden all of my integers in the csv had a .0 added at the end of them. Code is fully understood, no modifications. I pasted my code and asked why it did that.
int_columns = ["id", "num_nights", "num_adults", "num_children", "room_num"]
for col in int_columns:
    df[col] = df[col].fillna(0).astype(int)
df.to_csv(file, index=False)


def show_menu(): # function show_menu() => print options
    print("~"*40)
    print("Grand Hotel***** reservation system")
    print("~"*40)
    print("Options:")
    print("1. View all reservations")
    print("2. Create a new reservation")
    print("3. Modify reservation")
    print("4. Cancel reservation")
    print("5. Exit")
    print("~"*40)
    return input("Please choose from options 1-5 by typing the corresponding number, e.g 3 = Modify reservation: ")

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
    try: # DD/MM/YYYY format validation
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
    
    new_reservation = f"\n{int(new_id)}, {first_name.title()}, {last_name.title()}, {checkin_date}, {checkout_date}, {int(num_nights)}, {int(num_adults)}, {int(num_children)}, {room_type}, {int(room_num)}, {guest_type}, {comments}"

    with open(file, "a") as f: #add reservation to csv
        f.write(new_reservation)
    
    return new_reservation

def modify_reservation():
    """lines 212-218 were initially code generated but I initially didn't use it. I wrote my own code which was very similar but didn't have .values and 
    didn't have global df, I then added those elements in too see what was stopping my code from working. I then asked it to explaint the purpose of both
    and the generated code didn't have a loop but I wanted the program to keep asking the user for the ID until they input a correct one so added that in"""""
    global df 
    
    search_id = input("Enter the reservation ID of reservation you wish to modify: ")
    
    while search_id not in df["id"].astype(str).values:
            print("Reservation ID not found, please try again")
            search_id = input("Please enter valid reservation ID: ")

    print(f"Here are the reservation details for ID: {search_id}")    
    print(df[df["id"].astype(str) == search_id].to_string(index=False))

    print("What would you like to modify?")
    print("1. First name")
    print("2. Last name")
    print("3. Check in date")
    print("4. Check out date")
    print("5. Number of nights")
    print("6. Number of adults")
    print("7. Number of children")
    print("8. Room type")
    print("9. Room number")
    print("10. Guest type")
    print("11. Comments")

    mod = input("Enter a number between 1-11: ")

    choice_dict = { #create dictionary so users choice corresponds to column name
        "1" : "first_name",
        "2" : "last_name",
        "3" : "checkin_date",
        "4" : "checkout_date",
        "5" : "num_nights",
        "6" : "num_adults",
        "7" : "num_children",
        "8" : "room_type",
        "9" : "room_num",
        "10" : "guest_type",
        "11" : "comments"
    }

    value = choice_dict[mod] #column name corresponding to user choice

    new = ""

    if value == "first_name" or value == "last_name":
        new = name_val(input("Enter new: ")) #assign the input to the variable new
        while not new:
            new = name_val(input("Invalid, try again"))

    elif value == "checkin_date" or value == "checkout_date":
        new = date_val(input("Enter new date in DD/MM/YYYY format: "))
        while not new:
            new = date_val(input("Invalid, try again"))

    elif value == "num_nights":
        new = input("Enter number of nights: ")

    elif value == "num_adults":
        new = adults_val(input("Enter number of adults: "))
        while not new:
            new = adults_val(input("Invalid, try again"))

    elif value == "num_children":
        new = child_val(input("Enter number of children: "))
        while not new:
            new = child_val(input("Invalid, try again"))

    elif value == "room_type":
        new = room_type_val(input("Enter new room type: "))
        while not new:
            new = room_type_val(input("Invalid, try again"))
    
    elif value == "room_num":
        new = input("Enter new room number: ")

    elif value == "guest_type":
        new = guest_type_val(input("Enter guest type: "))
        while not new:
            new = guest_type_val(input("Invalid, try again"))
    
    elif value == "comments":
        new = input("Enter new comments: ") 
    
    if value in int_columns:
        df.loc[df["id"].astype(str) == search_id, value] = int(new) # for integer values converts user input to integer
    else:
        df.loc[df["id"].astype(str) == search_id, value] = new # otherwise just leaves it as a string
    
    for col in int_columns:
        df[col] = df[col].astype(int)

    df.to_csv(file, index=False)
    print(f"Reservation {search_id} successfuly updated!")

def delete_reservation():
    global df

    search_id = input("Enter the reservation ID of reservation you wish to cancel: ")
    while search_id not in df["id"].astype(str).values:
            print("Reservation ID not found, please try again")
            search_id = input("Please enter valid reservation ID: ")
    
    print("Please check the reservation details:")
    print(df[df["id"].astype(str) == search_id].to_string(index=False))

    yes_no = input("Are you sure you want to cancel this reservation?")

    if yes_no.lower() == "yes":

        index_delete = df[df["id"].astype(str) == search_id].index #locate row for pandas to drop
        df=df.drop(index_delete)
        df.to_csv(file, index=False)
        print("Reservation cancelled")

    else:
        print("Reservation not cancelled")


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
            print("Modifying reservation: ")
            modify_reservation()
            input("Press enter to continue")

        elif choice == "4":
            delete_reservation()
            input("Press enter to continue")

        elif choice == "5":
            print("Bye, have a great day!")
            break

        else:
            print("Invalid input, please choose a number between 1 and 6")

if __name__ == "__main__":
   options()


# function delete_reservation()


