#################################
######## UNIT TEST OF the Habit class in habit.py ####
#################################


#required libraries
import unittest
import datetime as dt 
import sqlite3
import os

# classes and modules to be tested
import habit as hb  
import database as db
import analytics as a

# defining datetime objects 
today = dt.date.today()    # dt.date(YYYY,MM,DD) is a convenient way to simulate different dates and test if everything works accordingly
yesterday = today - dt.timedelta(days=1)
one_week_ago = today - dt.timedelta(weeks=1)
more_than_one_week_ago = today - dt.timedelta(weeks=2)
future_date = today + dt.timedelta(weeks=4)
one_day = dt.timedelta(days=1)
one_week = dt.timedelta(weeks=1) 


######## defining the test class ########

class TestHabit(unittest.TestCase):
    def setUp(self):
        # Creating instances of habits to test to simulate different scenarios and test whether the functions work as expected
        self.habit1 = hb.Habit("daily_habit_in_time", "Description 1", "day", 0, 1, today.strftime("%Y-%m-%d") , 0)
        self.habit2 = hb.Habit("daily_habit_not_in_time", "Description 2", "day", 2, 3, yesterday.strftime("%Y-%m-%d"), 1)
        self.habit3 = hb.Habit ("weekly_habit_in_time", "Description 3", "week", 4, 5, one_week_ago.strftime("%Y-%m-%d"), 2)
        self.habit4 = hb.Habit ("weekly_habit_not_in_time", "Description 4", "week", 6, 7, more_than_one_week_ago.strftime("%Y-%m-%d"), 3)
        self.habit5 = hb.Habit ("future_habit", "Description 5", "weeek", 0, 3, future_date.strftime("%Y-%m-%d"), 4)
        self.habit6 = hb.Habit ("already_finished_habit", "Description 6", "day", 1 , 1, today.strftime("%Y-%m-%d"), 5)

