#題意:給定一個包含單字和空格的字串，找出裡面最後一個單字的長度。
#想法:用split來分割單字，在計算倒數最後一個單字的長度即可。
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        word = s.split()       #用空格分割單字
        return len(word[-1])   #回傳最後一個單字的長度