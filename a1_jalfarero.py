#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_jalfarero.py
Author: Jordan Alfarero
The python code in this file a1_jalfarero.py is original work written by
Jordan Alfarero. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys
import calendar

user_raw_data = sys.argv[1]

#user_raw_data1 = user_raw_data.replace("/", "")
#user_raw_data2 = user_raw_data1.replace(".", "")
#sanitize = user_raw_data2.replace("-", "")
#allow_chars = '0123456789'

def size_check(sanitize,):
    if len(sanitize) != 8:
         x = False
    else:
         x = True

    return x

def sanitize(user_raw_data):
    sanitize_data = ''
    for i in user_raw_data:
        if i == '/':
             outchar = ''
        elif i == '-':
             outchar = ''
        elif i == '.':
             outchar = ''
        sanitize_data += outchar
        return sanitize_data

def leap_year(l_year):
    """
    Takes the year from sanitized user input (YYYY) and returns it True if it is a leap year
    or false if it is not a leap year.
    """
    l_year = int(sanitize[0:4])
    if calendar.isleap(l_year):
       x = True 
    else:
       x = False  
    
    return x
def range_check(l_year,years):
    """
    Takes the year from sanitized user input (YYYY) and determines if it falls within
    the appropriate range of 1900 and 9999.
    """
    years = (1900, 9999)
    if int(l_year) in years[0:1]:
       x = True
    else:
       x = False

    return x

#    if y_year <= yearmin:
#         return False
#    elif y_year >= yearmax:
#         return False
#    else:
#         return True

def month_check(x_month):
    x_month = sanitize[4:6]
    if 1 <= x_month <= 12:
         x = True
    else:
         x = False
 
    return x

def day_check(x_day, int):
    x_day = int(sanitize[6:])
    if x_day > 31:
         x = False
    else:
         x = True
   
    return x

def usage():
    
    use = """
    Usage: a1_jalfarero.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD

    """
    print(use)
    exit()

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}
   user_raw_data = sys.argv[1]
   allow_chars = '0123456789'
   dob = sanitize
   result = size_check
#   if len(sanitize) == 8 and sanitize.isdigit():
#       print("Sanitized user data:", dob)
#   else:
#       print("Error 09: wrong date entered")
#       sys.exit()
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
#   result = range_check
#   if result == False:
   if year < 1900: 
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   if month > 12:
       print("Error 02: Wrong month entered")
       sys.exit()
   elif month < 1:
       print("Error 02: Wrong month entered")
       sys.exit()
#   result = leap_year
   if calendar.isleap(year):
       days_in_month[2] = 29
   else:
       print("Error 03: wrong day entered")
#   result = day_check
   if day > 31:
       print("Error 03: wrong day entered")
       sys.exit()
   elif day < 1:
       print("Error 03: wrong day entered")
       sys.exit()
#   elif day != days_in_month
#       print("Error 03: wrong day entered")
#       sys.exit()
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   print("Your date of birth is:", new_dob)
