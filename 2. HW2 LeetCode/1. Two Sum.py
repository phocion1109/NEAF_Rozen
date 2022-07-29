#題意:給定一個整數list，找到裡面相加等於目標的兩個數字的位置，每個數字只能用一次。
#想法:先依序把數字以及該數字的位置存到字典裡，然後判斷目標減去那個數是否出現在字典裡。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}    #創建一個字典
        for n1 ,n2 in enumerate(nums): #編列list裡的每個數字 
            if target - n2 in dic:#如果目標減去當前的數字已經出現在這個字典裡
                return [dic[target - n2], n1] #如果出現了就回傳位置
            dic[n2] = n1#如果沒出現就把數字加入字典中