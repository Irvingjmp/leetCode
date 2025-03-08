class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}
        for current_word in strs:
            sorted_key = ''.join(sorted(current_word))
            
            if sorted_key in anagrams:
                anagrams[sorted_key].append(current_word)
            else:
                anagrams[sorted_key] = [current_word]
        return list(anagrams.values()) 