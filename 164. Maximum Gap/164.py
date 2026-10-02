
def bucket_sort(nums):
    min_num = min(nums)
    max_num = max(nums)
    if len(nums) < 2:
        return nums
    range_num = max_num - min_num
    buckets = [[] for _ in range(len(nums))]
    numBuckets = len(nums)
    if range_num == 0:
        return nums
    for i in range(len(nums)):
        index = (nums[i] - min_num) // (range_num + 1) * numBuckets 
        buckets[index].append(nums[i])
    for i in range(numBuckets):
        buckets[i].sort()
    ind = 0
    for i in buckets:
        for j in i:
            nums[ind] = j
            ind += 1
    return nums
nums = list(map(int, input().split()))
nums = bucket_sort(nums)
max_diff = 0
for i in range(len(nums) - 1):
    diff = nums[i + 1] - nums[i]
    if diff > max_diff:
        max_diff = diff
print(max_diff)