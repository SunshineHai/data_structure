
# 定义异常：栈下溢
class StackUnderflow(ValueError):
    pass

class Sstack:
    """:arg
        定义栈，使用列表实现
    """
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []        # 加下划线，代表该成员变量为私有变量

    # 返回栈顶元素
    def top(self):
        if self.is_empty():
            raise StackUnderflow("in Sstack.top()")   # 使用 raise 抛出自定义异常
        else:
            return self._elems[-1]    # 返回栈顶，即最后一个元素

    def push(self, element):
        self._elems.append(element)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow("in SStack.pop()")
        else:
            return self._elems.pop()    # 列表中的pop()，移除列表中最后一个元素，并返回移除的元素

# 1.栈与递归
def fact(n):
    """:arg
        递归：简单理解的话，函数自己调用自己 就成为递归。
        递归定义时，递归的部分必须比原来的整体简单，并且递归要有 递归定义的出口，递归定义的出口 是 不能递归的，否则就会无限递归下去。
        我们知道 阶乘的数学定义如下:

        fact(n) = 1,                 n = 0
                = n X fact(n-1),     n > 0
        很明显 阶乘的定义就是 递归形式的。

        求 5的阶乘？
        步骤：
        1.求 fact(5), 我们需要求fact(4)
        2.在计算 fact(5) 时， 这个函数的参数是 n = 5, 然后递归调用 fact(4), 函数的参数 n=4
        3.递归调用 fact(3) 时，函数参数为3
        4.递归调用 fact(2) 时，函数参数为2
        5.递归调用 fact(1) 时，函数参数为1
        6.此时 递归定义的出口为 fact(0) == 1; 此时函数返回，和递归调用顺序相反
        7.函数返回时，先计算 1*fact(0) = 1
        8. 再计算 2 * 1*fact(0) = 2
        9.再计算 3 * 2*1*fact(0) = 6
        10.   4 * 3*2*1*fact(0) = 24
        11.   5 * 4*3*2*1*fact(0) = 120
        注意：这里函数返回时使用的 参数 和 函数调用时刚好相反，是后进先出的特点，在函数调用执行时，实际上有一个 程序运行栈，我们可以进行模拟，
        方便理解递归的执行过程。
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def non_rec_fact(n):
    """:arg
        这里定义 的 栈，保存了 运行时栈 的部分信息
    """
    st = Sstack()      # 这里用列表模拟一下栈
    res = 1            # 存放递归结果
    while n > 0:
        st.push(n)
        n -= 1
    while not st.is_empty():
        res *= st.pop()
    return res


# 2.栈的应用：背包问题
""":arg
    栈的应用：简单的背包问题
    问题描述：
        一个背包可以放重量为 weight 的物品，现有 n 件物品， S = {S0, S1, ..., Sn-1}, 物品的重量分别为
        w0, w1, ..., wn-1, 能否取出若干件物品，使得重量之和正好等于 weight。
    分析：
        1.如果不选最后一件物品，则 knap(weight, n-1)的解也就是 knap(weight, n) 的解，两者解一样
        2.如果选择最后一件物品，那么如果 knap(weight-wn-1, n-1) 有解，其解加上最后一件物品就是 knap(weight, n) 的解，
        即前者有解，后者也有解。

    eg: 一个背包可以放 weight = 10kg 的物品， 一共有 8 件物品， 重量分别为：[1, 3, 1, 0.5, 4, 2, 1, 5] kg, 请问是否可以
    找到 若干件 物品 的重量 等于 weight？
    第 [1, 3, 6, 7, 8] 个物品的重量和 为 1+1+2+1+5 = 10 满足背包 weight 的重量

    一次递归使用 运行时栈 比较容易转化 为非递归函数
     使用2次以上递归就比较麻烦，难于理解。

     递归在使用时，相对容易写出递归，但是递归的执行比较难理解。
"""
def knap_rec(weight, wlist, n):
    """:arg
        weight : 背包容纳的重量
        wlist :  各个物品的重量
        n     :  物品的个数
    """
    if weight == 0:                                 # 刚好 weight - 若干件的重量 == 0; 刚好放下
        return True
    if weight < 0 or (weight > 0 and n < 1):        # 剩余重量小于零说明 若干件的重量 > weight(所有物品的重量和<weight)，依然没有找到
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):   # 第n-1件放到背包里
        print("Item " + str(n) + ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):                # 第n-1件不合适，不放入背包
        return True
    else:
        return False
    pass


if __name__ == '__main__':
    weight = 10
    wlist, n = [1, 3, 1, 0.5, 4, 2, 1, 5], 8
    res = knap_rec(weight, wlist, n)
    print(res)

    print("---------------------------------")
    num = 5
    res = fact(num)
    print("{0}!={1}".format(num, res))
    
    print(non_rec_fact(5))
