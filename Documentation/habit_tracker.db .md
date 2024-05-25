# Habit Tracker Database Documentation

## Database Schema

The Habit Tracker database consists of two main tables: `habits` and `habit_history`. Below is a description of the main properties and structure of these tables.

### Table: habits

The `habits` table stores information about each currently active habit tracked by the application. 

**Columns:**

1. **habit_name (TEXT, PRIMARY KEY)**
   - The name of the habit.
   - Example: "Brush teeth"

2. **habit_specification (TEXT)**
   - Detailed description of the habit.
   - Example: "Brush your teeth in the morning and evening"

3. **periodicity (TEXT)**
   - The frequency with which the habit should be performed.
   - Possible values: "day", "week"

4. **current_frequency (INTEGER)**
   - The current count of how many times the habit has been performed in the current period.

5. **frequency (INTEGER)**
   - The required number of times the habit should be performed within its periodicity.

6. **last_timestamp (TEXT)**
   - The timestamp of the last time the habit was updated in a TEXT format (not a datetime.date object)
   - Example: "2024-05-05"

7. **current_streak (INTEGER)**
   - The current streak of consecutive periods i.e. days or weeks the habit has been successfully maintained.

### Table: habit_history

The `habit_history` table stores historical data about the streaks of each habit.

**Columns:**

1. **id (INTEGER, PRIMARY KEY, AUTOINCREMENT)**
   - A unique identifier for each record in the history.

2. **historic_timestamp (TEXT)**
   - The timestamp of when the streak count was recorded i.e. the habit broken.
   - Example: "2024-04-04"

3. **streak_count (INTEGER)**
   - The streak count recorded at the given timestamp.
   - Example: 2

4. **habit_name (TEXT)**
   - The name of the habit associated with the historical record.
   - This column is a foreign key referencing `habit_name` in the `habits` table.
   - Example: "Brush teeth"