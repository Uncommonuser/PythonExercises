#Automate the Boring Stuff: Chapter 7 Practice Problem: Date Detection
#Write a regular expression that can detect dates in the DD/MM/YYYY format.
#Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
#Note that if the day or month is a single digit, it’ll have a leading zero.

import re

def datedetect(date):
    day = None
    month = None
    year = None

    dateRegex = re.compile(r'''(
                (^\d{2}) #DD with caret to indicate match must occur at beginning of string
                \/      #backslash
                (\d{2}) #MM
                \/      #backslash
                (\d{4}$))#YYYY with dollar sign to indicate match must end with pattern
                ''', re.VERBOSE)

    if dateRegex.search(date) is not None:
        dategroup = dateRegex.search(date)
        day = int(dategroup.group(2))
        month = int(dategroup.group(3))
        year = int(dategroup.group(4))
        #print(dategroup)
        #print(type(dategroup))
        #print(dategroup.groups())
        #print(dategroup.group())
        print(day,month,year)
    #month validator
        if month <= 0 or month > 12:
            return 'Month is invalid!'
        if day <=0:
            return 'Day cannot be negative!'
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day >30:
                return 'Month cannot have more than 30 days in April, June, September, or November!'
        if month == 2:
            if year%4 == 0:
                if year%100 == 0 and year%400 == 0:
                    if day > 29:
                        return 'February cannot have more than 29 days on a leap year!'
                elif year%100 == 0 and year%400 != 0:
                    if day > 28:
                        return 'February cannot have more than 28 days on a non-leap year!'
                else:
                    if day > 29:
                        return 'February cannot have more than 29 days on a leap year!'
            else:
                if day > 28:
                    return 'February cannot have more than 28 days on non-leap years!'
        if day > 31:
            return 'Months cannot have more than 31 days!'
        else:
            return "Valid date entered", date


print(datedetect('02/31/2008'))
print(datedetect('31/07/2008'))
print(datedetect('13/02/2008'))
print(datedetect('63/04/2008'))
print(datedetect('56/03/2008'))
print(datedetect('28/02/2008'))
print(datedetect('29/02/2008'))
print(datedetect('30/02/2002'))
print(datedetect('30/02/2000'))
print(datedetect('30/02/3000'))
print(datedetect('30/02/2008'))
