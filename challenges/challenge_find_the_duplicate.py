def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1 or nums[0] <= 0:
        return False
    copy_list = list()
    for number in nums:
        if type(number) != int:
            return False
        if number not in copy_list:
            copy_list.append(number)
        else:
            return number
    return False
