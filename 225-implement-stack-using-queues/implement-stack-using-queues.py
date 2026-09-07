class MyStack(object):

    def __init__(self):
        self.queue1 = [] #stores stack elements
        self.queue2 = [] #temporary queue

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue2.append(x)
        while len(self.queue1) > 0:
            self.queue2.append(self.queue1.pop(0)) #add popped element from queue1 to queue2
        #swap queue 1 and queue 2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()