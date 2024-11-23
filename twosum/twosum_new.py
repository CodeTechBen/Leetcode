def twoSum(nums: list[int], target: int) -> list[int]:
    dict_of_key_value = {}
    for key, num in enumerate(nums):
        find_num = target - num
        if find_num in dict_of_key_value:
            return [dict_of_key_value[find_num], key]
        
        dict_of_key_value[num] = key
