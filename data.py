import pandas as pd
import csv

#AI generated data, prompt : "generate 20 hotel reservations I can add to a csv file, here are the columns" + column names
rows = [
    ["id","first_name","last_name","checkin_date","checkout_date","num_nights","num_adults","num_children","room_type","room_num","guest_type","comments"],
    [1,"Alice","Smith","01/03/2026","03/03/2026",2,2,0,"double",201,"Leisure","High floor requested"],
    [2,"Bob","Johnson","02/03/2026","05/03/2026",3,1,1,"family",305,"Leisure","Needs baby cot"],
    [3,"Charlie","Brown","03/03/2026","04/03/2026",1,1,0,"twin",112,"Business",""],
    [4,"Diana","Taylor","04/03/2026","08/03/2026",4,2,2,"family",318,"Leisure","Near lift if possible"],
    [5,"Edward","Wilson","05/03/2026","07/03/2026",2,2,0,"double",225,"Business","Requires late check-in"],
    [6,"Fiona","Evans","06/03/2026","09/03/2026",3,2,1,"family",332,"Leisure","Allergic to feathers"],
    [7,"George","Thomas","07/03/2026","08/03/2026",1,1,0,"twin",129,"Walk-in",""],
    [8,"Hannah","Roberts","08/03/2026","11/03/2026",3,2,0,"double",248,"Conference","Near conference room"],
    [9,"Ian","Walker","09/03/2026","10/03/2026",1,1,0,"twin",104,"Business","Early check-out"],
    [10,"Julia","Hall","10/03/2026","13/03/2026",3,2,2,"family",309,"Leisure","Needs baby cot"],
    [11,"Liam","Smith","11/03/2026","12/03/2026",1,2,0,"double",217,"Leisure",""],
    [12,"Olivia","Johnson","12/03/2026","15/03/2026",3,1,0,"twin",138,"Business","Quiet room requested"],
    [13,"Noah","Brown","13/03/2026","16/03/2026",3,2,1,"family",321,"Leisure","Allergic to feathers"],
    [14,"Emma","Taylor","14/03/2026","15/03/2026",1,1,0,"double",234,"Walk-in",""],
    [15,"James","Wilson","15/03/2026","18/03/2026",3,2,0,"double",203,"Business","Late arrival"],
    [16,"Ava","Evans","16/03/2026","19/03/2026",3,2,2,"family",315,"Group","Connecting rooms requested"],
    [17,"William","Thomas","17/03/2026","18/03/2026",1,1,0,"twin",121,"Business",""],
    [18,"Sophia","Roberts","18/03/2026","20/03/2026",2,2,0,"double",229,"Leisure","Anniversary stay"],
    [19,"Henry","Walker","19/03/2026","22/03/2026",3,2,1,"family",304,"Leisure","Near lift if possible"],
    [20,"Mia","Hall","20/03/2026","22/03/2026",2,1,0,"twin",117,"Walk-in",""],
]

#add data to + automatically create csv file
 with open("reservations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows) 

#see if worked
data = pd.read_csv("reservations.csv")
print(data.head(8))