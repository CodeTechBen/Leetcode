'''Implementation of a two-sum problem solution. It finds two indices in a list such that their values add up to a target sum.'''
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''Returns indices of the two numbers such that they add up to target.'''
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

if __name__ == "__main__":
    input = [2, 7, 11, 15]
    target = 9
    output = [0, 1]
    twoSumSolver = Solution()
    result = twoSumSolver.twoSum(input, target)
    assert result == output, f"Expected {output}, but got {result}"
    print(f"Input: {input}, Target: {target}, Output: {output}")# This is a simple script to demonstrate a two-sum problem solution.