def find_duplicate(nums):
    if isinstance(nums, str) or len(nums) == 0 or len(nums) == 1:
        return False
    original_list = nums.sort()
    duplicate_number_list = list()
    for i in range(len(original_list)):
        if original_list[i] == original_list[i+1]:
            duplicate_number_list.append(original_list[i])
    return duplicate_number_list
