class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10**9 + 7 #limits
        inventory.sort(reverse = True)
        inventory.append(0)
        profit = 0 #initialise
        colours = 1 #how many colours are at currrent highest level

        for i in range(len(inventory) - 1):
            high = inventory[i]
            low = inventory[i+1]
            levels = high - low
            totalballs = colours * levels

            if orders >= totalballs:
                profit += colours * ((high + low + 1 )* levels // 2)
                orders -= totalballs
            else:
                rows = orders // colours
                extra = orders % colours
                stop = high - rows
                profit += colours * ((high + stop + 1) * rows // 2)
                profit += extra * stop
                return profit % MOD
            colours += 1
        return profit % MOD