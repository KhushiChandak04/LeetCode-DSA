class MinStack(object):
#normal stack -> stores all values, but minstack stores the most minimum val till that point

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value) #appends val to normal stack

        if not self.minstack: #first element of minstack
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minstack[-1])) #store the most min value between current and previous value here

    def pop(self):
        """
        :rtype: None
        """
        #remove top elements from both stacks
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        #return the last element here
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        #thats the last element of minstack
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()