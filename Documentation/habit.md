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

- load_all_habits: Loads all habits from the database, creates instances of the Habit class of each row of the habits table  and checks their status. It:
  1. Retrieves the total number of habits from the database.
  2. Iterates through each habit, creates an instance, checks its timing, and updates its status in the database.

