#題意:把給定32位的整數做反轉。
#想法:直接變成字串，再用字串逆續的功能。
class Solution:
    def reverse(self, x: int) -> int:
        
        strx = str(x)                       #先轉成字串
        if x < 0:                          #判斷x是否小於0
            x = int('-' + strx[1:][::-1])   #如果是的話就把負號提出來再把從位置1到最後的逆續後，再回去負號
        else:                              #如果大於0
            x = int(strx[::-1])             #直接逆續
        if x < -2**31 or x > 2**31 - 1:    #判斷x是否有在題目給定的範圍內
            return 0                       #超出直接回傳0
        else:
            return x                       #沒超出就回傳x