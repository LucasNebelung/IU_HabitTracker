# database.py documentation 

# Habit Tracker Database Module Documentation

## Overview

The Database Module is responsible for managing the storage and retrieval of habit data for the Habit Tracker application. It includes functions to initialize the database, insert test data, modify existing records, and perform various analyses on the stored habits.

## Database Initialization and Test Data Insertion

1. **`initialize_database`**:
    - Creates the database file `habit_tracker.db` if it doesn't already exist.
    - Defines two tables: `habits` (for current habit data) and `habit_history` (for historical streak data).

2. **`insert_testdata`**:
    - Adds sample habits and historical data into the database to facilitate testing and demonstration of the application's features.

## Data Modification Functions

1. **`update_habit`**:
    - Updates dynamic properties of a habit, such as its current frequency, current streak, and the last time it was updated.

2. **`remove_deleted_habit`**:
    - Deletes a specified habit and its associated history from the database.

3. **`insert_created_habit`**:
    - Adds a newly created habit with the provided details into the database.

4. **`insert_habit_history`**:
    - Logs a new entry in the habit history, recording the streak count and timestamp for a habit. Used in the break_habit method to later be able to analyse habit_history to get average and highest streaks

## Data Retrieval and Analysis Functions

1. **`get_current_streaks`**:
    - Retrieves the current streak information for all habits.

2. **`get_weekly_habits`**:
    - Retrieves all habits that are performed on a weekly basis.

3. **`get_daily_habits`**:
    - Retrieves all habits that are performed daily.

4. **`get_habit_description`**:
    - Retrieves the names and descriptions of all habits.

5. **`get_number_of_rows`**:
    - Retrieves the total number of habits stored in the database. This is equaivalent to the number of habits

6. **`get_habit_by_row`**:
    - Retrieves a specific habit based on its row number in the database. Used in the load_all_habits function in order to be able to correctly create instances. 

7. **`get_all_habit_names`**:
    - Retrieves the names of all habits, ordered by their entry in the database.

8. **`get_highest_streaks`**:
    - Retrieves the highest streak counts for each habit in the habit_history table.

9. **`get_average_streaks`**:
    - Retrieves the average streak count for each habit in the habit_history table.

