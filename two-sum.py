#https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
  dict = {} 
  for index, value in enumerate(nums):
    diff = target - value
    if diff in dict:
      return [dict[diff],index]
    else:
      dict[value] = index

print(twoSum([2,5,3,6,0,8,14],19))