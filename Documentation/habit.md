# habit.py Documentation 

## Overview

The Habit Tracker program is designed to help users manage and track their habits. It offers functionality to check off progress, control habit timings, and maintain streaks, ensuring users stay on track with their goals. This documentation covers the `Habit` class and several supporting functions that facilitate interaction with the habit database and user interface.

### Habit Class

The `Habit` class encapsulates the attributes and behaviors associated with a habit. It allows for creating and managing habits, checking progress, and updating streaks.

#### Attributes

- habit_name: A string representing the name of the habit.
- habit_specification: A detailed description or specification of the habit.
- periodicity: The frequency with which the habit should be completed (e.g., daily, weekly).
- current_frequency: An integer representing the current count of habit completions within the specified period.
- frequency: The required number of completions within the specified period.
- last_timestamp: A date object representing the last date the habit was checked off.
- current_streak: An integer representing the current streak of consecutive completions.

#### Methods

1. control_time_habit: Manages the timing and streaks of the habit. It:
   - Converts the last timestamp to a date object.
   - Checks if the habit is daily or weekly.
   - Updates the last timestamp, current frequency, and streak based on whether the habit is completed on time.
   - Resets the habit if it is not completed on time and updates the streak and frequency accordingly.

2. check_off_habit: Marks the habit as completed for the day or week. It:
   - Converts the last timestamp to a date object.
   - Checks if the habit can be marked as completed based on the current frequency and date.
   - Increments the current frequency if the habit can be checked off.
   - Provides feedback if the habit cannot be checked off.

3. break_habit: Resets the habit streak and frequency to zero if the habit is not maintained. It:
   - Logs the habit in the habit_history table of database in order to be able to later analyse average and highest streak 
   - Resets the current frequency and streak.
   - Sets the last timestamp to the current date.
   - Provides feedback to the user about the broken streak.

### Supporting Functions

These functions support the main functionalities of the Habit Tracker by interacting with the database and providing a user-friendly interface.

#### Database Interaction

- load_all_habits: Loads all habits from the database, creates instances of the Habit class of each row of the habits table  and checks their status. It:
  - Retrieves the total number of habits from the database.
  - Iterates through each habit, creates an instance, checks its timing, and updates its status in the database.

- print_current_streaks: Retrieves and prints the current streaks of all habits from the database. It provides an overview of ongoing progress.

- print_highest_streaks: Retrieves and prints the highest streaks, sorted from highest to lowest. It helps identify the most successfully maintained habits.

- print_average_streaks: Retrieves and prints the average streaks, sorted from lowest to highest. It provides insights into overall habit maintenance.

- print_weekly_habits: Retrieves and prints all weekly habits in a readable format. It:
  - Converts the start dates to weekday names.
  - Differentiates between habits that have already started and those scheduled for the future.

- print_daily_habits: Retrieves and prints all daily habits, showing whether they are ongoing or scheduled to start in the future. It helps users keep track of their daily goals.

- print_habit_description: Retrieves and prints the descriptions of all habits. It provides detailed information about each habit.

- print_all_habit_names: Retrieves and prints the names of all habits, primarily used for selecting habits to delete.

