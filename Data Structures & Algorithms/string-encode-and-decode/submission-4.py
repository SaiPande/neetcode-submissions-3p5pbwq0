class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for i in strs:
            encodedstr += str(len(i))+"#"+i
        print(encodedstr)    
        return encodedstr    

    def decode(self, s: str) -> List[str]:
        lst = []
        i=0
        while i in range(len(s)):
            if s[i] in '0123456789':
                num1 = ""
                while  i < len(s) and s[i] in '0123456789':
                    num1 += (s[i])
                    i+=1
                num = int(num1) 
                if  i < len(s) and s[i] == '#':   
                    st = s[i+1:i+num+1]
                    lst.append(st) 
                    i = i + num + 1 
                else:
                    i+=1
            else:
                i+=1           
        return lst        