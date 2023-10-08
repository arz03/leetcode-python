#https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        if len(nums)>1:
            for i in range(0,len(nums)):
                if nums[i] == nums[i-1]:
                    return True
        return False

#     Exceeds time limit ==> time complexity
#        p=0
#        limt=len(nums)
#        while p<limt:
#            ch = nums[p]
#            co=0
#            for o in nums:
#                if o == ch:
#                    co=co+1
#                else:
#                    pass
#            if co>=2:
#                return True
#            else:
#                p=p+1
#        return False
