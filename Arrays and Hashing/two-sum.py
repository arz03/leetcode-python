# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         i=0
#         j=0
#         if i <= len(nums):
#             if j <= len(nums):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#                 else:
#                     j+=1
#             else:
#                 j=0
#                 i+=1
#         else:
#             return False
        
# nums = [2,7,11,15]
# target = 9
# print(Solution().twoSum(nums,target))
