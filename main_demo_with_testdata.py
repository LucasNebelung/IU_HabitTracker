######################
### USER INTERFACE ###
#####################

import habit as hb 
import database as db
import analytics as a
import time
import datetime as dt
from habit import today

################# 

def start_page ():
    ''' Function to display the start page of the Habit Tracker.'''
    # Loading all required objects
    hb.load_all_habits()
    # getting number of habits in order to avoid an error message
    number_of_habits = a.get_number_of_rows()
    row = 0 
    # displaying all active habits
    print ("\n")
    if number_of_habits == 0:
            print ("No habits to track. Please add a habit first.")
    else:
        habit_info = a.get_all_habit_info()
        for i, habit in enumerate(habit_info, start=1):
            name, current_frequency, frequency, periodicity = habit
            print(f"{i}.{name}({current_frequency}/{frequency}) done per {periodicity}")

    print ("\n")
    print ("Press the number of the habit you want to check off.")
    print ("Press 'reload' to reload the page")
    print ("Press 0 for menu")
    print ("Press 9 to exit")

    #Input Handling of start page
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice == "reload":
                start_page()
                break
            choice = int(choice) 
            if   number_of_habits < choice < 9:
                print ("You have only got " + str(number_of_habits) + " habits. Try again")
                continue
            elif choice > 9:
                print ("Invalid number. Please try again.")
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
                print ("Exiting program...")
                exit()
            if choice == 0:
                menu()
                break
        except ValueError:
            print ("Please enter a number (not a name)")
            continue

    

                 

def menu():
    ''' Function to display the menu of the Habit Tracker.'''
    print ("\n")
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
    print ("\n")
    print ("INSIGHTS")
    print ("1. View current streak")
    print ("2. View highest streaks")
    print ("3. View average streaks")
    print ("\n")
    print ("Please note: a streak is defined as the successful completion of one habit for a given period (e.g. day or week).")
    print ("Press 9 to go back to menu")
    # Input Handling of the insights
    while True:
        try:
            insights_choice = int (input ("Enter your insights choice: "))
            if insights_choice == 1:
                print ("\n")
                print ("CURRENT STREAKS")
                current_streaks = a.get_current_streaks()
                for habit in current_streaks:
                    print(f"{habit[0]}  {habit[1]}")
                print ("\n")
                print ("Please note: Streaks for habits completed today or this week will be updated the following day or week.")
                print ("      Going back to insights...")
                time.sleep(2)
                insights()
                break
            if insights_choice == 2:
                print ("\n")
                print ("HIGHEST STREAKS")
                highest_streaks = a.get_highest_streaks()
                #sorts the list from highest to lowest 
                highest_streaks = sorted(highest_streaks, key=lambda x: x[1], reverse=True)   
                for streak in highest_streaks:
                    print (streak[0] + " " + str(streak[1]))
                highest_overall_streak = highest_streaks[0]
                print ("\n")
                
                print("Your highest overall streak is: " + str(highest_overall_streak[0]) + " with a streak of " + str(highest_overall_streak[1]))
                highest_streak_by_periodicity = a.get_highest_streaks_by_periodicity()
                #sorting them by periodicity
                highest_weekly_habits = [habit for habit in highest_streak_by_periodicity if habit[1] == 'week']
                highest_daily_habits = [habit for habit in highest_streak_by_periodicity if habit[1] == 'day']
                #sorting them by highest streak
                highest_weekly_habits = max(highest_weekly_habits, key=lambda habit: habit[2])
                highest_daily_habits = max(highest_daily_habits, key=lambda habit: habit[2])

                # printing the results
                print(f"Your highest daily habit streak is: {highest_daily_habits[0]} with a streak of {highest_daily_habits[2]}")
                print(f"Your highest weekly habit streak is: {highest_weekly_habits[0]} with a streak of {highest_weekly_habits[2]}")

                print ("     Going back to insights...")
                time.sleep(2)
                insights()
                break
            if insights_choice == 3:
                print ("\n")
                print ("AVERAGE STREAKS")
                average_streaks = a.get_average_streaks()
                average_streaks = sorted(average_streaks, key=lambda x: x[1])   #sorts the list from lowest to highest
                for streak in average_streaks:
                    print (streak[0] + " " + str(streak[1]))
                print ("     Going back to insights...")
                time.sleep(2)
                insights()
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
    print ("\n SCHEDULE")
    weekly_habits = a.get_weekly_habits()
    print ("Weekly Habits:")
    for habit in weekly_habits:                    
        #initializing a dictionary to convert the weekday number to the weekday name
        weekday_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}    
        #retrieving date from the database and converting it to a date object
        retrieved_date_str = habit[2] 
        date_obj = dt.datetime.strptime(retrieved_date_str, "%Y-%m-%d").date()
        #converting the date to a weekday name
        weekday_num = dt.date.weekday (date_obj)
        weekday_name = weekday_dict[weekday_num]
        #printing the habits in a more readable way
        if date_obj <= today:
            print(habit[0] + " " + str(habit[1]) + " time(s) per week starting every " + weekday_name)
        elif date_obj > today:
            print(habit[0] + " " + str(habit[1]) + " time(s) per week starting from the " + date_obj.strftime("%d.%m.%Y"))
    print ("\n")
    daily_habits = a.get_daily_habits()
    print ("Daily Habits:")
    for habit in daily_habits:
        retrieved_date_str = habit[2]
        date_obj = dt.datetime.strptime(retrieved_date_str, "%Y-%m-%d").date()
        # checking whether habit is in future or already started
        if date_obj == today:
            print (habit[0] + " " + str(habit[1]) + " time(s) every day")
        elif date_obj > today:
            print (habit[0] + " " + str(habit[1]) + " time(s) per day starting from the " + date_obj.strftime("%d.%m.%Y")) 
    print (" Going back to menu...")
    time.sleep(2)
    menu()

