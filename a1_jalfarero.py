#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_jalfarero.py (replace [Seneca_name] with your Seneca User name)
Author: Jordan Alfarero
The python code in this file (a1_jalfarero.py) is original work written by
Jordan Alfarero. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    """
    Takes the year from user input YYYY and return it True if it is a leap year
    or False if it is not a leap year.
    """
    if (obj % 4) ==0:
       if (obj % 100) ==0:
          if (obj % 400) ==0:
             output = True
          else:
             output = False
       else:
          output = True
    else:
      output = False
    return output

def sanitize(obj1,obj2):
    """
    Takes out characters that would otherwise disrupt the functionality of the script
    and ensures only required values remain
    """
    cleanse = ''
    for char in obj1:
        if char in obj2:
           cleanse += char
    return cleanse

def size_check(obj, intobj):
    """
    Determines the appropriate size for user input
    """
    if len(obj) == intobj:
         output = True
    else:
         output = False
    return output

def range_check(obj1,obj2):
    """
    Takes the year from sanitized user input (YYYY) and determines if it falls within
    the appropriate range of 1900 and 9999.
    """
    if int(obj1) in range(obj2[0],obj2[1]+1):
       output = True
    else:
       output = False  
   
    return output

def usage():
    """
    Message on script's use if it is not being used for it's purpose
    """ 
    use = """Usage: a1_jalfarero.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"""
    print(use)
    exit()

if __name__ == "__main__":
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # ste 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6 
   result = range_check(year,(1900,9999))
   if result == False: 
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
#   print("Your date of birth is:", new_dob)
   print(new_dob)
