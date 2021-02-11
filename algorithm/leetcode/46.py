import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        sol = [[nums[0]]]
        for i in range(1, n): # Recursively find permutations of elements 0 to i of nums
            new_sol = []
            a = nums[i]
            for j in range(i+1):
                new_sol.extend([x[:j]+[a]+x[j:] for x in sol])
            sol = new_sol
        return sol