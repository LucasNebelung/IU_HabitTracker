# database.py documentation 

# Habit Tracker Database Module Documentation

## Overview

The Database Module is responsible for managing the storage of habit data for the Habit Tracker application. It includes functions to initialize the database, insert test data, and modify existing records like updating, removing and inserting info.

## Database Initialization and Test Data Insertion

1. **`initialize_database`**:
    - Creates the database file `habit_tracker.db` if it doesn't already exist.
    - Defines two tables: `habits` (for current habit data) and `habit_history` (for historical streak data).

2. **`insert_testdata`**:
    - Adds sample habits and historical data into the database to facilitate testing and demonstration of the application's features.

## Database Functions

1. **`update_habit`**:
    - Updates dynamic properties of a habit, such as its current frequency, current streak, and the last time it was updated.

2. **`remove_deleted_habit`**:
    - Deletes a specified habit and its associated history from the database.

3. **`insert_created_habit`**:
    - Adds a newly created habit with the provided details into the database.

4. **`insert_habit_history`**:
    - Logs a new entry in the habit history, recording the streak count and timestamp for a habit. Used in the break_habit method to later be able to analyse habit_history to get average and highest streaks

