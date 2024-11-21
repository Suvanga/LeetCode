class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        reverse = a[::-1]
        if reverse == str(x):
            return True
        else:
            return False
       