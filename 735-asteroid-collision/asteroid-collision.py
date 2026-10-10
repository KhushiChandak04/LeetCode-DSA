class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # +ve is right and -ve is left, smaller always explodes, same size then both explode
        
        stack = [] #use stack to store the rem astroids that do not collide

        for a in asteroids:
            
            #check till the end of stack and if both are moving towards each other or no
            while stack and a < 0 and stack[-1] > 0:

                if abs(a) > stack[-1]: #if current is bigger than stack top
                    stack.pop() #prev explodes
                elif abs(a) == stack[-1]: #both equal
                    stack.pop()
                    a = 0
                    break
                else:
                    a = 0
                    break #if curr is smaller to prev the prev remains the same
            
            if a != 0:
                stack.append(a) #if asteroid survived append it to stack
                
        return stack