class Solution(object):
    def romanToInt(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


        # How I tried it instead, but I had the same idea except we used to use swap for differnt scenarios which can result in errors being formulated. PLease use
        # map = {}
        # map['I'] = 1
        # map['V'] = 5 
        # map['X'] = 10
        # map['L'] = 50
        # map['C'] = 100
        # map['D'] = 500
        # map['M'] = 1000
        #         sum  = sum + map[char]
        # return sum