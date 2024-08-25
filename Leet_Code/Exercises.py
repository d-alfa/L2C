# ===================
# 1. Two Sum
# ===================

# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashmap = {}

#         for i, num in enumerate(nums):
#             new_num = target - num
#             if new_num in hashmap:
#                 return [hashmap[new_num], i]
#             hashmap[num] = i

# solution = Solution()
# result_1 = solution.twoSum([2,7,11,15], 9)
# result_2 = solution.twoSum([3,2,4], 6)
# result_3 = solution.twoSum([3,3], 6)

# print(result_1) # [0,1]
# print(result_2) # [1,2]
# print(result_3) # [0,1]

# ===================
# 9. Palindrome Number
# ===================

# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         x = str(x)
#         return x == x[::-1]
    
# solution = Solution()
# result_1 = solution.isPalindrome(121)
# result_2 = solution.isPalindrome(-121)
# result_3 = solution.isPalindrome(10)

# print(result_1) # True
# print(result_2) # False
# print(result_3) # False

# ===================
# 13. Roman to Integer
# ===================

# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         total = 0
#         roman = {
#             "I" : 1,
#             "V" : 5,
#             "X" : 10,
#             "L" : 50,
#             "C" : 100,
#             "D" : 500,
#             "M" : 1000,
#         }
#         for i in range(len(s)-1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 total -= roman[s[i]]
#             else:
#                 total += roman[s[i]]
#         return total + roman[s[-1]]
    
# solution = Solution()
# result_1 = solution.romanToInt("III")
# result_2 = solution.romanToInt("LVIII")
# result_3 = solution.romanToInt("MCMXCIV")

# print(result_1) # 3
# print(result_2) # 58
# print(result_3) # 1994

# ===================
# 14. Longest Common Prefix
# ===================

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
#         prefix = strs[0]
#         for string in strs[1:]:
#             while not string.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix
                
# solution = Solution()
# result_1 = solution.longestCommonPrefix(["flower","flow","flight"])
# result_2 = solution.longestCommonPrefix(["dog","racecar","car"])

# print(result_1) # "fl"
# print(result_2) # ""

# ===================
# 20. Valid Parentheses
# ===================

# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         stack = []
#         pairs = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }

#         for bracket in s:
#             if bracket in pairs:
#                 stack.append(bracket)
#             elif len(stack) == 0 or bracket != pairs[stack.pop()]:
#                 return False
        
#         return len(stack) == 0
    
# solution = Solution()
# result_1 = solution.isValid("()")
# result_2 = solution.isValid("()[]{}")
# result_3 = solution.isValid("(]")
# result_4 = solution.isValid("([])")

# print(result_1) # True
# print(result_2) # True
# print(result_3) # False
# print(result_4) # True

# ===================
# 26. Remove Duplicates from Sorted Array
# ===================

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
    
# solution = Solution()
# result_1 = solution.removeDuplicates([1,1,2])
# result_2 = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

# print(result_1) # [1,2] length 2
# print(result_2) # [0,1,2,3,4] length 5

# ===================
# 27. Remove Element
# ===================

# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         index = 0
#         for n in range(len(nums)):
#             if nums[n] != val:
#                 nums[index] = nums[n]
#                 index += 1
#         return index
    
# solution = Solution()
# result_1 = solution.removeElement([3,2,2,3],3)
# result_2 = solution.removeElement([0,1,2,2,3,0,4,2],2)

# print(result_1) # [2,2] length 2
# print(result_2) # [0,1,3,0,4] length 5

# ===================
# 66. Plus One
# ===================

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         for i in reversed(range(len(digits))):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0

#         return [1] + digits
    
# solution = Solution()
# result_1 = solution.plusOne([1,2,3])
# result_2 = solution.plusOne([4,3,2,1])
# result_3 = solution.plusOne([9])

# print(result_1) # [1,2,4]
# print(result_2) # [4,3,2,2]
# print(result_3) # [1,0]

# ===================
# 121. Best Time to Buy and Sell Stocks
# ===================

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         buy = prices[0]
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] < buy:
#                 buy = prices[i]
#             elif prices[i] - buy > profit:
#                 profit = prices[i] - buy
#         return profit
    
# solution = Solution()
# result_1 = solution.maxProfit([7,1,5,3,6,4])
# result_2 = solution.maxProfit([7,6,4,3,1])

# print(result_1) # 5
# print(result_2) # 0

# ===================