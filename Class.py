# -*- coding: utf-8 -*-
"""
A class that represents a class you'd take in school
Comparisons will be based on day and start/end time

@author: Cameron Zurmuhl 
@version: 1.0
"""

class Class(object):
    
    def __init__(self, name, Day, startTime, endTime):
        """
        creates the variables associated with the class
        :type name: String
        :param name: The name of the class
        
        :type Day: Day
        :param Day: The day the class is
        
        :type startTime: String
        :param startTime: the starting time of the class
        
        :type endTime: String
        :param endTime: the ending time of the class
        """
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.Day = Day
     
    def __lt__ (self, other):
        """
         Represents when this object is less than another
         :type other: Class
         :param other: The other object in comparison
        """
        return self.Day < other.Day or self.Day == other.Day and self.endTime < other.startTime
    def __le__ (self, other):
        """
         Represents when this object is less than or equal to another
         :type other: Class
         :param other: The other object in comparison
        """
        return self.Day < other.Day or self.Day == other.Day and self.endTime <= other.startTime 
    def __gt__(self, other):
        """
         Represents when this object is greater than another
         :type other: Class
         :param other: The other object in comparison
        """
        return self.Day > other.Day or self.Day == other.Day and self.startTime > other.endTime
    def __ge__(self, other):
        """
         Represents when this object is greater than or equal to another
         :type other: Class
         :param other: The other object in comparison
        """
        return self.Day > other.Day or self.Day == other.Day and self.startTime >= other.endTime
    
  
    def __eq__ (self, other):
        """
         Represents when this object is equal to another
         :type other: Class
         :param other: The other object in comparison
        """
        if self.Day == other.Day:
            if self.startTime == other.startTime or self.endTime == other.endTime:
                return True
            elif self.endTime <= other.endTime and self.startTime >= other.startTime:
                return True
            elif self.endTime >= other.endTime and self.startTime <= other.startTime:
                return True
            elif self.endTime >= other.endTime and self.startTime >= other.startTime and self.startTime <= other.endTime:
                return True
            elif self.endTime <= other.endTime and self.startTime <= other.startTime and self.endTime >= other.startTime:
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self):
        """
        Returns a String representation of this object
        """
        day = str(self.Day)
        outstr = "{0:<12}  {1:^12}  {2:>12}"
        return outstr.format(self.name.upper(), day, self.startTime + " - " + self.endTime)
    
    #Method scheduleString returns another formatted string that is differnt from __str__
    def scheduleString(self):
        """
        Method scheduleString returns a string representation of this object formatted
        for method printSchedule in ClassScheduler.py
        
        :returns: A String representation of this object
        """
        
        day = str(self.Day)
        outstr = "{0:<12}  {1:^12}  {2:>12}"
        return outstr.format(day, self.name.upper(), self.startTime + " - " + self.endTime)
    
    #Method csvRow returns the object in csv format
    def csvRow(self):
        """
        Method csvRow returns this object's fields in a list separated by commas for a csv file
        
        :returns: A list of this object's fields (as Strings) separated by commas 
        """
        day = str(self.Day)
        return [day,self.name,self.startTime,self.endTime]
        
    def getName(self):
        """
        Method getName returns this class's name
        :returns: This object's name as a string
        """
        return self.name
    def getDay(self):
        """
        Method getDay returns this class's Day
        :returns: The object's day of the week as a string
        """
        return self.Day.dayofWeek
    def getstartTime(self):
        """
        Method getstartTime returns this class's starting time
        :returns: The object's starting time as a string
        """
        return self.startTime
    def getendTime(self):
        """
        Method getendTime returns this class's ending time
        :returns: The object's ending time as a string
        """
        return self.endTime
    def setName(self, name):
        """
        Method setName changes this class's name
        :type name: String
        :param name: The new name of this object
        """
        self.name = name
    def setDay(self, Day):
        """
        Method setDay changes this class's Day
        :type Day: Day
        :param Day: the new Day for this object
        """
        self.Day = Day
    def setstartTime(self, time):
        """
        Method setstartTime changes the starting time for this class
        :type time: String
        :param time: The new starting time for this object
        """
        self.startTime = time
    def setendTime(self, time):
        """
        Method setendTime changes the ending time for this class
        :type time: String
        :param time: The new ending time for this object
        """
        self.endTime = time