############### Database Module Tests ####################        
    def test_database(self):
        #Testing if the database file exists
        self.assertTrue(os.path.exists('habit_tracker.db'), "The database file 'habit_tracker.db' does not exist.")
        #Testing if the table habits exists
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='habits' ''')
        self.assertEqual(c.fetchone()[0], 1, "The table 'habits' does not exist.")
        #Testing if the table habit_history exists
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='habit_history' ''')
        self.assertEqual(c.fetchone()[0], 1, "The table 'habit_history' does not exist.")
        conn.close()
        print ("Test database initialization passed") 

    def test_database_functions(self):
        #testing all of the functions bundled into one test
        #1) starting with db.insert_created_habit
        db.insert_created_habit ("daily_habit_in_time", "Description 1", "day", 1, today.strftime("%Y-%m-%d"))
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits WHERE habit_name = "daily_habit_in_time"''')
        habit = c.fetchone()
        self.assertEqual(habit[0], "daily_habit_in_time")
        self.assertEqual(habit[1], "Description 1")
        self.assertEqual(habit[2], "day")
        self.assertEqual(habit[3], 0)
        self.assertEqual(habit[4], 1)
        self.assertEqual(habit[5], today.strftime("%Y-%m-%d"))
        self.assertEqual(habit[6], 0)
        print ("Test insert_created_habit passed")
        # 2) testing db.update_habit
        db.update_habit("daily_habit_in_time", 1, 0, today.strftime("%Y-%m-%d"))
        c.execute('''SELECT * FROM habits WHERE habit_name = "daily_habit_in_time"''')
        habit = c.fetchone()
        self.assertEqual(habit[0], "daily_habit_in_time")
        self.assertEqual(habit[1], "Description 1")
        self.assertEqual(habit[2], "day")
        self.assertEqual(habit[3], 1)
        self.assertEqual(habit[4], 1)
        self.assertEqual(habit[5], today.strftime("%Y-%m-%d"))
        self.assertEqual(habit[6], 0)
        print ("Test update_habit passed")
        # 3) testing db.insert_habit_history
        db.insert_habit_history("daily_habit_in_time", 1, today.strftime("%Y-%m-%d"))
        c.execute('''SELECT * FROM habit_history WHERE habit_name = "daily_habit_in_time"''')
        habit = c.fetchone()
        self.assertEqual(habit[1], today.strftime("%Y-%m-%d"))
        self.assertEqual(habit[2], 1)
        self.assertEqual(habit[3], "daily_habit_in_time")
        print ("Test insert_habit_history passed")
        # 4) testing db.remove_deleted_habit
        db.remove_deleted_habit("daily_habit_in_time")
        c.execute('''SELECT * FROM habits WHERE habit_name = "daily_habit_in_time"''')
        habit = c.fetchone()
        self.assertEqual(habit, None)
        c.execute('''SELECT * FROM habit_history WHERE habit_name = "daily_habit_in_time"''')
        habit = c.fetchone()
        self.assertEqual(habit, None)
        print ("Test remove_deleted_habit passed")

        # closing the connection        
        conn.close()


############### Habit Class  Tests ####################
    def test_control_time_habit(self):
        #Testing Habit 1 
        self.habit1.control_time_habit()
        self.assertEqual(self.habit1.last_timestamp, today.strftime("%Y-%m-%d"))
        #Testing Habit 2
        self.habit2.control_time_habit()
        self.assertEqual(self.habit2.last_timestamp, today.strftime("%Y-%m-%d"))
        self.assertEqual(self.habit2.current_frequency, 0)
        #Testing Habit 3
        self.habit3.control_time_habit()
        self.assertEqual(self.habit3.last_timestamp, one_week_ago.strftime("%Y-%m-%d"))
        #Testing Habit 4
        self.habit4.control_time_habit()
        self.assertEqual(self.habit4.last_timestamp, today.strftime("%Y-%m-%d"))
        self.assertEqual(self.habit4.current_frequency, 0)
        print ("Test control_time_habit passed")

    def test_check_off_habit(self):
        #Testing Habit 1
        self.habit1.check_off_habit()
        self.assertEqual(self.habit1.current_frequency, 1)
        #Testing Habit 5
        self.habit5.check_off_habit()
        self.assertEqual(self.habit5.current_frequency, 0)
        #Testing Habit 6
        self.habit6.check_off_habit()
        self.assertEqual(self.habit6.current_frequency, 1)
        print ("Test check_off_habit passed")
    
    def test_break_habit(self):
        #Testing Habit 2
        self.habit2.break_habit()
        self.assertEqual(self.habit2.current_frequency, 0)
        self.assertEqual(self.habit2.last_timestamp, today)
        self.assertEqual(self.habit2.current_streak, 0)        
        print ("Test break_habit passed")

    def test_load_all_habits(self):
       #calling the function load_all_habits to test if it works as expected
        hb.load_all_habits()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits''')
        all_habits = c.fetchall()
        limit = len(all_habits) - 1 # getting the number of habits in the database to automatically stop the loop
        for i in range(limit):
            habit = getattr (hb, f'habit{i+1}')
    
            self.assertEqual(habit.habit_name, all_habits[i][0])
            self.assertEqual(habit.habit_specification, all_habits[i][1])
            self.assertEqual(habit.periodicity, all_habits[i][2])
            self.assertEqual(habit.current_frequency, all_habits[i][3])
            self.assertEqual(habit.frequency, all_habits[i][4])
            self.assertEqual(habit.last_timestamp, all_habits[i][5])
            self.assertEqual(habit.current_streak, all_habits[i][6])
        
        conn.close()
        print ("Test load_all_habits passed")

