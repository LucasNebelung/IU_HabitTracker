################################
###### Unit Test for database.py and functions outside of habit class in habit.py ######
##########################

#required libraries
import unittest 
import os
import sqlite3

# classes to be tested
import habit as hb
from database import database_controller



######## Methods to test database.py ########
class TestDatabase(unittest.TestCase):
    def setUp(self):
         self.db = database_controller()
         pass

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



if __name__ == '__main__':
    unittest.main()