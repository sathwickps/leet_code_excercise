class Solution:
    def canMakeSubsequence(self, y: str, x: str) -> bool:
        ascii = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
        it = iter(y)
        return all(any( (ascii[ord(c)-ord('a')] == ch or ascii[ord(c)-ord('a') + 1] == ch) for c in it) for ch in x)