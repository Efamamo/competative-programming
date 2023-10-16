import textwrap

def wrap(string, max_width):
    i=0
    j=0
    while j<len(string):
        print(string[j],end="")
        j+=1
        if j%max_width==0:
            print()
    
        
    return ""

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
