#############################
##### analytics module ######
#############################

# Importing modules
import sqlite3 


# Functions for retrieving habit data and performing necessary analysis using SQLite's aggregate functions

def get_current_streaks ():
    ''' Method to get the current streaks of all habits.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT  habit_name, current_streak FROM habits''')
    current_streaks = c.fetchall()
    conn.close()
    return current_streaks

def get_weekly_habits():
    ''' Method to get all habits that are week.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, frequency, last_timestamp FROM habits WHERE periodicity = "week"''')
    week_habits = c.fetchall()
    conn.close()
    return week_habits

def get_daily_habits():
    ''' Method to get all habits that are day.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, frequency, last_timestamp FROM habits WHERE periodicity = "day"''')
    day_habits = c.fetchall()
    conn.close()
    return day_habits

def get_habit_description(): 
    ''' Method to get the description of all habits.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, habit_specification FROM habits''')
    habit_description = c.fetchall()
    conn.close()
    return habit_description

def get_number_of_rows():
    ''' Method to get the number of rows in the habits table which is equivalent to the number of habits.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM habits''')
    rows = c.fetchall()
    conn.close()
    return len(rows)

def get_habit_by_row (row):
    ''' Method to get a habit by the row number.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM habits''')
    specific_habit = c.fetchall()[row]
    conn.close()
    return specific_habit

def get_all_habit_names():
    ''' Method to get all habit names. 
    Used in delete habit function and to check whether a habit already exists.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name FROM habits ORDER BY ROWID''')
    habit_names = c.fetchall()
    conn.close()
    return habit_names

def get_highest_streaks():
    ''' Method to get the highest streak of all habits.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, MAX(streak_count) FROM habit_history GROUP BY habit_name''')
    highest_streaks = c.fetchall()
    conn.close()
    return highest_streaks

def get_highest_streaks_by_periodicity():
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habits.habit_name, habits.periodicity, MAX(habit_history.streak_count) 
    FROM habit_history 
    JOIN habits ON habit_history.habit_name = habits.habit_name 
    GROUP BY habits.habit_name, habits.periodicity''') 
    highest_streaks_by_periodicity = c.fetchall()
    conn.close()
    return highest_streaks_by_periodicity


def get_average_streaks():
    ''' Method to get the average streak of all habits.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, ROUND(AVG(streak_count), 1) FROM habit_history GROUP BY habit_name''')
    average_streaks = c.fetchall()
    conn.close()
    return average_streaks

def get_all_habit_info():
    ''' Method to get all habit information for start page.'''
    conn = sqlite3.connect('habit_tracker.db')
    c = conn.cursor()
    c.execute('''SELECT habit_name, current_frequency, frequency, periodicity FROM habits''')
    habit_info = c.fetchall()
    conn.close()
    return habit_info

