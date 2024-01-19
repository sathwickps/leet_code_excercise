class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        res = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(s[i:j])) == 1:
                    if s[i:j] not in h:
                        h[s[i:j]] = 1
                    else:
                        h[s[i:j]] += 1
                    if h[s[i:j]] >= 3:
                        res = max(res, len(s[i:j]))
        return res