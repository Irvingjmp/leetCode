class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  
            return False  # Si las longitudes son distintas, no pueden ser anagramas

        char_count = {}  # Hashmap para contar caracteres

        # Contar frecuencia de cada letra en `s`
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        print(char_count)
        # Restar frecuencia usando `t`
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False  # Si falta un carácter o hay más de los necesarios en `t`
            char_count[char] -= 1
        
        return True  # Si todas las cuentas son 0, es un anagrama

sol = Solution()
print(sol.isAnagram("nagaram","anagram"))   #True
# print(sol.isAnagram("rat", "car"))          #False