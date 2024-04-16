##############################
# Backend ###################
##############################

# Importing modules
import datetime as dt
import sqlite3

# defining datetime objects
today = dt.date.today()
one_day = dt.timedelta(days=1)
one_week = dt.timedelta(weeks=1) 

# defining Habit class
class Habit:
    def __init__(self, habit_name, habit_specification, periodicity, current_frequency, frequency, last_timestamp, current_streak, is_in_time = False):
        self.habit_name = habit_name
        self.habit_specification = habit_specification
        self.periodicity = periodicity
        self.current_frequency = current_frequency
        self.frequency = frequency
        self.last_timestamp = dt.datetime.strptime(last_timestamp, "%Y-%m-%d").date()
        self.current_streak = current_streak
        self.is_in_time = is_in_time

    def control_time_habit(self):
        ''' Method to control whether the habit is in time or not.
        Based on Periodicity, it checks whether the last timestamp is in time or not.
        and returns a boolean value (is_in_time).'''
        if self.periodicity == "daily":
            if self.last_timestamp + one_day == today:
                self.is_in_time = True
            else: 
                self.is_in_time = False
        elif self.periodicity == "weekly":
            if self.last_timestamp + one_week >= today:
                self.is_in_time = True
            else:
                self.is_in_time = False 
    
    def check_off_habit(self):
        ''' Method to check off the habit. 
        Important: This method should only be called after the control_time_habit method has returned is_in_time = True.'''
        self.current_frequency += 1
        #controlling whether the habit has reached the frequency and then updating the streak and last timestamp
        if self.current_frequency == self.frequency:
            self.current_streak += 1
            self.current_frequency = 0  
            if self.periodicity == "daily":
                self.last_timestamp += one_day
            elif self.periodicity == "weekly":
                self.last_timestamp += one_week
        print (self.current_frequency)
        print (self.current_streak)
        print (self.last_timestamp) 
    
    def break_habit(self):
        ''' Method to break the habit. 
        Current_Frequency, Current_Streak are reset to zero and last_timestamp is set to today.'''
        self.current_frequency = 0
        self.current_streak = 0
        self.last_timestamp = today

class database_modifier:
    def __init__(self):
        pass

    def initalize_database(self):
        ''' Method to initalize the database. 
        Creates a database file and a table to store the habits.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE habits
                    (habit_name text, habit_specification text, periodicity text, current_frequency integer, frequency integer, last_timestamp text, current_streak integer)''')
        c.execute('''CREATE TABLE habit_history
                    (id integer, timestamp text, streak_count integer, habit_name text)''')
        conn.commit()
        conn.close()

    def update_checked_off_habit(self,




# Testing the class
Testhabit = Habit("Testhabit", "Testdescription", "daily", 0, 1, "2024-04-15" , 0)
Testhabit2 = Habit("Testhabit2", "Testdescription2", "weekly", 0, 1, "2024-04-15" , 0) 

Testhabit.break_habit()