# 3. View Description
def description():
    ''' Function to display the description of the Habit Tracker.'''
    print ("\n")
    print ("DESCRIPTION")
    habit_description = a.get_habit_description()
    for habit in habit_description:
        print (habit[0] + ": " + habit[1])
    print (" Going back to menu...")
    time.sleep(2)
    menu()

# 4. Delete Habit

def delete_habit ():
    hb.load_all_habits()
    print (" \n Which habit do you want to delete?")
    habit_names = a.get_all_habit_names()
    for i, name in enumerate(habit_names):
        print (f"{i+1}. {name[0]}")
    print (" \n Press shown key to delete habit") 
    print ("Press 9 to go back to menu")
    number_of_habits = a.get_number_of_rows()
    #input handling of delete habit
    while True:
        try:
            delete_choice = int (input ("Enter: "))
            if number_of_habits < delete_choice < 9:
                print ("You have only got " + str(number_of_habits) + " habits. Try again")
                continue
            if delete_choice == 1:
                print ("You have selected " + hb.habit1.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit1.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 2:
                print ("You have selected " + hb.habit2.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit2.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 3:
                print ("You have selected " + hb.habit3.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit3.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 4:
                print ("You have selected " + hb.habit4.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit4.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 5:
                print ("You have selected " + hb.habit5.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit5.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 6:
                print ("You have selected " + hb.habit6.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit6.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 7:
                print ("You have selected " + hb.habit7.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit7.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 8:
                print ("You have selected " + hb.habit8.habit_name + ". \n Please note: All history of this habit will be deleted too.")
                confirmation = confirm_deleted_habit_selection()
                if confirmation == True:
                    db.remove_deleted_habit(hb.habit8.habit_name)
                    print ("Habit deleted.")
                    time.sleep(2)
                    menu()
                    break
                elif confirmation == False:
                    print ("Habit not deleted. Going back...")
                    time.sleep(2)
                    delete_habit()
                    break
            if delete_choice == 9:
                menu()
                break
                      
        except ValueError:
            print ("Please enter a number (not a name)")
            continue
def confirm_deleted_habit_selection():
    print ("Do you really want to delete this habit?")
    print ("Press 1 to confirm")
    print ("Press 2 to cancel")
    confirmation = input("Enter your choice: ")
    while confirmation not in ["1", "2"]:
        print ("Please enter a valid choice")
        confirmation = input("Enter your choice: ")
        
    if confirmation == "1":
        return True
    elif confirmation == "2":
        return False

# 5. Add Habit
def add_habit():
    ''' Function to add a habit to the Habit Tracker.'''
    # get all existing habit_names so that the user can't add a habit with the same name and number of habits
    habit_names = [name[0] for name in a.get_all_habit_names()]
    number_of_habits = a.get_number_of_rows()
    print ("\n")
    print ("ADD HABIT")
    print ("You can alwyas go back by typing 'cancel'. PLease note that the habit will not be saved then.") 
    
    if number_of_habits == 8:
        print ("Maximum number of habits reached. Please delete a habit first.")
        print ("Going back to menu...")
        time.sleep(2)
        menu()
    
    while True:
        habit_name = control_input_for_cancel("What's the name of the habit you want to create?")
        if habit_name in habit_names:
            print ("Habit name already exists. Please choose another name.")
            continue 
        break 
    habit_description = control_input_for_cancel("Please add a description to your habit.")
    print ("Would you like to track this habit daily or weekly?")
    while True:
        periodcitiy = control_input_for_cancel("Enter 'daily' or 'weekly': ").strip().lower()
        if periodcitiy == "daily":
            while True:
                try:
                    frequency = int(control_input_for_cancel("How often do you want to do this habit per day?").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            periodcitiy = "day"
            break 
        elif periodcitiy == "weekly":
            while True:
                try:
                    frequency = int(control_input_for_cancel("How often do you want to do this habit per week?").strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            periodcitiy = "week"
            break
        else:
            print("Invalid input. Please enter 'daily' or 'weekly'.")
    print ("When would you like your habit to start?")
    while True:
        start_date_choice =  control_input_for_cancel ("Press 1 for Today or Press 2 for a specific date.")
        if start_date_choice == "1":
            last_timestamp = hb.today
            print ("Habit starts today.")
            break
        elif start_date_choice == "2":
            while True:
                last_timestamp = control_input_for_cancel ("On which day you want the habit to start? PLease enter in the format 'DD.MM.YYYY': ")
                last_timestamp = hb.dt.datetime.strptime(last_timestamp, "%d.%m.%Y").date()
                if last_timestamp < hb.today:
                    print ("Invalid input. Please enter a date in the future.")
                    continue
                print ("Habit starts on " + last_timestamp.strftime("%d.%m.%Y"))
                break
            break
        else:
            print ("Invalid input. Please try again.")
            continue
    db.insert_created_habit(habit_name, habit_description, periodcitiy, frequency, last_timestamp)
    print ("Habit added.")
    print ("Going back to menu...")
    time.sleep(2)
    menu()
    
def control_input_for_cancel(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input == "cancel":
            print("Going back to menu...")
            time.sleep(2)
            menu()
            return None
        elif user_input:
            return user_input




############# Beginning of program #############
print ("\n")
print ("Hi! Welcome to the Habit Tracker")
print (" Got any tasks done?")
db.initalize_database()
db.insert_testdata()
start_page()



