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
# Time complexity : O(N*M)
# ===================

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
#         # Start with the first string
#         prefix = strs[0]
#         # Compare with each string
#         for string in strs[1:]:
#             # Check if current string starts with the prefix
#             while not string.startswith(prefix):
#                 # Shorten the prefix
#                 prefix = prefix[:-1]
#                 # If prefix is empty, no common prefix
#                 if not prefix:
#                     return ""
#         return prefix
                
# solution = Solution()
# result_1 = solution.longestCommonPrefix(["flower","flow","flight"])
# result_2 = solution.longestCommonPrefix(["dog","racecar","car"])

# print(result_1) # "fl"
# print(result_2) # ""

# ===================
# 15. 3Sum
# ===================
# Array
# Two_Pointers
# Sorting
# ================================
# Time complexity : O(n^2)
# ===================

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         answer = []
#         # Outer Loop (Iterates through sorted nums list)
#         for i in range(len(nums)-2):
#             # Skips duplicate numbers
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             # Initialize two pointers (left(l) and right(r))
#             l = i + 1
#             r = len(nums) - 1
#             # Inner Loop (Finding the triplets)
#             while l < r :
#                 # Counts total
#                 total = nums[i] + nums[l] + nums[r]
#                 # Adjust Pointers based on "total" variable
#                 if total < 0 :
#                     # Increases the total
#                     l += 1
#                 elif total > 0:
#                     # Decreases the total
#                     r -= 1
#                 # Triplet found, because "total" is 0
#                 else :
#                     # Created variable "triplet" for number storage
#                     triplet = [nums[i], nums[l], nums[r]]
#                     # "triplet" is apended to "answer" list
#                     answer.append(triplet)
#                     # Skips Duplicates in the Two_Pointer Search
#                     while l < r and nums[l] == triplet[1]:
#                         l += 1
#                     while l < r and nums[r] == triplet[2]:
#                         r -= 1
#         return answer

# solution = Solution()
# result_1 = solution.threeSum([-1,0,1,2,-1,-4])
# result_2 = solution.threeSum([0,1,1])
# result_3 = solution.threeSum([0,0,0])

# print(result_1) # [[-1,-1,2],[-1,0,1]]
# print(result_2) # []
# print(result_3) # [[0,0,0]]

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
# 21. Merge Two Sorted Lists (Linked List) (Unfinished)
# ===================
# Time complexity : 
# ===================

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
        
# solution = Solution()
# result_1 = solution.mergeTwoLists([1,2,4], [1,3,4])
# result_2 = solution.mergeTwoLists([], [])
# result_3 = solution.mergeTwoLists([], [0])

# print(result_1) # True
# print(result_2) # True
# print(result_3) # False

# ================================
# 26. Remove Duplicates from Sorted Array (Array)(Two Pointers)
# ================================
# Time complexity : 
# ================================

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

# ================================
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
# 35. Search Insert Position (Array)(Binary Search)(Unfinished)
# ===================
# Time complexity : 
# ===================

# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         for idx, num in enumerate(nums):
#             if num == target:
#                 return idx
#             if target != num:


# solution = Solution()
# result_1 = solution.searchInsert([1,3,5,6], 5)
# result_2 = solution.searchInsert([1,3,5,6], 2)
# result_3 = solution.searchInsert([1,3,5,6], 7)

# print(result_1) # 2
# print(result_2) # 1
# print(result_3) # 4        

# ================================
# 53. Maximum Subarray (Array)(Divide and Conquer)(Dynamic Programming)
# ================================
# Time complexity : O(n)
# ================================

# from numpy import inf 
# (importing "numpy" also works, but it's slower)

# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         curr_max = 0
#         overall_max = float('-inf')
#         for num in nums:
#             curr_max = max(curr_max + num, num)
#             overall_max = max(overall_max, curr_max)
#         return overall_max

# solution = Solution()
# result_1 = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# result_2 = solution.maxSubArray([1])
# result_3 = solution.maxSubArray([5,4,-1,7,8])

# print(result_1) # 6
# print(result_2) # 1
# print(result_3) # 23

# ================================
# 66. Plus One (Could_be_Improved) 
# ================================
# Array
# Math
# ================================
# Time complexity : 
# ================================

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

# ================================
# 73. Set Matrix Zeroes (Documentation can be improved)
# ================================
# Array
# Hash_Table
# Matrix
# ================================
# Time complexity : O(m*n)
# ================================

# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         first_row = False
#         first_col = False
#         rows, cols = len(matrix), len(matrix[0])

#         # Checks "first_row" and "first_col" for 0
#         first_row = 0 in matrix[0]
#         first_col = any(row[0] == 0 for row in matrix)

#         # Marks Rows and Columns using "first_row" and "first_col"
#         for r in range(1, rows):
#             for c in range(1, cols):
#                 if matrix[r][c] == 0:
#                     matrix[r][0] = 0
#                     matrix[0][c] = 0

#         # Zero Out Rows and Columns Based on Markers
#         for r in range(1, rows):
#             for c in range(1, cols):
#                 if matrix[r][0] == 0 or matrix[0][c] == 0:
#                     matrix[r][c] = 0

#         # Zero Out the First Row
#         if first_row:
#             matrix[0] = [0] * cols

#         # Zero Out the First Collumn
#         if first_col:
#             for row in matrix:
#                 row[0] = 0

#         print(matrix)
    
# solution = Solution()
# result_1 = solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
# result_2 = solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

# print(result_1) # [[1,0,1],[0,0,0],[1,0,1]]
# print(result_2) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

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

