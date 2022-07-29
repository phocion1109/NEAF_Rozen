#題意:判斷給定的整數是否回文
#想法:轉成字串翻轉後是否相等判斷回文
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:                     #判斷x是否小於0
            return False              #是的話直接回傳false
        strx = str(x)                 #轉成字串
        return strx == strx[::-1]     #如果字串逆續後相等，那就是回文