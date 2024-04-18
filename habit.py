##############################
# Backend ###################
##############################

# Importing modules
import datetime as dt
import sqlite3
from database import database_controller as db

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
        ''' Method to create a habit instance from each entry in the database.'''
        

        

        
#################### Testing

all_habits = [('Brush teeth', 'Brush your teeth in the morning and evening', 'daily', 0, 2, '2024-04-17', 0), 
              ('Vacuum room', 'Vacuum your room twice a week, dont forget Bathroom', 'weekly', 0, 2, '2024-04-15', 0), 
              ('Workout', 'Workout five times a week, dont forget running', 'weekly', 0, 5, '2024-04-15', 0), 
              ('Learn Spanish', 'Learn Spanish once a day alternate between vocab and grammar', 'daily', 0, 1, '2024-04-17', 0), 
              ('Call Family', 'Call your family once a week', 'weekly', 0, 1, '2024-04-15', 0)]

# creating instances of the Habit class
for i, habit_data in enumerate(all_habits, start=1):
    habit_name, habit_specification, periodicity, current_frequency, frequency, last_timestamp, current_streak = habit_data
    vars()[f"habit{i}"] = Habit(habit_name, habit_specification, periodicity, current_frequency, frequency, last_timestamp, current_streak)

print (habit1)
################################### Hier weitermachen!!!!!!!