def twoSum(nums: list[int], target: int) -> list[int]:
        # Dictionary to store the value and its index
        num_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = i