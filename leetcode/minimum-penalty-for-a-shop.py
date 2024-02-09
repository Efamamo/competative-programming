class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre = []
        No=Yes=0
        for i in range(len(customers)):
            pre.append([Yes,No])
            if customers[i] == "Y":
                Yes+=1
            else:
                No += 1
        
        pre.append([Yes,No])

        post = []
        No=Yes=0
        for i in range(len(customers)-1,-1,-1):
            post.append([Yes,No])
            if customers[i] == "Y":
                Yes+=1
            else:
                No += 1
        post.append([Yes,No])
        post = post[::-1]

        res = []
        for i in range(len(post)):
            res.append(pre[i][1]+post[i][0])
        
        minim = res.index(min(res))
        return minim




            
        