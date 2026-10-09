class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent #stores the parent of every node
        self.locked = [0] * len(parent) #0 = unlocked, otherwise locked
        self.children = [[] for i in range(len(parent))]

        for i in range(1, len(parent)):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locked[num] != 0: #if node is already locked
            return False
        self.locked[num] = user #lock node for this user
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        #onli the user who locked the node can unlock it
        if self.locked[num] != user:
            return False
        self.locked[num] = 0 #unlock the node
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        #check if node is already locked
        if self.locked[num] != 0:
            return False

    #check if any parent is locked
        p = self.parent[num]

        while p != -1:
            if self.locked[p] != 0:
                return False
            p = self.parent[p]

    #check all descendants
        stack = self.children[num][:]
        found = False

        while stack:
            node = stack.pop()

            #if descendant is locked, unlock it
            if self.locked[node] != 0:
                self.locked[node] = 0
                found = True

        #add its children to check them too
            for child in self.children[node]:
                stack.append(child)

    #if no locked descendant was found
        if found == False:
            return False

    #lock the current node
        self.locked[num] = user
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)