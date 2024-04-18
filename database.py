#########################
# This file contains the database_modifier class which is used to interact with the database.
#########################

#importing relevant modules
import sqlite3
import datetime as dt



class database_controller:
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
        c.execute('''INSERT INTO habits VALUES ("Brush teeth", "Brush your teeth in the morning and evening", "daily", 0, 2, "2024-04-17", 0)''')
        c.execute('''INSERT INTO habits VALUES ("Vacuum room", "Vacuum your room twice a week, dont forget Bathroom", "weekly", 0, 2, "2024-04-15", 0)''')
        c.execute('''INSERT INTO habits VALUES ("Workout", "Workout five times a week, dont forget running", "weekly", 0, 5, "2024-04-15", 0)''')
        c.execute('''INSERT INTO habits VALUES ("Learn Spanish", "Learn Spanish once a day alternate between vocab and grammar", "daily", 0, 1, "2024-04-17", 0)''')
        c.execute('''INSERT INTO habits VALUES ("Call Family", "Call your family once a week", "weekly", 0, 1, "2024-04-15", 0)''')
        conn.commit()
        conn.close()

    def get_specific_habit(self, habit_name):
        ''' Method to load a habit and create an Instance of the Habit class using habit_name.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits WHERE habit_name = ?''', (habit_name,))
        habit_data = c.fetchone()
        # creating an instance out of habit_data
        conn.close()
        return habit_data
    
    def update_habit(self,habit_name, current_frequency, current_streak, last_timestamp):
        ''' Method to easily update the current_frequency, current_streak and last_timestamp of a habit.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''UPDATE habits SET current_frequency = ?, current_streak = ?, last_timestamp = ? WHERE habit_name = ?''', (current_frequency, current_streak, last_timestamp, habit_name))
        conn.commit()
        conn.close()
    
    def remove_deleted_habit (self, habit_name):
        ''' Method to remove a habit from the database.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''DELETE FROM habits WHERE habit_name = ?''', (habit_name,))
        conn.commit()
        conn.close()
    
    def insert_created_habit(self, habit_name, habit_specification, periodicity, frequency, last_timestamp):
        ''' Method to insert a created habit into the database.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''INSERT INTO habits VALUES (?, ?, ?, 0, ?, ?, 0)''', (habit_name, habit_specification, periodicity, frequency, last_timestamp))
        conn.commit()
        conn.close()

    def get_weekly_habits(self):
        ''' Method to get all habits that are weekly.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits WHERE periodicity = "weekly"''')
        weekly_habits = c.fetchall()
        conn.close()
        return weekly_habits
    
    def get_daily_habits(self):
        ''' Method to get all habits that are daily.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits WHERE periodicity = "daily"''')
        daily_habits = c.fetchall()
        conn.close()
        return daily_habits
    
    def count_rows(self):
        ''' Method to count the rows in the habits table.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT COUNT(*) FROM habits''')
        count = c.fetchone()
        conn.close()
        return count
    
    def get_all_habits(self):
        ''' Method to get all habits.'''
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits''')
        all_habits = c.fetchall()
        conn.close()
        return all_habits


db = database_controller()

all_habits = db.get_all_habits()
print (all_habits)


