class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0 #count of 5 doll bill
        ten = 0 #count of 10 doll bill

        for bill in bills:
            if bill == 5:
                five += 1 #no change needed

            elif bill == 10: #cust pays 10 doll, give them 5 doll back
                if five == 0:
                    return False
                five -= 1
                ten += 1
            
            else: #cust pays 20 doll, give them back 15 doll change
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1 #give them direct change
                elif five >= 3:
                    five -= 3
                else:
                    return False #cannot give correct change to them

        return True #all cust get exact change