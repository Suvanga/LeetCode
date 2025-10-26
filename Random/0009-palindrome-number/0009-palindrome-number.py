class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = (str(x)[::-1])
        return reverse==str(x)
        # if reverse == str(x):
        #     return True
        # else:
        #     return False
       
       #So how it works is [::-1] -1 is used to split it in reverse order and it starts at the end since it is not specified  [start:stop:step] since step is -1 so it moves in negative -1 stepa and when we use the start as a different number it starts at a different number for example :
       # 10,20,30 when [1:0:-1] is used we can simply reverse it using  20
       # 10,20,30,40 when [3:1:-1] is used we can simply reverse it using  40,30 as it stops before the stop index which is 1 
