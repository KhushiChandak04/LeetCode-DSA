class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = zip(position, speed) #we are pairing them cuz every car has both speed and pos and spped and both parameters determine the fleeet
        cars = sorted(cars, reverse=True) #closest to target first
        stack = [] #empty stack
        for pos, spd in cars:
            time = float(target - pos) / spd #time = dist/speed

            if not stack or time > stack[-1]: #if cannot catch the fleet ahead, then new fleet
                stack.append(time)
            #otherwise do nthng just join the fleet
        return len(stack)