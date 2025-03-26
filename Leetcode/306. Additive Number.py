class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        input = list(map(int, num))
        for i in range(len(num)):
            if input[i] + input[i+1] != input[i+2]:
                print(False)
            else:
                print(True)

trying = Solution()
print(trying.isAdditiveNumber('112358'))