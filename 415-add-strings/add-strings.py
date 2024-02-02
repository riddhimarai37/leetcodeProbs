
# num1 = '123' num2 = '77'
class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
      res = ""
      carry = 0
      pt1 = len(num1) - 1
      pt2 = len(num2) - 1

      while pt1 >= 0 or pt2>= 0 or carry:
          curr_1 = int(num1[pt1]) if pt1 >= 0 else 0
          curr_2 = int(num2[pt2]) if pt2 >= 0 else 0

          curr_sum = curr_1 + curr_2 + carry
          print(curr_sum)
          res += str(curr_sum % 10)

          carry = curr_sum // 10
          pt1 -= 1
          pt2 -= 1

      if carry:
          res += str(carry)

      res = reversed(res)
      return "".join(res)


    # ans = []
    # carry = 0
    # i = len(num1) - 1
    # j = len(num2) - 1

    # while i >= 0 or j >= 0 or carry:
    #   if i >= 0:
    #     carry += int(num1[i])
    #   if j >= 0:
    #     carry += int(num2[j])
    #   ans.append(str(carry % 10))
    #   carry //= 10
    #   i -= 1
    #   j -= 1

    # return ''.join(ans[::-1])


