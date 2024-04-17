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

    def __str__(self):
        return f'Habit({self.habit_name}, {self.habit_specification}, {self.periodicity}, {self.current_frequency}, {self.frequency}, {self.last_timestamp}, {self.current_streak}, {self.is_in_time})'

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

class database_modifier:
    def __init__(self):
        pass

    def initalize_database(self):
        ''' Method to initalize the database. 
        Creates a database file and a table to store the habits.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS habits
                    (
                  habit_name TEXT PRIMARY KEY NOT NULL, 
                  habit_specification text, 
                  periodicity text, 
                  current_frequency integer, 
                  frequency integer, 
                  last_timestamp text, 
                  current_streak integer)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS habit_history
                    (
                  id integer PRIMARY KEY AUTOINCREMENT, 
                  historic_timestamp text, 
                  streak_count integer, 
                  habit_name text, 
                  FOREIGN KEY(habit_name) REFERENCES habits(habit_name))''')
        conn.commit()
        conn.close()

    def insert_testdata(self):
        ''' Method to insert test data into the database.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''INSERT INTO habits VALUES ("Testhabit", "Testdescription", "daily", 0, 1, "2024-04-17", 0)''')
        c.execute('''INSERT INTO habits VALUES ("Testhabit2", "Testdescription2", "weekly", 0, 1, "2024-04-15", 0)''')
        conn.commit()
        conn.close()

    def load_habit(self, habit_name):
        ''' Method to load a habit and create an Instance of the Habit class using habit_name.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits WHERE habit_name = ?''', (habit_name,))
        habit_data = c.fetchone()
        # creating an instance out of habit_data
        habit_name = Habit(*habit_data)
        conn.close()
        return habit_name
    
    def update_habit(self,habit_name, current_frequency, current_streak, last_timestamp):
        ''' Method to easily update the current_frequency, current_streak and last_timestamp of a habit.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''UPDATE habits SET current_frequency = ?, current_streak = ?, last_timestamp = ? WHERE habit_name = ?''', (current_frequency, current_streak, last_timestamp, habit_name))
        conn.commit()
        conn.close()

        

        
    


# Testing the class
#Testhabit = Habit("Testhabit", "Testdescription", "daily", 0, 1, "2024-04-15" , 0)
#Testhabit2 = Habit("Testhabit2", "Testdescription2", "weekly", 0, 1, "2024-04-15" , 0) 


db = database_modifier()


Testhabit = db.load_habit ("Testhabit")
#print (Testhabit)
#Testhabit.control_time_habit()
#print (Testhabit)
#Testhabit.check_off_habit()
#print (Testhabit)


db.update_habit("Testhabit", Testhabit.current_frequency, Testhabit.current_streak, Testhabit.last_timestamp)
print (Testhabit)


