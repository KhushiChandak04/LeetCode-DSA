class MyQueue(object):

    def __init__(self):
        self.stack1 = [] #stores elements to be pushed into the queue
        self.stack2 = [] #gives us front elements

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x) #add x to stack 1

    def pop(self):
        """
        :rtype: int
        """
        self.move() #make sure stack 2 has the front element
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stack2[-1] #return the front element without removing it

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def move(self):
        #onli move the elements if stack 2 is empty
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()