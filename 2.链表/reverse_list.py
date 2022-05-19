
class Solution:

    def get_factorial(self, num):

        if num == 0:
            return 1
        else:
            return num * self.get_factorial(num-1)


    ''':arg
        斐波那契数列：F(n) = F(n-1)+F(n-2) n >= 2    1, 1, 2, 3, 5, 8, 13, 21, 34......
        n 是 要输入的位数
    '''
    def fibonacci(self, n):

        if n < 3:
            return 1  # f(1) = 1, f(2) = 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    def change(self, n):
        if n > 9:
            self.change(n // 10)
        print(n % 10)

if __name__ == '__main__':

    s = Solution()
    list1 = []
    for i in range(8):
        list1.append(s.fibonacci(i+1))
    print(list1)

    res = s.change(1234567) # 1 2 3 4 5 6 7



