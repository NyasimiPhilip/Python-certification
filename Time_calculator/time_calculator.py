#!/usr/bin/python3
"""
The add_time function calculates the resulting time after adding a given duration to a given start time. It takes three parameters: start (the starting time in the format 'HH:MM AM/PM'), duration (the duration to add in the format 'HH:MM'), and an optional start_day_of_week parameter (the starting day of the week as a string)."""
def add_time(start, duration, start_day_of_week=None):
    # Days of week dictionary for converting day of the week to numerical value
    days_of_week_dictionary = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    # List of days of the week for converting numerical value back to day of the week string
    list_of_days_weeks = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Split start time into hours and minutes
    start_hours, start_minutes_plus_am_pm = start.split(":")
    start_hours = int(start_hours)
    start_minutes_tuple = start_minutes_plus_am_pm.partition(" ")
    start_minutes = int(start_minutes_tuple[0])
    start_am_pm = (start_minutes_tuple[2])
    am_pm_flip_dictionary= {"AM":"PM","PM":"AM"}

    # Split duration into hours and minutes
    duration_hours, duration_minutes = duration.split(":")
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
    # Calculate the resulting time

    result_minutes = start_minutes + duration_minutes # Adds minutes and if greater than 60 increments hours
    if result_minutes >= 60:
        duration_hours += 1
        result_minutes = result_minutes % 60
    result_hours = (start_hours + duration_hours) % 12 # Adds hours and divides by  12 returning remainder (time in 12hrs) or 0


    No_of_am_pm_flips= (start_hours + duration_hours)// 12 # carries out integer division returning the number of times the total sum of hours has exceeded 12 and hence number of times AM has changed to PM and vice versa
    number_of_days = duration_hours// 24

    int_div = (duration_hours // 24)
    if  (int_div) != 0:
     extra_hours = duration_hours % 24
     if extra_hours > 0  :
       number_of_days += 1
    if start_am_pm == "PM" and No_of_am_pm_flips == 1:
      number_of_days += 1

    #if start_am_pm == "PM" and result_hours == 0:
      #number_of_days += 1
    result_hours = result_hours = 12 if result_hours == 0 else result_hours
    if No_of_am_pm_flips == 0:
     start_am_pm= start_am_pm
    else:
         start_am_pm= am_pm_flip_dictionary[start_am_pm] if No_of_am_pm_flips % 2 != 0 else start_am_pm



    # Calculate the resulting day of the week
    if start_day_of_week is not None:
        start_day_of_week =start_day_of_week.lower()


        # Handle case where start_day_of_week is not a valid day of the week
        if start_day_of_week not in days_of_week_dictionary:
            raise ValueError("Invalid day of the week")
        Index = ((days_of_week_dictionary[start_day_of_week] + (number_of_days )) % 7)
        New_day = ", "+list_of_days_weeks[Index]
    elif start_day_of_week is None:
      New_day= ""
    # Debugging output
    #print("start_hours:", start_hours)
    #print("start_minutes:", start_minutes)
    #print("result_hours:", result_hours)
    #print("result_minutes:", result_minutes)
    #print("No_of_am_pm_flips:", No_of_am_pm_flips)
    #print("number_of_days:", number_of_days)
    #print("New_day:", New_day)
    #print (check)
    #print(int_div)
    resulting_time= f"{result_hours}:{result_minutes:02d} {start_am_pm}"
    if number_of_days == 1:
      resulting_time= f"{resulting_time}{New_day} (next day)"
      New_day= ""

    elif number_of_days > 1:
      resulting_time= f"{resulting_time}{New_day} ({number_of_days} days later)"
      New_day= ""

    # Debugging output
   # print("resulting_time:", resulting_time)

    # Return the resulting time as a string in the format 'HH:MM DayOfWeek'
    return f"{resulting_time}{New_day}"
