#########################
#### DATABASE MODULE ####
#########################

#importing relevant modules
import sqlite3

############# Functions TO INITALIZE AND INSERT TEST DATA ################

def initalize_database():
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

def insert_testdata():
    ''' Method to insert test data into the database.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    #for habit table 
    c.execute('''INSERT INTO habits VALUES ("Brush teeth", "Brush your teeth in the morning and evening", "day", 0, 2, "2024-05-05", 0)''')
    c.execute('''INSERT INTO habits VALUES ("Vacuum room", "Vacuum your room twice a week, dont forget Bathroom", "week", 0, 2, "2024-05-05", 0)''')
    c.execute('''INSERT INTO habits VALUES ("Workout", "Workout five times a week, dont forget running", "week", 0, 5, "2024-05-05", 0)''')
    c.execute('''INSERT INTO habits VALUES ("Learn Spanish", "Learn Spanish once a day alternate between vocab and grammar", "day", 0, 1, "2024-05-05", 0)''')
    c.execute('''INSERT INTO habits VALUES ("Call Family", "Call your family once a week", "week", 0, 1, "2024-05-05", 0)''')
    #for habit_history table
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-04", 2, "Brush teeth")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-09", 1, "Brush teeth")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-13", 3, "Brush teeth")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-14", 2, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-15", 0, "Learn Spanish")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-15", 0, "Workout")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-15", 0, "Call Family")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-15", 0, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-16", 1, "Learn Spanish")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-16", 1, "Workout")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-16", 3, "Call Family")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-16", 1, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-17", 1, "Learn Spanish")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-17", 2, "Workout")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-17", 0, "Call Family")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-17", 1, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-18", 0, "Learn Spanish")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-18", 3, "Workout")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-18", 2, "Call Family")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-18", 5, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-19", 1, "Learn Spanish")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-19", 1, "Workout")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-19", 4, "Call Family")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-19", 6, "Vacuum room")''')
    c.execute('''INSERT INTO habit_history VALUES (NULL, "2024-04-20", 2, "Learn Spanish")''')

    conn.commit()
    conn.close()


############# METHODS TO MODIFY DATABASE ################

def update_habit(habit_name, current_frequency, current_streak, last_timestamp):
    ''' Method to easily update the current_frequency, current_streak and last_timestamp of a habit.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''UPDATE habits SET current_frequency = ?, current_streak = ?, last_timestamp = ? WHERE habit_name = ?''', (current_frequency, current_streak, last_timestamp, habit_name))
    conn.commit()
    conn.close()

def remove_deleted_habit (habit_name):
    ''' Method to remove a habit from the database.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''DELETE FROM habits WHERE habit_name = ?''', (habit_name,))
    c.execute('''DELETE FROM habit_history WHERE habit_name = ?''', (habit_name,))
    conn.commit()
    conn.close()

def insert_created_habit(habit_name, habit_specification, periodicity, frequency, last_timestamp):
    ''' Method to insert a created habit into the database.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''INSERT INTO habits VALUES (?, ?, ?, 0, ?, ?, 0)''', (habit_name, habit_specification, periodicity, frequency, last_timestamp))
    conn.commit()
    conn.close()

def insert_habit_history(habit_name, streak_count, historic_timestamp):
    ''' Method to insert a habit history into the database.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''INSERT INTO habit_history VALUES (NULL, ?, ?, ?)''', (historic_timestamp, streak_count, habit_name))
    conn.commit()
    conn.close()






