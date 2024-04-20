######################
# Habit Tracker Frontend (UI)
#####################

import habit as hb 
from database import database_controller 
db = database_controller ()

#loading all habits from the database into the habit objects
#hb.load_all_habits(db)

def start_page():
    ''' Function to display the start page of the Habit Tracker.'''

    print ("Hi! Welcome to the Habit Tracker")
    print (" Got any tasks done?")
    row = 0 
    while row < db.get_number_of_rows():
        if row == 0:
            print ("No habits to track. Please add a habit first.")
            break
    #################Hier weitermachen, Logik passt noch nicht

    print ("1." + (hb.habit1.habit_name) + "(" +  str(hb.habit1.current_frequency) + "/" + str(hb.habit1.frequency) + ") done. Due " + (hb.habit1.periodicity) )
    print 


def menu():
    ''' Function to display the menu of the Habit Tracker.'''
    print ("1. View Insights")
    print ("2. View Description")
    print ("3. Add Habit")
    print ("4. Remove Habit")
    print ( )

start_page()
menu () 