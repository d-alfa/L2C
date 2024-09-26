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

# ================================
# 35. Search Insert Position (Need_Documentation)
# ================================
# Array
# Binary_Search
# ================================
# Time complexity : O(log n)
# ================================

# class Solution(object):
# 	def searchInsert(self, nums, target):
# 		"""
# 		:type nums: List[int]
# 		:type target: int
# 		:rtype: int
# 		"""
# 		left = 0
# 		right = len(nums) - 1
# 		while left <= right:
# 			mid = (left + right) // 2
# 			if nums[mid] < target:
# 				left = mid + 1
# 			elif nums[mid] > target:
# 				right = mid - 1
# 			else:
# 				return mid
# 		return left

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
#         # Tracks if "first_row" contains 0's
#         first_row = False
#         # Tracks if "first_col" contains 0's
#         first_col = False
#         # "rows" and "cols" store the number of rows and collumns in the matrix
#         rows, cols = len(matrix), len(matrix[0])

#         # Checks "first_row" and "first_col" for 0's
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

# ================================
# 88. Merge Sorted Array (Need_Documentation)
# ================================
# Array
# Two_Pointers
# Sorting
# ================================
# Time complexity : O(m + n)
# ================================

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         m_idx = m - 1
#         n_idx = n - 1
#         right = m + n - 1

#         while n_idx >= 0:
#             if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
#                 nums1[right] = nums1[m_idx]
#                 m_idx -= 1
#             else:
#                 nums1[right] = nums2[n_idx]
#                 n_idx -= 1
            
#             right -= 1

# solution = Solution()
# result_1 = solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# result_2 = solution.merge([1], 1, [], 0)
# result_3 = solution.merge([0], 0, [1], 1)

# print(result_1) # [1,2,2,3,5,6]
# print(result_2) # [1]
# print(result_3) # [1]

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
# 125. Valid Palindrome (Could be Improved)
# ================================
# Two_Pointers
# String
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         new_string = "".join(letter for letter in s if letter.isalnum()).lower()
#         if new_string == new_string[::-1]:
#             return True
#         return False


# solution = Solution()
# result_1 = solution.isPalindrome("A man, a plan, a canal: Panama")
# result_2 = solution.isPalindrome("race a car")
# result_3 = solution.isPalindrome(" ")

# print(result_1) # True
# print(result_2) # False
# print(result_3) # True

# ================================
# 136. Single Number (Need_Documentation)
# ================================
# Array
# Bit_manipulation
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         answer = 0
#         for num in nums:
            # XOR operator "^"
            # Compares two binary numbers bit by bit
            # returns 1 if bits are different, and 0 if the bits are the same
#             answer ^= num
#         return answer
        
# solution = Solution()
# result_1 = solution.singleNumber([2,2,1])
# result_2 = solution.singleNumber([4,1,2,1,2])
# result_3 = solution.singleNumber([1])

# print(result_1) # 1
# print(result_2) # 4
# print(result_3) # 1

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
# 242. Valid Anagram (Could be Improved)
# ================================
# Hash_Table
# String
# Sorting
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s) != len(t):
#             return False

#         sMap = {}
#         tMap = {}

#         for l in s:
#             if l in sMap:
#                 sMap[l] += 1
#             else:
#                 sMap[l] = 1

#         for l in t:
#             if l in tMap:
#                 tMap[l] += 1
#             else:
#                 tMap[l] = 1

#         return sMap == tMap


# solution = Solution()
# result_1 = solution.isAnagram("anagram", "nagaram")
# result_2 = solution.isAnagram("rat", "car")

# print(result_1) # True
# print(result_2) # False

# ================================
# 268. Missing Number (Need_Documentation)
# ================================
# - Array
# - Hash_Table
# - Math
# - Binary_Search
# - Bit_Manipulation
# - Sorting
# ================================

# ======================
# Hash_table (set)
# ======================
# Time complexity : O(n)
# ======================

# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         num_set = set(range(n + 1))

#         for num in nums:
#             num_set.remove(num)

#         return num_set.pop()

# ======================
# Binary_Search
# ======================
# Time complexity : O(n log n)
# ======================

# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()

#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == mid:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return left

# ======================
# Bit_Manipulation
# ======================
# Time complexity : O(n)
# ======================

# class Solution(object):
#     def missingNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         missing = len(nums)

#         for i in range(len(nums)):
#             missing ^= i ^ nums[i]
#         return missing
    
# ======================
# Testing & Debugging
# ======================
    
# if __name__ == "__main__":
#     solution = Solution()
    
#     result_1 = solution.missingNumber([3,0,1])
#     print(result_1) # Expected: 2

#     result_2 = solution.missingNumber([0,1])
#     print(result_2) # Expected: 2

#     result_3 = solution.missingNumber([9,6,4,2,3,5,7,0,1])
#     print(result_3) # Expected: 8

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
# 680. Valid Palindrome II (Documentation can be improved)
# ================================
# Two_Pointers
# String
# Greedy
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         # Initialize pointer "left" (start of string)
#         left = 0
#         # Initialize pointer "right" (end of string)
#         right = len(s)-1
#         # Iterate while two pointers have not crossed each other
#         while left <= right:
#             # Checks if characters at the current pointers are not equal
#             if s[left] != s[right]:
#                 # Mismatch found, two versions of the string are created
#                  # "string_1" is created by removing the character at the "left" pointer
#                 string_1 = s[:left] + s[left + 1:]
#                  # "string_2" is created by removing the character at the "right" pointer
#                 string_2 = s[:right] + s[right + 1:]
#                 # Check if either string is a palindrome 
#                 return string_1 == string_1[::-1] or string_2 == string_2[::-1]
#             # No mismatch found
#              # Pointers move inward towards the center
#             left += 1
#             right -= 1
#         # Return True if no more than one mismatch was found or fixed
#         return True

# solution = Solution()
# result_1 = solution.validPalindrome("aba")
# result_2 = solution.validPalindrome("abca")
# result_3 = solution.validPalindrome("abc")

# print(result_1) # True
# print(result_2) # True
# print(result_3) # False 

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
# 1313. Decompress Run-Lenght Encoded List (Need_Documentation)
# ================================
# Array
# ================================
# Time complexity : 
# ================================

# class Solution(object):
#     def decompressRLElist(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         decomp_list = []

#         for i in range(0, len(nums), 2):
#             for _ in range(nums[i]):
#                 decomp_list.append(nums[i+1])
#         return decomp_list

# solution = Solution()
# result_1 = solution.decompressRLElist([1,2,3,4])
# result_2 = solution.decompressRLElist([1,1,2,3])

# print(result_1) # [2,4,4,4]
# print(result_2) # [1,3,3]

# ================================
# 1431. Kids With the Greatest Number of Candies (Need_Documentation)
# ================================
# Array
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         """
#         :type candies: List[int]
#         :type extraCandies: int
#         :rtype: List[bool]
#         """
#         list_bool = []
#         for candie in candies:
#             if (candie + extraCandies) >= max(candies):
#                 list_bool.append(True)
#             else:
#                 list_bool.append(False)
#         return list_bool

# solution = Solution()
# result_1 = solution.kidsWithCandies([2,3,5,1,3], 3)
# result_2 = solution.kidsWithCandies([4,2,1,1,2], 1)
# result_3 = solution.kidsWithCandies([12,1,12], 10)

# print(result_1) # [True, True, True, False, True]
# print(result_2) # [True, False, False, False, False]
# print(result_3) # [True, False, True]

# ================================
# 1470. Shuffle the Array (Need_documentation)
# ================================
# Array
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         k1=nums[:n]
#         k2=nums[n:2*n]
#         k3=[]
#         for i in range(n):
#             k3.append(k1[i])
#             k3.append(k2[i])
#         return k3
        
