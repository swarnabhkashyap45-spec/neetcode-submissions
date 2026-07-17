class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        characterMap = {}
        for c in s:
            characterMap[c] = characterMap.get(c,0)+1
        for c in t:
            if c not in characterMap or characterMap[c]==0:
                return False
            characterMap[c] = characterMap.get(c)-1
        for key in characterMap:
            if characterMap[key]!=0:
                return False
        return True