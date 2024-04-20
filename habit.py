##############################
# Backend ###################
##############################

# Importing modules
import datetime as dt
import sqlite3
from database import database_controller
db = database_controller () 

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
    global habit1, habit2, habit3, habit4, habit5, habit6, habit7, habit8, habit9, habit10
    max_rows = db.get_number_of_rows()
    rows = 0
    while rows < max_rows:
        habit1 = Habit (db.get_habit_by_row (0)[0], db.get_habit_by_row (0)[1], db.get_habit_by_row (0)[2], db.get_habit_by_row (0)[3], db.get_habit_by_row (0)[4], db.get_habit_by_row (0)[5], db.get_habit_by_row (0)[6])
        rows += 1
        if rows == max_rows:
            return habit1
        habit2 = Habit (db.get_habit_by_row(1)[0], db.get_habit_by_row(1)[1], db.get_habit_by_row(1)[2], db.get_habit_by_row(1)[3], db.get_habit_by_row(1)[4], db.get_habit_by_row(1)[5], db.get_habit_by_row(1)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2
        habit3 = Habit (db.get_habit_by_row(2)[0], db.get_habit_by_row(2)[1], db.get_habit_by_row(2)[2], db.get_habit_by_row(2)[3], db.get_habit_by_row(2)[4], db.get_habit_by_row(2)[5], db.get_habit_by_row(2)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3
        habit4 = Habit (db.get_habit_by_row(3)[0], db.get_habit_by_row(3)[1], db.get_habit_by_row(3)[2], db.get_habit_by_row(3)[3], db.get_habit_by_row(3)[4], db.get_habit_by_row(3)[5], db.get_habit_by_row(3)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4
        habit5 = Habit (db.get_habit_by_row(4)[0], db.get_habit_by_row(4)[1], db.get_habit_by_row(4)[2], db.get_habit_by_row(4)[3], db.get_habit_by_row(4)[4], db.get_habit_by_row(4)[5], db.get_habit_by_row(4)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5
        habit6 = Habit (db.get_habit_by_row(5)[0], db.get_habit_by_row(5)[1], db.get_habit_by_row(5)[2], db.get_habit_by_row(5)[3], db.get_habit_by_row(5)[4], db.get_habit_by_row(5)[5], db.get_habit_by_row(5)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6
        habit7 = Habit (db.get_habit_by_row(6)[0], db.get_habit_by_row(6)[1], db.get_habit_by_row(6)[2], db.get_habit_by_row(6)[3], db.get_habit_by_row(6)[4], db.get_habit_by_row(6)[5], db.get_habit_by_row(6)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7
        habit8 = Habit (db.get_habit_by_row(7)[0], db.get_habit_by_row(7)[1], db.get_habit_by_row(7)[2], db.get_habit_by_row(7)[3], db.get_habit_by_row(7)[4], db.get_habit_by_row(7)[5], db.get_habit_by_row(7)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7, habit8
        habit9 = Habit (db.get_habit_by_row(8)[0], db.get_habit_by_row(8)[1], db.get_habit_by_row(8)[2], db.get_habit_by_row(8)[3], db.get_habit_by_row(8)[4], db.get_habit_by_row(8)[5], db.get_habit_by_row(8)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7, habit8, habit9
        habit10 = Habit (db.get_habit_by_row(9)[0], db.get_habit_by_row(9)[1], db.get_habit_by_row(9)[2], db.get_habit_by_row(9)[3], db.get_habit_by_row(9)[4], db.get_habit_by_row(9)[5], db.get_habit_by_row(9)[6])
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7, habit8, habit9, habit10
        
        
    #################Hier weitermachen

load_all_habits(db)

print (habit5.current_frequency)