class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        for word in strs: 
            sortedWord = str(sorted(word))
            if sortedWord in anagrams: 
                anagrams[sortedWord].append(word)
            else: 
                anagrams[sortedWord] = [word]
      
        res = []
        for key, value in anagrams.items(): 
            res.append(value)
        return res