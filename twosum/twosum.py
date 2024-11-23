def twoSum(nums: list[int], target: int) -> list[int]:  
    for l, num1 in enumerate(nums):
        for r, num2 in enumerate(nums):
            if l != r and num1 + num2 == target:
                return [l,r]

    
            
if __name__ == "__main__":
    print(f'the index of the two that will sum to target are: {twoSum([1,2,3,4], 3)}')