############## Analytics Module Tests #################
        
    def test_get_current_streaks(self):
        #calling the function get_current_streaks to test if it works as expected
        streaks = a.get_current_streaks()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name, current_streak FROM habits''')
        all_streaks = c.fetchall()
        conn.close()
        for i in range(len(streaks)):
            self.assertEqual(streaks[i][0], all_streaks[i][0])
            self.assertEqual(streaks[i][1], all_streaks[i][1])
        print ("Test get_current_streaks passed")
    
    def test_get_weekly_habits(self):
        #calling the function get_weekly_habits to test if it works as expected
        week_habits = a.get_weekkly_habits()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name FROM habits WHERE periodicity = "week"''')
        all_week_habits = c.fetchall()
        conn.close()
        for i in range(len(week_habits)):
            self.assertEqual(week_habits[i][0], all_week_habits[i][0])
        print ("Test get_weekly_habits passed")
    
    def test_get_daily_habits(self):
        #calling the function get_daily_habits to test if it works as expected
        day_habits = a.get_daily_habits()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name FROM habits WHERE periodicity = "day"''')
        all_day_habits = c.fetchall()
        conn.close()
        for i in range(len(day_habits)):
            self.assertEqual(day_habits[i][0], all_day_habits[i][0])
        print ("Test get_daily_habits passed")
    
    def test_get_habit_description(self):
        #calling the function get_habit_description to test if it works as expected
        habit_description = a.get_habit_description()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name, habit_specification FROM habits''')
        all_habit_description = c.fetchall()
        conn.close()
        for i in range(len(habit_description)):
            self.assertEqual(habit_description[i][0], all_habit_description[i][0])
            self.assertEqual(habit_description[i][1], all_habit_description[i][1])
        print ("Test get_habit_description passed")
    
    def test_get_number_of_rows(self):
        #calling the function get_number_of_rows to test if it works as expected
        rows = a.get_number_of_rows()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits''')
        all_rows = c.fetchall()
        conn.close()
        self.assertEqual(rows, len(all_rows))
        print ("Test get_number_of_rows passed")
    
    def test_get_habit_by_row(self):
        #calling the function get_habit_by_row to test if it works as expected
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM habits''')
        all_habits = c.fetchall()
        conn.close()
        for i in range(len(all_habits)):
            habit = a.get_habit_by_row(i)
            self.assertEqual(habit, all_habits[i])
        print ("Test get_habit_by_row passed")
    
    def test_get_all_habit_names(self):
        #calling the function get_all_habit_names to test if it works as expected
        habit_names = a.get_all_habit_names()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name FROM habits ORDER BY ROWID''')
        all_habit_names = c.fetchall()
        conn.close()
        for i in range(len(habit_names)):
            self.assertEqual(habit_names[i][0], all_habit_names[i][0])
        print ("Test get_all_habit_names passed")
    
    def test_get_highest_streaks(self):
        #calling the function get_highest_streaks to test if it works as expected
        streaks = a.get_highest_streaks()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name, MAX(streak_count) FROM habit_history GROUP BY habit_name''')
        all_streaks = c.fetchall()
        conn.close()
        for i in range(len(streaks)):
            self.assertEqual(streaks[i][0], all_streaks[i][0])
            self.assertEqual(streaks[i][1], all_streaks[i][1])
        print ("Test get_highest_streaks passed")

    def test_get_highest_streaks_by_periodicity(self):
        #calling the function get_highest_streaks_by_periodicity to test if it works as expected
        streaks = a.get_highest_streaks_by_periodicity()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habits.habit_name, habits.periodicity, MAX(habit_history.streak_count) 
        FROM habit_history 
        JOIN habits ON habit_history.habit_name = habits.habit_name 
        GROUP BY habits.habit_name, habits.periodicity''')
        all_streaks = c.fetchall()
        conn.close()
        for i in range(len(streaks)):
            self.assertEqual(streaks[i][0], all_streaks[i][0])
            self.assertEqual(streaks[i][1], all_streaks[i][1])
            self.assertEqual(streaks[i][2], all_streaks[i][2])
        print ("Test get_highest_streaks_by_periodicity passed")
    
    def test_get_average_streaks(self):
        #calling the function get_average_streaks to test if it works as expected
        streaks = a.get_average_streaks()
        #comparing the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name, ROUND(AVG(streak_count), 1) FROM habit_history GROUP BY habit_name''')
        all_streaks = c.fetchall()
        conn.close()
        for i in range(len(streaks)):
            self.assertEqual(streaks[i][0], all_streaks[i][0])
            self.assertEqual(streaks[i][1], all_streaks[i][1])
        print ("Test get_average_streaks passed")
    
    def test_get_all_habit_info(self):
        # Call the function get_all_habit_info to test if it works as expected
        habit_info = a.get_all_habit_info()
        # Compare the assigned values of the habit instances with the values in the database
        conn = sqlite3.connect('habit_tracker.db')
        c = conn.cursor()
        c.execute('''SELECT habit_name, current_frequency, frequency, periodicity FROM habits''')
        all_habit_info = c.fetchall()
        conn.close()
        for i in range(len(habit_info)):
            self.assertEqual(habit_info[i][0], all_habit_info[i][0])
            self.assertEqual(habit_info[i][1], all_habit_info[i][1])
            self.assertEqual(habit_info[i][2], all_habit_info[i][2])
            self.assertEqual(habit_info[i][3], all_habit_info[i][3])
        print ("Test get_all_habit_info passed")
            
###########  Tear down necessary to remove unwanted habits in database, as they have been added because of the break_habit function (also the control_time_habit calls break_habit when not in time) 
    def tearDown(self) -> None:
        db.remove_deleted_habit("daily_habit_in_time")
        db.remove_deleted_habit("daily_habit_not_in_time")
        db.remove_deleted_habit("weekly_habit_in_time")
        db.remove_deleted_habit("weekly_habit_not_in_time")
        db.remove_deleted_habit("future_habit")
        db.remove_deleted_habit("already_finished_habit")
        return super().tearDown()
    

if __name__ == '__main__':
    unittest.main()
