#題目:把羅馬數字轉成整數。
#想法:用字典先儲存所有羅馬字母所對應的數值，再重裡面查找就可以。
class Solution:
    def romanToInt(self, s: str) -> int:
        
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,} #建立一個字典
        result = 0       #設定一個結果，預設為0
        
        for i in range(len(s)):  #在字串長度範圍內
            if i > 0 and Roman[s[i]] > Roman[s[i - 1]]:  #判斷第一位以後，是否有前一位比後一位小的情況
                result = result + (Roman[s[i]] - 2*Roman[s[i-1]])   #如果有就相減
                # M+C+M-C = M+M,     M+C+M-2C) = M+M-C 
            else:
                result = result + Roman[s[i]]      #如果沒有就繼續相加
        return result