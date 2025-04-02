from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+=str(len(s))+"#"+s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_strings=[]
        i=0

        while i<len(s):
            j=i
            while s[j] !="#":
                j+=1
                print(j,s[j+1])
                
            
            length = int(s[i:j])
            
            decoded_strings.append(s[j+1:j+1+length])

            i = j + 1 + length

        return decoded_strings

sol = Solution()

print(sol.encode(["##", "#hello#", "abc#def"]))
print(sol.decode(sol.encode(["##", "#hello#", "abc#def"])))
