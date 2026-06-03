class MyCalendar(object):

    def __init__(self):
        self.calendar = [] #inbuilt setup

    def book(self, startTime, endTime):
        for start, end in self.calendar:
            if startTime < end and endTime > start: #new meeting starts before old ends and new meeting ends after old starts
                return False 
        self.calendar.append([startTime, endTime])
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)