# solution = Solution()
# result_1 = solution.shuffle([2,5,1,3,4,7], 3)
# result_2 = solution.shuffle([1,2,3,4,4,3,2,1], 4)
# result_3 = solution.shuffle([1,1,2,2], 2)

# print(result_1) # [2,3,5,4,1,7]
# print(result_2) # [1,4,2,3,3,2,4,1]
# print(result_3) # [1,2,1,2]

# ================================
# 1512. Number of Good Pairs (Need_Documentation)
# ================================
# Array
# Hash_Table
# Math
# Counting
# ================================
# Time complexity : O(n^2) (Could_be_Improved)
# ================================

# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count

# solution = Solution()
# result_1 = solution.numIdenticalPairs([1,2,3,1,1,3])
# result_2 = solution.numIdenticalPairs([1,1,1,1])
# result_3 = solution.numIdenticalPairs([1,2,3])

# print(result_1) # 4
# print(result_2) # 6
# print(result_3) # 0

# ================================
# 1637. Widest Vertical Area Two Points Containing No Points (Need_Documentation)
# ================================
# Array
# Sorting
# ================================
# Time complexity : O (n log n) (Could_be_improved)
# ================================

# class Solution(object):
#     def maxWidthOfVerticalArea(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         points.sort(key=lambda point: point[0])
#         max_width = 0
#         for i in range(1, len(points)):
#             width = points[i][0] - points[i - 1][0]
#             max_width = max(max_width, width)
#         return max_width

# solution = Solution()
# result_1 = solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])
# result_2 = solution.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])

# print(result_1) # 1
# print(result_2) # 3

# ================================
# 1672. Richest Customer Wealth
# ================================
# Array
# Matrix
# ================================
# Time complexity : O(m*n)
 # More efficient than O(n^2), less efficient than O(n)
# ================================

# class Solution(object):
#     def maximumWealth(self, accounts):
#         """
#         :type accounts: List[List[int]]
#         :rtype: int
#         """
#         # More explicit, clear and easy to follow
#         max_wealth = 0
#         for i in range(len(accounts)):
#             total_wealth = sum(accounts[i])
#             max_wealth = max(max_wealth, total_wealth)
#         return max_wealth
    
        #  More concise, leverages Python's built-in functions
        #  return max(sum(acc) for acc in accounts)

# solution = Solution()
# result_1 = solution.maximumWealth([[1,2,3],[3,2,1]])
# result_2 = solution.maximumWealth([[1,5],[7,3],[3,5]])
# result_3 = solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])

# print(result_1) # 6
# print(result_2) # 10
# print(result_3) # 17

# ================================
# 1684. Count the Number of Consistent Strings
# ================================
# Array
# Hash_Table
# String
# Bit_Manipulation
# Counting
# ================================
# Time complexity : O(N*M)
# ================================

# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         """
#         :type allowed: str
#         :type words: List[str]
#         :rtype: int
#         """
#         # Inconsistent word count
#         count = 0
#         for word in words:
#             for char in word:
#                 # Check if character is not in the allowed string
#                 if char not in allowed:
#                         # Inconsistent word found, increment count by 1
#                         count += 1
#                         # Stops checking further characters in current word
#                          # because we already know that the word is inconsistent
#                         break
#         return len(words) - count

# solution = Solution()
# result_1 = solution.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
# result_2 = solution.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])
# result_3 = solution.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"])

# print(result_1) # 2
# print(result_2) # 7
# print(result_3) # 4

# ================================
# 1897. Redistribute Characters to Make All Strings Equal (Need_Documentation)
# ================================
# Hash_Table
# String
# Counting
# ================================
# Time complexity : O(m*n)
# ================================

# class Solution(object):
#     def makeEqual(self, words):
#         """
#         :type words: List[str]
#         :rtype: bool
#         """
#         char_count = {}
#         for word in words:
#             for char in word:
#                 if char not in char_count:
#                     char_count[char] = 1
#                 else:
#                     char_count[char] += 1
#         for count in char_count.values():
#             if count % len(words) != 0:
#                 return False
#         return True

