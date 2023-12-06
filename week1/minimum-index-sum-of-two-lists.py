class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result=[]
        minim_len=float("inf")
        for i in list1:
            if i in list2:
                len=list1.index(i)+list2.index(i)
                
                if len==minim_len:
                    result.append(i)
                elif len<minim_len:
                    result=[i]
                    minim_len=len
        return result

        