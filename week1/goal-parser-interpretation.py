class Solution:
    def interpret(self, command: str) -> str:
        output=""
        i=0
        while i<len(command)-1:
            if command[i]=="G":
                output+="G"
                i+=1
            elif command[i]=="(":
                if command[i+1]!=")":
                    output+="al"
                    i+=4
                else:
                    output+="o"
                    i+=2
        if command[-1]=="G":
            output+="G"
        return output
        