# solution = Solution()
# result_1 = solution.makeEqual(["abc","aabc","bc"])
# result_2 = solution.makeEqual(["ab","a"])

# print(result_1) # True
# print(result_2) # False

# ================================
# 1913. Maximum Product Difference Between Two Pairs (Need_Documentation)
# ================================
# Array
# Sorting
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def maxProductDifference(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         w, x = 0, 0
#         y, z = float('inf'), float('inf')

#         for n in nums:

#             if n > w:
#                 x = w
#                 w = n
#             elif n > x:
#                 x = n
            
#             if n < y:
#                 z = y
#                 y = n
#             elif n < z:
#                 z = n

#         return (w * x) - (y * z)

# solution = Solution()
# result_1 = solution.maxProductDifference([5,6,2,7,4])
# result_2 = solution.maxProductDifference([4,2,5,9,7,4,8])

# print(result_1) # 34
# print(result_2) # 64

# ================================
# 1920. Build Array from Permutation
# ================================
# Array
# Simulation
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def buildArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         ans = [0] * len(nums)
#         for i in range(len(nums)):
#             ans[i] = nums[nums[i]]
#         return ans

# solution = Solution()
# result_1 = solution.buildArray([0,2,1,5,3,4])
# result_2 = solution.buildArray([5,0,1,2,3,4])

# print(result_1) # [0,1,2,4,5,3]
# print(result_2) # [4,5,0,1,2,3]

# ================================
# 1929. Concatenation of Array
# ================================
# Array
# Simulation
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def getConcatenation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         return nums + nums

# solution = Solution()
# result_1 = solution.getConcatenation([1,2,1])
# result_2 = solution.getConcatenation([1,3,2,1])

# print(result_1) # [1,2,1,1,2,1]
# print(result_2) # [1,3,2,1,1,3,2,1]

# ================================
# 2011. Final Value of Variable After Performing Operations
# ================================
# Array
# String
# Simulation
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def finalValueAfterOperations(self, operations):
#         """
#         :type operations: List[str]
#         :rtype: int
#         """
#         X = 0
#         for o in range(len(operations)):
#             if operations[o] == "++X" or operations[o] == "X++":
#                 X += 1
#             else:
#                 X -= 1
#         return X

# solution = Solution()
# result_1 = solution.finalValueAfterOperations(["--X","X++","X++"])
# result_2 = solution.finalValueAfterOperations(["++X","++X","X++"])
# result_3 = solution.finalValueAfterOperations(["X++","++X","--X","X--"])

# print(result_1) # 1
# print(result_2) # 3
# print(result_3) # 0

# ================================
# 2037. Minimum Number of Moves to Seat Everyone
# ================================
# Array
# Greedy
# Sorting
# Counting_Sort
# ================================
# Time complexity : O(n log n)
# ================================

# class Solution(object):
#     def minMovesToSeat(self, seats, students):
#         """
#         :type seats: List[int]
#         :type students: List[int]
#         :rtype: int
#         """
#         seats.sort()
#         students.sort()
#         count = 0
#         for i in range(len(seats)):
#             count += abs(seats[i] - students[i])
#         return count
                
# solution = Solution()
# result_1 = solution.minMovesToSeat([3,1,5], [2,7,4])
# result_2 = solution.minMovesToSeat([4,1,5,9], [1,3,2,6])
# result_3 = solution.minMovesToSeat([2,2,6,6], [1,3,2,6])

# print(result_1) # 4
# print(result_2) # 7
# print(result_3) # 4

# ================================
# 2373. Largest Local Values in a Matrix
# ================================
# Array
# Matrix
# ================================
# Time complexity : O(n^2)
# ================================

# class Solution(object):
#     def largestLocal(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         # Number of rows in the "grid"
#         n = len(grid)
#         # New result grid of size (n-2) x (n-2)
#         res = [[0] * (n-2) for _ in range(n-2)]
#         # Iterate over possible 3x3 subgrids
#         for i in range(n - 2):
#             for j in range(n - 2):
#                 # Initialize max_val variable
#                 max_val = float("-inf")
#                 # Iterate over the current 3x3 subgrid
#                 for ii in range(i, i + 3):
#                     for jj in range(j, j + 3):
#                         # Update max_val with maximum value
#                         max_val = max(max_val, grid[ii][jj])
#                 # Store the maximum value in the result grid
#                 res[i][j] = max_val
#         return res

# solution = Solution()
# result_1 = solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
# result_2 = solution.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])

# print(result_1) # [[9,9],[8,6]]
# print(result_2) # [[2,2,2],[2,2,2],[2,2,2]]

# ================================
# 2706. Buy Two Chocolates
# ================================
# Array
# Greedy
# Sorting
# ================================
# Time complexity : O(n log n)
# ================================

# class Solution(object):
#     def buyChoco(self, prices, money):
#         """
#         :type prices: List[int]
#         :type money: int
#         :rtype: int
#         """
#         prices.sort()
#         balance = money - (prices[0] + prices[1])
#         if balance >= 0:
#             return balance
#         else:
#             return money

# solution = Solution()
# result_1 = solution.buyChoco([1,2,2], 3)
# result_2 = solution.buyChoco([3,2,3], 3)

# print(result_1) # 0
# print(result_2) # 3

# ================================
# 2798. Number of Employees Who Met the Target
# ================================
# Array
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def numberOfEmployeesWhoMetTarget(self, hours, target):
#         """
#         :type hours: List[int]
#         :type target: int
#         :rtype: int
#         """
#         count = 0
#         for hour in hours:
#             if hour >= target:
#                 count += 1
#         return count

# solution = Solution()
# result_1 = solution.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2)
# result_2 = solution.numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6)

# print(result_1) # 3
# print(result_2) # 0

# ================================
# 2942. Find Words Containing Character
# ================================
# Array
# String
# ================================
# Time complexity : O(n * m)
# ================================

# class Solution(object):
#     def findWordsContaining(self, words, x):
#         """
#         :type words: List[str]
#         :type x: str
#         :rtype: List[int]
#         """
#         ans = []
#         for i, word in enumerate(words):
#             if x in word:
#                 ans.append(i)
#         return ans

# solution = Solution()
# result_1 = solution.findWordsContaining(["leet","code"], "e")
# result_2 = solution.findWordsContaining(["abc","bcd","aaaa","cbc"], "a")
# result_3 = solution.findWordsContaining(["abc","bcd","aaaa","cbc"], "z")

# print(result_1) # [0,1]
# print(result_2) # [0,2]
# print(result_3) # []

# ================================
# 3110. Score of a String (Need_Documentation)
# ================================
# String
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def scoreOfString(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         score = 0
#         for i in range(len(s) - 1):
#             score += abs(ord(s[i]) - ord(s[i + 1]))
#         return score

# solution = Solution()
# result_1 = solution.scoreOfString("hello")
# result_2 = solution.scoreOfString("zaz")

# print(result_1) # 13
# print(result_2) # 50

# ================================
# 3190. Find Minimum Operations to Make Elements Divisible by Three
# ================================
# Array
# Math
# ================================
# Time complexity : O(n)
# ================================

# class Solution(object):
#     def minimumOperations(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         count = 0
#         for num in nums:
#             # If remainder is 1, subtraction is required to make number divisible by 3
#             # If remainder is 2, addition is required to make number divisible by 3
#             if num % 3 != 0:
#                 count += 1
#         return count

# solution = Solution()
# result_1 = solution.minimumOperations([1,2,3,4])
# result_2 = solution.minimumOperations([3,6,9])

# print(result_1) # 3
# print(result_2) # 0

# ================================