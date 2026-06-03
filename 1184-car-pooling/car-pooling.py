class Solution(object):
    def carPooling(self, trips, capacity):
        passengers = [0] * 1001 #due to constraints given in prob
        
        for numPassengers, start, end in trips:
            passengers[start] += numPassengers #pick up
            passengers[end] -= numPassengers #drop off
        currentPassengers = 0 #initialise their count
        for i in range (1001):
            currentPassengers += passengers[i] #increment total count
            if currentPassengers > capacity: #exceeds capacity
                return False
        return True