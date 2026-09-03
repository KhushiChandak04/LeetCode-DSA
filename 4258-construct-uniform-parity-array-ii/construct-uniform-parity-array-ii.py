class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        #for every number whose parity is different from the smallest number, we need a smaller number of the opposite parity(odd/even)

        nums1.sort()
        first_parity = nums1[0] % 2 #first number cannot be changed so its parity is same as final parity
        has_odd = (nums1[0] % 2 == 1) #we have seen an odd or even number before
        has_even = (nums1[0] % 2 == 0)

        for i in range(1,len(nums1)):
            if nums1[i] % 2 == 1: #odd
                if first_parity == 0 and not has_odd: #to make it even do we need a smaller odd number or no?????
                    return False
                has_odd = True

            else: #current number is even
                if first_parity == 1 and not has_odd:
                    return False
                has_even = True
        return True