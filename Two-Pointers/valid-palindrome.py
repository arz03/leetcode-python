# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.lower()
        for i in s:
            if i.isalnum():
                pass
            else:
                s=s.replace(i,"")
        if len(s)==0:
            return True
        else:
            if s==s[::-1]:
                return True
            else:
                return False
