class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path=defaultdict(set)
        for i in paths:
            subp,*cont=i.split()
            for j in cont:
                file_n,con=j.split("(")
                path[con]
                path[con[:-1]].add( f"{subp}/{file_n}")
        return [list(result) for result in path.values() if len(result)>1]


        
        