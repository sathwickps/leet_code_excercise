class Solution:
    def findIndices(self, v, index, value):
        n = len(v)
        ans = [-1, -1]
        for i in range(n):
            for j in range(i, n):
                if abs(i - j) >= index and abs(v[i] - v[j]) >= value:
                    ans[0] = i
                    ans[1] = j
                    break
        return ans

if __name__ == "__main__":
    solution = Solution()
    v = [1, 2, 3, 4, 5]
    index = 2
    val = 2
    result = solution.findIndices(v, index, val)
    print(result)