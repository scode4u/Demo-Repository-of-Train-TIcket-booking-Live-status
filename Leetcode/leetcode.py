# number =  '2446'
# # number2 = list(number)
# count = 0
# for i in range((number)):
#     x = number[i]
#     if x % number == 0:
#         count += 1
# print(count)

# alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
# # print(alphabet_dict)
# value = input()
# k = int(input())
# add = 0
# if k <= 1:
#     for i in value:
#         if i in alphabet_dict:
#             add += alphabet_dict[i]
#     print(add)


# class Solution(object):
#     def getLucky(self, s, k):
#         num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
#         for _ in range(k):
#             num_str = str(sum(int(digit) for digit in num_str))
#         return int(num_str)

# s = "leetcode"
# k = 2
# solution = Solution()
# print(solution.getLucky(s, k)) 


# s = "Leetcode"
# k = 2
# for i in s:
#     num_str = (''.join(str(ord(i)-ord('a')+1)))


# class Solution(object):
#     def getLucky(self, s, k):
#         for i in s:
#             return "".join(str(ord(i)-96))
# s = "iiii"
# k = 1
# solution = Solution()
# print(solution.getLucky(s, k))



