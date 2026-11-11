class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def isLeap(year): #chk all cases of leap year first
            if year % 400 == 0:
                return True
            if year % 100 == 0: #div by 4 AND NOT div by 100 case
                return False
            if year % 4 == 0:
                return True
            return False #otherwise

        def countDays(date): #count total days frm year 1
            #split the year into 3 parts by slicing
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])

            total = 0 #initilise here

            for y in range(1, year): #count days frm all prev yrs, to see how many days have passed befor reaching the curr yr
                if isLeap(y):
                    total += 366
                else:
                    total += 365
            
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #no if days in each month

            if isLeap(year):
                months[1] = 29 #in case of leap year make 29 days for february

            for i in range(month -1): #as indexing is from 0
                total += months[i] #add days of months till current date

            total += day #add upto current day
            return total

        days1 = countDays(date1)
        days2 = countDays(date2)

        return abs(days1 - days2) #return absolute value difference