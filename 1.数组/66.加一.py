# https://leetcode.cn/problems/plus-one/solution/
class Solution:

    def plusOne(self, digits):
        tail = len(digits) - 1
        carry = 0               # 进位

        while tail >= 0:
            if digits[tail] < 9:
                digits[tail] += 1
                return digits
            else:
                digits[tail] = 0
                carry = 1
            tail -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits

    def plusOne2(self, digits):
        '''
            1.从后往前遍历 digits, 进位 carry 默认为0
            2.如果 该元素值 <9 , 加1 返回
            3.否则(=9)，该元素值赋值为 0， carry = 1
            4.依次遍历，最后如果 carry == 1 , 则开头增加一位 1.
        '''
        carry = 0  # 进位 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i], carry = 0, 1
        if carry == 1:
            return [1] + digits


my_list = [1, 9, 9]
solution = Solution()
res = solution.plusOne(my_list)
print(res)

res = solution.plusOne2([9, 9, 9])
print(res)


