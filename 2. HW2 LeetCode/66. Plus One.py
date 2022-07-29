#題意:給定一個非0且不為負數並把數字分成一位一位的list，把最後一位加1後回傳結果。
#想法:一般情況下直接加，如果遇到9，就抹0，然後讓上一位加1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):   #從最後一位開始
            if digits[i] == 9:                   #如果遇到9
                digits[i] = 0                    #就強制變成0 
            else:
                digits[i] += 1                   #如果是非9情況正常加1
                return digits                    #回傳list
        return [1] + digits                      #回傳list最前面加1