"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar(calendar.SUNDAY)


def create_calendar(calendar_input):
    try:
        now = datetime.now()
        if (len(calendar_input) not in range(3)):
            print("Please type the date in the following format: MM YYYY")
            return
        if len(calendar_input) == 0:
            print(cal.formatmonth(now.year, now.month))
        elif len(calendar_input) == 1:
            print(cal.formatmonth(now.year, int(calendar_input[0])))
        elif len(calendar_input) == 2:
            print(cal.formatmonth(
                int(calendar_input[1]), int(calendar_input[0])))
    except Exception as e:
        print(f'Error: {e}')
        print("Please type the date in the following format: MM YYYY")
        exit()


calendar_input = sys.argv[1:]
create_calendar(calendar_input)
