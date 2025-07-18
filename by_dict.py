class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        adi=[]
        dic={}
        for i in range (len(names)):
            dic[heights[i]]=names[i]
        for i in sorted (dic.keys(),reverse=True):
            adi.append(dic[i])
        return adi
