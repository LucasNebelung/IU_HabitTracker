##############################
# Backend ###################
##############################

# Importing modules
import datetime as dt
from database import database_controller
db = database_controller () 

# defining datetime objects
today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
one_week_ago = today - dt.timedelta(weeks=1)
one_day = dt.timedelta(days=1)
one_week = dt.timedelta(weeks=1) 

# defining Habit class
class Habit:
    def __init__(self, habit_name, habit_specification, periodicity, current_frequency, frequency, last_timestamp, current_streak):
        self.habit_name = habit_name
        self.habit_specification = habit_specification
        self.periodicity = periodicity
        self.current_frequency = current_frequency
        self.frequency = frequency
        self.last_timestamp = last_timestamp
        self.current_streak = current_streak

    def __str__(self):
        return f'Habit({self.habit_name}, {self.habit_specification}, {self.periodicity}, {self.current_frequency}, {self.frequency}, {self.last_timestamp}, {self.current_streak}, {self.is_in_time})'

    def control_time_habit(self):
        ''' Method to control whether the habit is in time or not based on Periodicity and last_timestamp.'''
        self.last_timestamp = dt.datetime.strptime(self.last_timestamp, "%Y-%m-%d").date()
        if self.periodicity == "day":
            if self.last_timestamp == yesterday and self.current_frequency == self.frequency:                  #this is the case when the habit is done how its supposed to be done
                self.last_timestamp = today
                self.current_frequency = 0
                self.current_streak += 1 
                print ("First case: Habit is done how its supposed to be done")
            elif self.last_timestamp < today and self.current_frequency < self.frequency:                      #this is the case when the habit has not been done often enough within the day
                self.break_habit()
                print ("Second case: Habit has not been done often enough within the day")
            elif self.last_timestamp < yesterday and self.current_frequency == self.frequency:                       #this is the case when the habit has been completly done within the day but the program was not started on the next day. 
                self.current_streak += 1                                                                             #In order to count the current streaks correctly, we still need to add 1 to current streak before it is broken
                self.break_habit()
                print ("Third case: Habit has been completly done within the day but the program was not started on the next day") 
            else:
                pass    
        elif self.periodicity == "week":
            if self.last_timestamp == one_week_ago and self.current_frequency == self.frequency:                  #this is the case when the habit is done how its supposed to be done and the next time period starts
                self.last_timestamp = today
                self.current_frequency = 0
                self.current_streak += 1
            elif self.last_timestamp < one_week_ago and self.current_frequency < self.frequency:                      #this is the case when the habit has not been done often enough within the week
                self.break_habit()
            elif self.last_timestamp < one_week_ago and self.current_frequency == self.frequency:                       #this is the case when the habit has been completly done within the week but the program was not started on the next week.
                self.current_streak += 1                                                                             #In order to count the current streaks correctly, we still need to add 1 to current streak before it is broken
                self.break_habit()
            else:
                pass
        self.last_timestamp = self.last_timestamp.strftime("%Y-%m-%d")
        return self.last_timestamp, self.current_frequency, self.current_streak 
    
    def check_off_habit(self):
        ''' Method to check off the habit. '''
        self.last_timestamp = dt.datetime.strptime(self.last_timestamp, "%Y-%m-%d").date()
        if self.current_frequency == self.frequency:
            print ("Unable to check off habit. You have already reached your goal for this habit")
        else:
            self.current_frequency += 1
            print (self.habit_name + " has been checked off successfully.")

        self.last_timestamp = self.last_timestamp.strftime("%Y-%m-%d")
        return self.current_frequency, self.current_streak, self.last_timestamp
         
    
    def break_habit(self):
        ''' Method to break the habit. 
        Current_Frequency, Current_Streak are reset to zero and last_timestamp is set to today.'''
        self.current_frequency = 0
        self.current_streak = 0
        self.last_timestamp = today
        print (self.habit_name + " streak has been broken.")
        #hier noch Methode hinzufügen, dass Daten auch in die habit_history Tabelle geschrieben werden