# ================================
# 169. Majority Element (Array)(Hash_Table)(Divide_and_Conquer)(Sorting)(Could_be_improved)
# ================================
# Time complexity : 
# ================================

# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         element_count = {}
#         for num in nums:
#             if num not in element_count:
#                 element_count[num] = 1
#             else:
#                 element_count[num] += 1
#         return max(element_count, key=element_count.get)

# solution = Solution()
# result_1 = solution.majorityElement([3,2,3])
# result_2 = solution.majorityElement([2,2,1,1,1,2,2])

# print(result_1) # 3
# print(result_2) # 2

# ================================
# 189. Rotate Array (Array)(Math)(Two_Pointers)(Could_be_improved)
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         if k != 0:
#             nums[:k], nums[k:] = nums[-k:], nums[:-k]
#         return nums

# solution = Solution()
# result_1 = solution.rotate([1,2,3,4,5,6,7], 3)
# result_2 = solution.rotate([-1,-100,3,99], 2)

# print(result_1) # [5, 6, 7, 1, 2, 3, 4]
# print(result_2) # [3, 99, -1, -100]

# ================================
# 217. Contains Duplicate (Array)(Hash_Table)(Sorting)
# ================================
# Time complexity : O(N)
# ================================

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         num_set = set()
#         for i in nums:
#             if i in num_set:
#                 return True
#             else:
#                 num_set.add(i)
#         return False

# solution = Solution()
# result_1 = solution.containsDuplicate([1,2,3,1])
# result_2 = solution.containsDuplicate([1,2,3,4])
# result_3 = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

# print(result_1) # True
# print(result_2) # False
# print(result_3) # True

# ================================
# 283. Move Zeroes (Could_be_Improved)
# ================================
# Array
# Two_Pointers
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         left = 0

#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
#         return nums 


# solution = Solution()
# result_1 = solution.moveZeroes([0,1,0,3,12])
# result_2 = solution.moveZeroes([0])

# print(result_1) # [1,3,12,0,0]
# print(result_2) # [0]

# ================================
# 350. Intersection of Two Arrays II (Could_be_Improved) 
# ================================
# Array
# Hash_Table
# Two_Pointers
# Binary_Search
# Sorting
# ================================
# Time complexity : 
# ================================

# from collections import Counter

# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         return list((Counter(nums1)&Counter(nums2)).elements())

# solution = Solution()
# result_1 = solution.intersect([1,2,2,1], [2,2])
# result_2 = solution.intersect([4,9,5], [9,4,9,8,4])

# print(result_1) # [2,2]
# print(result_2) # [4,9]

# ================================
# 448. Find All Numbers Disappeared in an Array 
# ================================
# Array
# Hash_Table
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         # Create a hash map to track the presence of numbers
#         num_map = {}

#         # Mark the numbers that are present in the array
#         for num in nums:
#             num_map[num] = True

#         # Identify the numbers that are missing
#         result = []
#         for i in range(1, len(nums) + 1):
#             if i not in num_map:
#                 result.append(i)
#         return result

# solution = Solution()
# result_1 = solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
# result_2 = solution.findDisappearedNumbers([1,1])

# print(result_1) # [5,6]
# print(result_2) # [2]

# ================================
# 485. Max Consecutive Ones
# ================================
# Array
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # "result" tracks current number of consecutive 1's
#         # "max_num" tracks maximum number of consecutive 1's
#         max_num = result = 0
#         for num in nums:
#             if num == 1:
#                 result += 1
#                 max_num = max(max_num, result)
#             else:
#                 result = 0
#         return max_num

# solution = Solution()
# result_1 = solution.findMaxConsecutiveOnes([1,1,0,1,1,1])
# result_2 = solution.findMaxConsecutiveOnes([1,0,1,1,0,1])

# print(result_1) # 3
# print(result_2) # 2

# ================================
# 941. Valid Mountain Array
# ================================
# Array
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def validMountainArray(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """
#         n = len(arr)
#         # Check if Array Length is Less than 3
#         if n < 3:
#             return False
#         # Pointer (Peak)
#         i = 0
#         # Ascend to the Peak
#         while i + 1 < n and arr[i] < arr[i + 1]:
#             i += 1
#         # Check if Peak is valid
#         if i == 0 or i == n - 1:
#             return False
#         # Descend from the Peak
#         while i + 1 < n and arr[i] > arr[i + 1]:
#             i += 1

#         return i == n - 1

# solution = Solution()
# result_1 = solution.validMountainArray([2,1])
# result_2 = solution.validMountainArray([3,5,5])
# result_3 = solution.validMountainArray([0,3,2,1])

# print(result_1) # False
# print(result_2) # False
# print(result_3) # True

# ================================
# 1051. Height Checker
# ================================
# Array
# Sorting
# Counting_Sort
# ================================
# Time complexity : O(n log n)
# ================================

# class Solution(object):
#     def heightChecker(self, heights):
#         """
#         :type heights: List[int]
#         :rtype: int
#         """
#         result = 0
#         sorted_heights = sorted(heights)
#         for idx, _ in enumerate(heights):
#             if heights[idx] != sorted_heights[idx]:
#                 result += 1
#         return result

# solution = Solution()
# result_1 = solution.heightChecker([1,1,4,2,1,3])
# result_2 = solution.heightChecker([5,1,2,3,4])
# result_3 = solution.heightChecker([1,2,3,4,5])

# print(result_1) # 3
# print(result_2) # 5
# print(result_3) # 0

# ================================