def find_duplicate(nums):
    original_list = nums.sort()
    if isinstance(nums, str) or len(nums) == 0 or len(nums) == 1 or nums[0] < 0:
        return False    

    duplicate_number_list = list()
    for i in range(len(original_list)):
        if original_list[i] == original_list[i+1]:
            duplicate_number_list.append(original_list[i])
    return duplicate_number_list
