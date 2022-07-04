def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    copy_list = list()
    for number in nums:
        if type(number) != int or number <= 0:
            return False
        if number not in copy_list:
            copy_list.append(number)
        else:
            return number
    return False
