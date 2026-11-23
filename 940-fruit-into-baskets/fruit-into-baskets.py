class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0 #we will use sliding window here
        count = {} #make a dictionatry
        ans = 0

        for right in range(len(fruits)):
            fruit = fruits[right] #take fruit at curr pos

            if fruit in count:
                count[fruit] += 1 #if fruit type alrd in our basket
            else:
                count[fruit] = 1 #else add new cateory
            
            while len(count) > 2: #we have 2 baskets sand can take 2 distinct types of fruits
                count[fruits[left]] -= 1 #reduce the window size

                if count[fruits[left]] == 0: #no fruits of this tyle left thenremove its entry
                    del count[fruits[left]]
                left += 1 #move the window

            length = right - left +1

            if length > ans:
                ans = length
        return ans