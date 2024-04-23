######################
# Habit Tracker Frontend (UI)
#####################

import habit as hb 
from database import database_controller 
db = database_controller ()

#loading all habits from the database into the habit objects

def welcome_greeting ():
    print ("Hi! Welcome to the Habit Tracker")
    print (" Got any tasks done?")

def start_page():
    ''' Function to display the start page of the Habit Tracker.'''
    # Loading all required objects
    hb.load_all_habits()
    ## hier noch hb.control_time() einfügen sobald die Methode fertig ist
    # getting number of habits in order to avoid an error message
    number_of_habits = db.get_number_of_rows()
    row = 0 
    # displaying all active habits
    while row < number_of_habits:
        if db.get_number_of_rows == 0:
            print ("No habits to track. Please add a habit first.")
            break
        row += 1
        print ("1." + (hb.habit1.habit_name) + "(" +  str(hb.habit1.current_frequency) + "/" + str(hb.habit1.frequency) + ") done per " + (hb.habit1.periodicity) )
        if row == number_of_habits:
            break
        print ("2." + (hb.habit2.habit_name) + "(" +  str(hb.habit2.current_frequency) + "/" + str(hb.habit2.frequency) + ") done per " + (hb.habit2.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("3." + (hb.habit3.habit_name) + "(" +  str(hb.habit3.current_frequency) + "/" + str(hb.habit3.frequency) + ") done per " + (hb.habit3.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("4." + (hb.habit4.habit_name) + "(" +  str(hb.habit4.current_frequency) + "/" + str(hb.habit4.frequency) + ") done per " + (hb.habit4.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("5." + (hb.habit5.habit_name) + "(" +  str(hb.habit5.current_frequency) + "/" + str(hb.habit5.frequency) + ") done per " + (hb.habit5.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("6." + (hb.habit6.habit_name) + "(" +  str(hb.habit6.current_frequency) + "/" + str(hb.habit6.frequency) + ") done per " + (hb.habit6.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("7." + (hb.habit7.habit_name) + "(" +  str(hb.habit7.current_frequency) + "/" + str(hb.habit7.frequency) + ") done per " + (hb.habit7.periodicity) )
        row += 1
        if row == number_of_habits:
            break
        print ("8." + (hb.habit8.habit_name) + "(" +  str(hb.habit8.current_frequency) + "/" + str(hb.habit8.frequency) + ") done per " + (hb.habit8.periodicity) )
        print ("Maximum number of habits reached.")
        break
    print ("\n")
    print ("Press 0 for menu")
    print ("Press 9 to exit")

    #Input Handling of start page
    while True:
        try:
            choice = input("Enter your choice: ")
            choice = int(choice) 
            if   number_of_habits < choice < 9:
                print ("You have only got " + str(number_of_habits) + " habits. Try again")
                continue
            if choice == 1:
                print ("You have selected " + hb.habit1.habit_name)
                hb.Habit.check_off_habit(hb.habit1)
                db.update_habit(hb.habit1.habit_name, hb.habit1.current_frequency, hb.habit1.current_streak, hb.habit1.last_timestamp)
                continue
            if choice == 2:
                print ("You have selected " + hb.habit2.habit_name)
                hb.Habit.check_off_habit(hb.habit2)
                db.update_habit(hb.habit2.habit_name, hb.habit2.current_frequency, hb.habit2.current_streak, hb.habit2.last_timestamp)
                continue
            if choice == 3:
                print ("You have selected " + hb.habit3.habit_name)
                hb.Habit.check_off_habit(hb.habit3)
                db.update_habit(hb.habit3.habit_name, hb.habit3.current_frequency, hb.habit3.current_streak, hb.habit3.last_timestamp)
                continue
            if choice == 4:
                print ("You have selected " + hb.habit4.habit_name)
                hb.Habit.check_off_habit(hb.habit4)
                db.update_habit(hb.habit4.habit_name, hb.habit4.current_frequency, hb.habit4.current_streak, hb.habit4.last_timestamp)
                continue
            if choice == 5:
                print ("You have selected " + hb.habit5.habit_name)
                hb.Habit.check_off_habit(hb.habit5)
                db.update_habit(hb.habit5.habit_name, hb.habit5.current_frequency, hb.habit5.current_streak, hb.habit5.last_timestamp)
                continue
            if choice == 6:
                print ("You have selected " + hb.habit6.habit_name)
                hb.Habit.check_off_habit(hb.habit6)
                db.update_habit(hb.habit6.habit_name, hb.habit6.current_frequency, hb.habit6.current_streak, hb.habit6.last_timestamp)
                continue
            if choice == 7:
                print ("You have selected " + hb.habit7.habit_name)
                hb.Habit.check_off_habit(hb.habit7)
                db.update_habit(hb.habit7.habit_name, hb.habit7.current_frequency, hb.habit7.current_streak, hb.habit7.last_timestamp)
                continue
            if choice == 8:
                print ("You have selected " + hb.habit8.habit_name)
                hb.Habit.check_off_habit(hb.habit8)
                db.update_habit(hb.habit8.habit_name, hb.habit8.current_frequency, hb.habit8.current_streak, hb.habit8.last_timestamp)
                continue
            if choice == 9:
                print ("Goodbye!")
                break
            if choice == 0:
                menu()
                break
        except ValueError:
            print ("Please enter a number (not a name)")
            continue

    

                 

def menu():
    ''' Function to display the menu of the Habit Tracker.'''
    print ("MENU")
    print ("1. View Insights")
    print ("2. View Schedule")
    print ("3. View Description")
    print ("4. Add Habit")
    print ("5. Delete Habit")
    print ("\n Press 9 to go back to start page")
    
    # Input Handling of the menu
    while True:
        try: 
            menu_choice = int (input("Enter your Menu choice: "))
            if menu_choice not in [1, 2, 3, 4, 5, 9]:
                print("Invalid choice. Please enter a valid number.")
                continue
            if menu_choice == 1:
                insights()
                break
            if menu_choice == 2:
                view_schedule()
                break 
            if menu_choice == 3:
                description()
                break 
            if menu_choice == 4:
                add_habit()
                break
            if menu_choice == 5:
                delete_habit()
                break
            if menu_choice == 9:
                start_page()
                break
            
        except ValueError:
            print ("Please enter a number (not a name)")
            continue
        

# 1. View Insights
def insights():
    ''' Function to display the insights of the Habit Tracker.'''
    print ("INSIGHTS")
    print ("1. View current streak")
    print ("2. View highest streaks")
    print ("3. View average streaks")
    print ("9. Go back to menu")
    # Input Handling of the insights
    while True:
        try:
            insights_choice = int (input ("Enter your insights choice: "))
            if insights_choice == 1:
                hb.print_current_streaks()
                break
            if insights_choice == 2:
                view_highest_streaks()
                break
            if insights_choice == 3:
                view_average_streaks()
                break
            if insights_choice == 9:
                menu()
                break
        except ValueError:
            print ("Please enter a number (not a name)")
            continue

# 2. View Schedule
def view_schedule():
    ''' Function to display the schedule of the Habit Tracker.'''
    print ("SCHEDULE")
    ################


def description():
    ''' Function to display the description of the Habit Tracker.'''
    print ("DESCRIPTION")
    ######### hier noch so db.get_habit_description() oder so einfügen

def delete_habit ():
    print ("Which habit do you want to delete?")
    ########### hier fehlt auch nochs 

def add_habit():
    ''' Function to add a habit to the Habit Tracker.'''
    print ("ADD HABIT")
    ##########Hier fehlt noch viel 


######################
############ Test Area 
######################

welcome_greeting()
start_page()
