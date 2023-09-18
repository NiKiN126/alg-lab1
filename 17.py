f = open('17.txt')
nums = [int(i) for i in f]
max_square_sum = count = 0
max_elem = -10001
for x in nums:
    if x % 10 == 3:
        max_elem = max(max_elem, x)
for i in range(len(nums) - 1):
    check_suf = (abs(nums[i]) % 10 == 3 and abs(nums[i + 1]) % 10 != 3) or (
                abs(nums[i]) % 10 != 3 and abs(nums[i + 1]) % 10 == 3)
    if check_suf and nums[i] ** 2 + nums[i + 1] ** 2 >= max_elem ** 2:
        count += 1
        max_square_sum = max(max_square_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, max_square_sum)
