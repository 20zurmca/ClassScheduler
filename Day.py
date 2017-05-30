# -*- coding: utf-8 -*-
"""
class Day represents a day of the week

@author: Cameron Zurmuhl
@version: 1.0
"""

#%%  

class Day(object):
    
    DAY_OF_WEEK_INT = None #Converting the day of the week to an interger for comparison
    
    def __init__(self, dayofWeek):
        """
        creates the variables associated with the class
        :type dayofWeek: String
        :param dayofWeek: the day of the week
        """
        #Set the DAY_OF_WEEK_INT according to the first letter(s) of dayofWeek
        if dayofWeek[0].lower() == "m":
             self.dayofWeek = "Monday"
             self.DAY_OF_WEEK_INT = 0
        elif dayofWeek[0].lower() == "t" and dayofWeek[1].lower() == "u":
             self.dayofWeek = "Tuesday"
             self.DAY_OF_WEEK_INT = 1
        elif dayofWeek[0].lower() == "w":
             self.dayofWeek = "Wednesday"
             self.DAY_OF_WEEK_INT = 2
        elif dayofWeek[0].lower() == "r" or (dayofWeek[0].lower() == "t" and dayofWeek[1].lower() == "h") or (dayofWeek[0].lower() == "t" and dayofWeek[1].lower() == "r"):
             self.dayofWeek = "Thursday"
             self.DAY_OF_WEEK_INT = 3
        elif dayofWeek[0].lower() == "f":
             self.dayofWeek = "Friday"
             self.DAY_OF_WEEK_INT = 4
        elif dayofWeek[0].lower() == "s" and dayofWeek[1].lower() == "a":
              self.dayofWeek = "Saturday"
              self.DAY_OF_WEEK_INT = 5
        else:
              self.dayofWeek = "Sunday"
              self.DAY_OF_WEEK_INT = 6
              
              
    def __lt__ (self, other):
        """
        Represents when this object is less than another
        :type other: Day
        :param other: The other object in comparison
        """
        return self.DAY_OF_WEEK_INT < other.DAY_OF_WEEK_INT
    def __gt__(self, other):
        """
        Represents when this object is greater than another
        :type other: Day
        :param other: The other object in comparison
        """
        return self.DAY_OF_WEEK_INT > other.DAY_OF_WEEK_INT
  
    def __eq__ (self, other):
        """
        Represents when this object is equal to another
        :type other: Day
        :param other: The other object in comparison
        """
        return self.DAY_OF_WEEK_INT == other.DAY_OF_WEEK_INT
    
    def __ne__ (self, other):
        """
        Represents when this object is not equal to another
        :type other: Day
        :param other: The other object in comparison
        """
        return self.DAY_OF_WEEK_INT != other.DAY_OF_WEEK_INT
                
    
    def __str__(self):
        """
        Returns a string representation of this object
        """
        return self.dayofWeek
    
    def getDay(self):
        """
        Method getDay returns this object's day of the week as an integer
        :returns: an integer representing a day of the week (Monday = 0)
        """
        return self.DAY_OF_WEEK_INT