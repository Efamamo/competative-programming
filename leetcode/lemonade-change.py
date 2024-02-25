class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {}
        for i in bills:
            
            if i == 10:
                if 5 not in count:
                    return False
                else:
                    count[5]-=1
                    if count[5] == 0:
                        del count[5]
            elif i == 20:
                if 10 in count:
                    count[10]-=1
                    if count[10] == 0:
                        del count[10]
                    if 5 not in count:
                        return False
                    else:
                        count[5]-=1
                        if count[5] == 0:
                            del count[5]
                else:
                    if 5 not in count:
                        return False
                    elif count[5]<3:
                        return False

                    else:
                        count[5]-=3
                        if count[5] == 0:
                            del count[5]
            count[i] = 1 + count.get(i,0)
        return True


            