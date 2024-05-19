# Main.py Documentation 

## Overview
This part of the Habit Tracker program provides the user interface and functionality for managing habits. Users can view, check off, add, and delete habits, as well as view insights and schedules related to their habits. The interface is interactive and provides various options for navigating through different features of the habit tracker.

Components:

### Initialization and Start Page
Function: start_page()
The program starts by initializing the database and loading the start page.
-> Displays all active habits.
-> Provides options to check off a habit, reload the page, access the menu, or exit the program.


### Menu
Function: menu()
The menu provides access to various features of the habit tracker.
-> Displays options to view insights, view schedule, view descriptions, add a habit, or delete a habit.

### Insights
Function: insights()
Allows users to view insights related to their habits.
-> Options to view current streaks, highest streaks, and average streaks.
-> Provides details about the streaks and navigates back to the insights menu.

### View Schedule
Function: view_schedule()
Displays the user's habit schedule.
-> Shows weekly and daily habits.
-> Automatically returns to the menu after displaying the schedule.

### View Description
Function: description()
Provides descriptions of all habits.
-> Displays habit descriptions.
-> Automatically returns to the menu after displaying the descriptions.

### Delete Habit
Function: delete_habit()
Allows users to delete a habit.
-> Prompts the user to select a habit to delete.
-> Confirms the deletion before proceeding.
-> Updates the database to remove the selected habit.

### Add Habit
Function: add_habit()
Allows users to add a new habit.
-> Prompts the user to enter details for the new habit, including name, description, periodicity (daily/weekly), frequency, and start date.
-> Validates user input and adds the habit to the database.
-> the  helper function: control_input_for_cancel(prompt) allows the user to cancel and return to the menu if desired.