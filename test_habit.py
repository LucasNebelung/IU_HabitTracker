#################################
######## UNIT TEST OF the Habit class in habit.py ####
#################################


#required libraries
import unittest
import datetime as dt 
import sqlite3
import os

# classes to be tested
from habit import Habit  


# defining datetime objects
today = dt.date.today()    # dt.date(2024,5,20) is a convenient way to simulate different dates and test if everything works accordingly
yesterday = today - dt.timedelta(days=1)
one_week_ago = today - dt.timedelta(weeks=1)
more_than_one_week_ago = today - dt.timedelta(weeks=2)
future_date = today + dt.timedelta(weeks=4)
one_day = dt.timedelta(days=1)
one_week = dt.timedelta(weeks=1) 

class TestHabit(unittest.TestCase):
    def setUp(self):
        # Creating instances of habits to test to simulate different scenarios and test whether the functions work as expected
        self.habit1 = Habit("daily_habit_in_time", "Description 1", "day", 0, 1, today.strftime("%Y-%m-%d") , 0)
        self.habit2 = Habit("daily_habit_not_in_time", "Description 2", "day", 2, 3, yesterday.strftime("%Y-%m-%d"), 1)
        self.habit3 = Habit ("weekly_habit_in_time", "Description 3", "week", 4, 5, one_week_ago.strftime("%Y-%m-%d"), 2)
        self.habit4 = Habit ("weekly_habit_not_in_time", "Description 4", "week", 6, 7, more_than_one_week_ago.strftime("%Y-%m-%d"), 3)
        self.habit5 = Habit ("future_habit", "Description 5", "weeek", 0, 3, future_date.strftime("%Y-%m-%d"), 4)
        self.habit6 = Habit ("already_finished_habit", "Description 6", "day", 1 , 1, today.strftime("%Y-%m-%d"), 5)
        
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
    

if __name__ == '__main__':
    unittest.main()
