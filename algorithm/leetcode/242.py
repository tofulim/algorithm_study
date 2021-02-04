from collections import Counter
class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return True if sorted(s)==sorted(t) else False
        
    def isAnagram(self, s: str, t: str) -> bool:
        return True if Counter(s)==Counter(t) else False
        