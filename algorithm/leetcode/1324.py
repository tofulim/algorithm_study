class Solution:
    def printVertically(self, s: str) -> List[str]:
        input_word=s.split()
        max_len=len(max(input_word,key=len))
        return [''.join([i[j] if len(i)>j else ' ' for i in input_word]).rstrip() for j in range(max_len)]
        