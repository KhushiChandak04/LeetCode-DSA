class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        #numbers we can use
        numbers = []
        for i in range(1, n + 1):
            numbers.append(i)

        #keep track of how many permutations we made
        count = [0]
        #store the kth permutation
        answer = [""]

        def generate(current, used):

            #if we used all numbers, one permutation is complete
            if len(current) == n:
                #increase the permutation count
                count[0] += 1
                #if this is the kth permutation, store it
                if count[0] == k:
                    answer[0] = current
                return

            #try every number
            for i in range(n):
                #if number is already used, skip it
                if used[i] == True:
                    continue
                #mark this number as used
                used[i] = True
                #add this number to current permutation
                generate(current + str(numbers[i]), used)
                #if we already found kth permutation, stop
                if answer[0] != "":
                    return
                #make this number available again
                used[i] = False

        #initially no number is used
        used = [False] * n
        #start generating permutations
        generate("", used)
        return answer[0]