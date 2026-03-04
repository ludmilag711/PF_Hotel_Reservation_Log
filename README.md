# Grand Hotel Reservation System
A reservation management system for hotel staff, built in Python using pandas. Supports creating, viewing, modifying and cancelling guest reservations, stored in a CSV file.

## Requirements

- Python 3.14
- Pandas 

Insall in terminal:

pip install pandas

## Setup

1. Clone or download project files 
2. Ensure reservations.csv is in the same directory as the script
3. Run the program - run main.py

## Features 

1. View all reservations - Displays all current reservations in a formatted table.
2. Create a new reservation - Prompts staff to enter new reservation details. Fileds marked with * are mandatory and those that are not can be skipped by pressing enter. New reservation is then added to the end of the csv file.
3. Modify reservation - Reservation must be searched by reservation ID and the detail that needs modifying must be chosen and change must be input by the staff. Modification replaces previous value in csv.
4. Cancel reservation - Reservation must be searched by reservation ID after which details of the reservation will display. Details should then be reviewed and intention to cancel must be confirmed. The reservation is then permanently removed from csv.

## Validation rules 

- Fist and last names must be letters only.
- Dates must be in DD/MM/YYYY format
- Adults must be integers between 1 and 4 per booking
- Children must be integers beween 0 and 3 per booking
- Children must be accompanied by at leats 1 adult
- Total number of guests should not exceed 4
- Room type family is automatically attributed to booking with more than 2 guests 
- Guest type amd room type are restricted to predefined options 

## Notes

- All data is added, manipulated or deleted to/from the reservations.csv file
- Reservation IDs and room numbers are automatically generated
- When modifying a reservation not all validation rules apply, this is intenional to allow staff the freedom needed to adapt to various situations. For example if 2 adults and 1 child are booked in the staff may override the room category from family to double as perhaps the child just needs a baby cot.
- The program will run as a continuous loop until the user selects option 5 to exit the program.
