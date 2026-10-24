class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #no of days in each month

        #convert the date into a count of day in the year
        def convert(date):
            month = int(date[0:2]) #first 2 dig before hyphen
            day = int(date[3:5]) #next 2 after hyphen

            for i in range(month-1): #add nums before the currrent month so do not incl that
                day += days[i]
            return day

        #now convert all dates given
        a1 = convert(arriveAlice)
        a2 = convert(leaveAlice)
        b1 = convert(arriveBob)
        b2 = convert(leaveBob)

        start = max(a1,b1) #choose later arrival date
        end = min(a2,b2) #choose earlier departure date

        if start > end:
            return 0 #they do not meet
            
        return end - start +1