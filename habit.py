##############################
# Backend ###################
##############################

# Importing modules
import datetime as dt
import sqlite3
from database import database_controller 

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
        self.last_timestamp = last_timestamp
        self.current_streak = current_streak
        self.is_in_time = is_in_time

    def __str__(self):
        return f'Habit({self.habit_name}, {self.habit_specification}, {self.periodicity}, {self.current_frequency}, {self.frequency}, {self.last_timestamp}, {self.current_streak}, {self.is_in_time})'

    def control_time_habit(self):
        ''' Method to control whether the habit is in time or not.
        Based on Periodicity, it checks whether the last timestamp is in time or not.
        and returns a boolean value (is_in_time).'''
        self.last_timestamp = dt.datetime.strptime(self.last_timestamp, "%Y-%m-%d").date()
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
        #controlling whether the habit has reached the max frequency and then updating the streak and last timestamp
        if self.current_frequency == self.frequency:
            self.current_streak += 1
            self.current_frequency = 0  
            if self.periodicity == "daily":
                self.last_timestamp += one_day
            elif self.periodicity == "weekly":
                self.last_timestamp += one_week
        
         
    
    def break_habit(self):
        ''' Method to break the habit. 
        Current_Frequency, Current_Streak are reset to zero and last_timestamp is set to today.'''
        self.current_frequency = 0
        self.current_streak = 0
        self.last_timestamp = today
        #hier noch Methode hinzufügen, dass Daten auch in die habit_history Tabelle geschrieben werden

    def load_all_habits(self):
        ''' Method to load all habits from the database.
        1. get number of rows 
        2. get habit by row
        3. create Habit object and append to list'''



db = database_controller()

#habit_number
#i = 0
#habit_number[i] = Habit(db.get_habit_by_row(i)[0], db.get_habit_by_row(i)[1], db.get_habit_by_row(i)[2], db.get_habit_by_row(i)[3], db.get_habit_by_row(i)[4], db.get_habit_by_row(i)[5], db.get_habit_by_row(i)[6])
#print (habit1.habit_name)

#habit0 = Habit(db.get_habit_by_row(0)[0], db.get_habit_by_row(0)[1], db.get_habit_by_row(0)[2], db.get_habit_by_row(0)[3], db.get_habit_by_row(0)[4], db.get_habit_by_row(0)[5], db.get_habit_by_row(0)[6])
 
#print (habit0.habit_name)

my_list = []

for i in range(5):
    my_list.append(habit + i)

print(my_list)