class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom_c = defaultdict(int)
        for i in cpdomains:
            num,domain=i.split()
            domain=domain.split(".")
            for i in range(len(domain)):
                dom_c[".".join(domain[i:])] += int(num)
        return [f"{value} {key}" for key,value in dom_c.items()]
        
        # for i in range(len(domains)):
        #     domains[i]=domains[i].split(".")
        # for i in range(len(domains)):
        #     for j in range(len(domains[i])):
        #         dom_c[domains[i][j]]+=int(nums[i])
        # result=[]
        # for i in domains:
        #     for j in range(len(i)):
        #         val= str(dom_c[i[j]]) + " "+  ".".join(i[j:])
        #         result.append(val)
        # return list(set(result))