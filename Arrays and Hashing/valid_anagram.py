# https://leetcode.com/problems/valid-anagram/


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        k=sorted(s)
        l=sorted(t)
        if k==l:
            return True
        else:
            return False



# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s)==len(t):
#             list1=[]
#             list2=[]
#             for i in s:
#                 if i in list1:
#                     pass
#                 else:
#                     list1.append(i)
#                     list1.sort
#             for p in t:
#                 if p in list2:
#                     pass
#                 else:
#                     list2.append(p)
#                     list2.sort

#             if list1==list2:
#                 return True
#             else:
#                 return False
#         else:
#             return False



        # count1=0
        # count2=0
        # positive=0
        # if len(s)==len(t):
        #     for i in s:
        #         for y in t:
        #             if y==i:
        #                 positive+=1
        #             else:
        #                 pass
        #     if len(s)==1:
        #         if s==t:
        #             return True
        #     elif len(s)==1:
        #         if s==t:
        #             return True
        #     elif positive==len(s):
        #          return True
        #     else:
        #          return False
        # else:
        #     return False
        


        # if len(s)==len(t):
        #     count = 0
        #     for i in s:

        #         if i in t:
        #              count+=1
        #         else:
        #              continue
        #     if len(s)==1:
        #         if s==t:
        #             return True
        #     elif len(s)==1:
        #         if s==t:
        #             return True
        #     elif count>=len(s):
        #          return True
        #     else:
        #          return False
        # else:
        #     return False
