from typing import List


class Solution:
    
    def isAnagram (self, stringA: str, stringB: str):
        if len(stringA) != len(stringB):
            return False
        
        countS, countT = {}, {}

        for i in range(len(stringA)):
            countS[stringA[i]] = 1 + countS.get(stringA[i], 0)
            countT[stringB[i]] = 1 + countT.get(stringB[i], 0)

        if countS == countT:
            return True


    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # check array length constraint
        if len(strs) < 1 or len(strs) > 1000:
            return []
        

        anagrams = {} # string -> List[string]

        for i, str in enumerate(strs):
            strs.remove(str)
            print (str)
            print (strs)

            if len(str) > 100: # check string length constraint
                continue

            anagrams[str] = anagrams.get([str], [])

            for j in range(len(strs)):
                if self.isAnagram(str, strs[j]):
                    anagrams[str] = anagrams.get([str]).add(strs[j])
                else:
                    continue
            


