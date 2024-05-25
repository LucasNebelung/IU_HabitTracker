# analytics.py Documentation

## Overview

The Analytics Module is responsible for retrieving and analyzing habit data for the Habit Tracker application. It includes functions to fetch various details about the habits stored in the database, such as current streaks, highest streaks, average streaks, and descriptions. This module leverages SQLite's aggregate functions to perform necessary analyses and provide insights into the user's habit patterns.


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
    - Retrieves the names of all habits, ordered by their entry in the database. IMportant in the delete habit function

8. **`get_highest_streaks`**:
    - Retrieves the highest streak counts for each habit from the habit_history table. 

9. **`get_average_streaks`**:
    - Retrieves the average streak count for each habit in the habit_history table.

10. **`get_all_habit_info`**:
    - Retrieves relevant information in order to display them on the start page  