def load_all_habits():
    max_rows = db.get_number_of_rows()
    rows = 0
    while rows < max_rows:
        global habit1
        habit1 = Habit (db.get_habit_by_row (0)[0], db.get_habit_by_row (0)[1], db.get_habit_by_row (0)[2], db.get_habit_by_row (0)[3], db.get_habit_by_row (0)[4], db.get_habit_by_row (0)[5], db.get_habit_by_row (0)[6])
        habit1.control_time_habit()
        db.update_habit(habit1.habit_name, habit1.current_frequency, habit1.current_streak, habit1.last_timestamp)
        rows += 1
        if rows == max_rows:
            return habit1
        
        global habit2
        habit2 = Habit (db.get_habit_by_row(1)[0], db.get_habit_by_row(1)[1], db.get_habit_by_row(1)[2], db.get_habit_by_row(1)[3], db.get_habit_by_row(1)[4], db.get_habit_by_row(1)[5], db.get_habit_by_row(1)[6])
        habit2.control_time_habit()
        db.update_habit(habit2.habit_name, habit2.current_frequency, habit2.current_streak, habit2.last_timestamp)
        rows += 1
        if rows == max_rows:
            return habit1, habit2
        
        global habit3
        habit3 = Habit (db.get_habit_by_row(2)[0], db.get_habit_by_row(2)[1], db.get_habit_by_row(2)[2], db.get_habit_by_row(2)[3], db.get_habit_by_row(2)[4], db.get_habit_by_row(2)[5], db.get_habit_by_row(2)[6])
        habit3.control_time_habit()
        db.update_habit(habit3.habit_name, habit3.current_frequency, habit3.current_streak, habit3.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3
        
        global habit4
        habit4 = Habit (db.get_habit_by_row(3)[0], db.get_habit_by_row(3)[1], db.get_habit_by_row(3)[2], db.get_habit_by_row(3)[3], db.get_habit_by_row(3)[4], db.get_habit_by_row(3)[5], db.get_habit_by_row(3)[6])
        habit4.control_time_habit()
        db.update_habit(habit4.habit_name, habit4.current_frequency, habit4.current_streak, habit4.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4
        
        global habit5
        habit5 = Habit (db.get_habit_by_row(4)[0], db.get_habit_by_row(4)[1], db.get_habit_by_row(4)[2], db.get_habit_by_row(4)[3], db.get_habit_by_row(4)[4], db.get_habit_by_row(4)[5], db.get_habit_by_row(4)[6])
        habit5.control_time_habit()
        db.update_habit(habit5.habit_name, habit5.current_frequency, habit5.current_streak, habit5.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5
        
        global habit6
        habit6 = Habit (db.get_habit_by_row(5)[0], db.get_habit_by_row(5)[1], db.get_habit_by_row(5)[2], db.get_habit_by_row(5)[3], db.get_habit_by_row(5)[4], db.get_habit_by_row(5)[5], db.get_habit_by_row(5)[6])
        habit6.control_time_habit()
        db.update_habit(habit6.habit_name, habit6.current_frequency, habit6.current_streak, habit6.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6
        
        global habit7
        habit7 = Habit (db.get_habit_by_row(6)[0], db.get_habit_by_row(6)[1], db.get_habit_by_row(6)[2], db.get_habit_by_row(6)[3], db.get_habit_by_row(6)[4], db.get_habit_by_row(6)[5], db.get_habit_by_row(6)[6])
        habit7.control_time_habit()
        db.update_habit(habit7.habit_name, habit7.current_frequency, habit7.current_streak, habit7.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7
        
        global habit8
        habit8 = Habit (db.get_habit_by_row(7)[0], db.get_habit_by_row(7)[1], db.get_habit_by_row(7)[2], db.get_habit_by_row(7)[3], db.get_habit_by_row(7)[4], db.get_habit_by_row(7)[5], db.get_habit_by_row(7)[6])
        habit8.control_time_habit()
        db.update_habit(habit8.habit_name, habit8.current_frequency, habit8.current_streak, habit8.last_timestamp)
        rows += 1
        if rows == max_rows: 
            return habit1, habit2, habit3, habit4, habit5, habit6, habit7, habit8

def print_current_streaks (): 
    current_streaks = db.get_current_streaks()
    for habit in current_streaks:
        print(f"{habit[0]}: Current Streak: {habit[1]}")


#########################
###### Test Area ########
#########################



# def __init__(self, habit_name, habit_specification, periodicity, current_frequency, frequency, last_timestamp, current_streak):

'''Testhabit = Habit("Testhabit", "Test", "week", 3, 3, "2024-04-14", 0)


print (Testhabit.current_frequency)
print (Testhabit.frequency)
print (Testhabit.current_streak)
print (Testhabit.last_timestamp)
print ("-----------------") 
Habit.control_time_habit(Testhabit)
print ("-----------------") 
print (Testhabit.current_frequency)
print (Testhabit.frequency)
print (Testhabit.current_streak)
print (Testhabit.last_timestamp)
'''
