
""":arg
栈：是一种常用的数据结构，特点是：先入后出
实现方法：
    1.顺序表
    2.链表
"""

# 顺序表
""":arg
    顺序表的实现：
    列表本身可以看做是用栈实现的，但是 list.pop(index=),形参的索引为空时可以看做出栈，但是list提供可以删除指定索引的元素，
    因此我们使用列表定义严格意义的栈。
        1.把列表 [] 作为私有的成员变量
        2.栈只能操作栈顶元素，我们根据顺序表的特点，把顺序表的尾部作为栈顶，操作式复杂度为O(1) 
    定义如下：
"""
# 定义异常：栈下溢
class StackUnderflow(ValueError):
    pass

class Sstack:

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

""":arg
    由链表实现栈, 根据链表的特性，我们应该把第一个结点作为栈顶元素而不是尾结点
    1.栈顶指向头结点
    2.实现常用操作
    
"""
class Node:
    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_
    pass


class LStack:
    def __init__(self):
        self._top = None       # 初始化时，头结点为空, 私有成员变量

    def is_empty(self):
        return self._top is None

    # 返回栈顶元素
    def top(self):
        if self._top is None:
            raise StackUnderflow("error in Lstack.top()")
        else:
            return self._top.data

    def push(self, element):
        self._top = Node(element, self._top)  # 新节点指向了旧结点


    def pop(self):
        if self.is_empty():
            raise StackUnderflow("error in pop()")
        else:
            e = self._top.data
            self._top = self._top.next_    # 空出来的结点系统会自动释放
            return e

""":栈的应用
    一、串的反转
        利用 “栈” 先入后出的特点，把串进行反转。
    二、检索括号是否匹配
        检查括号正确的配对。如：()、[]、{}
    三、后缀表达式的计算
        中缀表达式：形如 运算对象 + 运算符 +  运算对象 的形式。我们平常书写的表达式就是中缀表达式。
        后缀表达式：形如 运算对象 + 运算对象 + 运算符 的形式。
        前缀表达式：形如 运算符 + 运算对象 + 运算对象
        给出一个后缀表达式计算出该表达式的值。
        eg:后缀表达式： 3 5 - 6 17 4 * + * 3 /          
            值为：-49.333333333333336
    四、中缀表达式   -->   后缀表达式
       eg: 
          中缀：(3 - 5) * (6 + 17 * 4) /3
          后缀：3 5 - 6 17 4 * + * 3 /
        中缀表达式转换成后缀表达式，人根据规则很容易转换，但是计算机是一个一个字符进行遍历的，需要使用中间的缓存保存中间产生的运算符(+ - * / 括号)
        或者 运算对象(要计算的数字，例子中为3等)。
    转换步骤：
            假设中间保存运算符的数据结构为 栈st，得到的后缀表达式保存在 列表exp 中。    
            1.扫描遇到的 运算对象 直接压入后缀表达式exp中；
            2.遇到 运算符对象时，分几种情况处理：
                ① 左括号直接压入栈st中
                ② 右括号弹出运算符完成计算，直到弹出最后的左括号
                ③ +-*/运算符，根据运算符优先级处理，当前运算符 > 后一个运算符 时压入后缀表达式exp中，否则压入st中。
                ④ 遇到左括号，压入运算符栈st中。    
"""

def reverse(line:list):
    stack = Sstack()    # 使用 栈 作为中间变量存储
    for x in line:
        stack.push(x)
    res = []
    while not stack.is_empty():
        res.append(stack.pop())
    return res

def check_parent(text):
    """
        括号配对检查函数，text 是被检查的正文串
        text 文本 括号全部匹配则返回 True， 否则 返回 False ,输出第一个 不匹配的 下标 和 内容
    """
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")" : "(", "]": "[", "}":"{"}       # 表示配对关系的字典

    def parentheses(text):
        """括号生成器，每次调用返回text里的下一个括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i                        # 找到了 与 parens 匹配的字符
            i += 1

    st = Sstack()                                   # 保存括号的栈  : 保存 ([{
    for pr, i in parentheses(text):
        if pr in open_parens:                       # 开括号压进栈
            st.push(pr)
        elif st.pop() != opposite[pr]:              # 不匹配就失败，退出
            print("Unmatching is found at", i, "for", pr)
            return False
        else:
            pass                                    # 这个 else 语句什么也不做

    print("All parentheses are correctly matched")
    return True


class ESStack(Sstack):
    """:arg
        检查栈元素的深度（栈的长度）: ESStack 继承 Sstack类，不改变父类元素、不破坏父类的安全性
    """
    def depth(self):
        return len(self._elems)

def suf_exp_evaluator(exp):
    ''':arg
        后缀表达式的计算：给出一个后缀表达式，求出该表达式的值
        exp ： 是 后缀表达式
    '''
    operators = "+-/*"
    st = ESStack()

    for x in exp:
        # 不为运算符，即是 运算对象， 放入 中间变量 栈st 中
        if x not in operators:
            st.push(float(x))           # 不能转换为 float() 则抛出异常
            continue

        #  处理 运算对象
        if st.depth() < 2:              # 此时 x 为 运算符, 栈元素不够引发异常
            raise SyntaxError("Short of operand(s)")
        a = st.pop()                    # 后一个元素
        b = st.pop()                    # 前一个元素

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':                  # 除数为0可能引发异常
            c = b / a
        else:
            break                       # else 分支不可能出现，为了使代码清晰

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")
    pass


priority = {"(":1, "+":3, "-":3, "*":5, "/":5}      # 定义运算符的优先级
infix_operators = "+-*/()"                          # 把 ‘()’ 看出运算符，但是特殊处理

def trans_infix_suffix(line):
    st = Sstack()           # 存放中间的运算符
    exp = []                # 存放转换后的后缀表达式

    for x in tokens(line):  # tokens 是一个待定义的生成器，返回line中的一个个项。项是浮点数或运算符

        if x not in infix_operators:        # 运算对象直接放到 exp
            exp.append(x)
        elif st.is_empty() or x == '(':     # 左括号 入栈 st
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.top() != '(':      # x 等于 ')' 则把 st 中的 运算符 压入 exp中
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '(' .")
            st.pop()                        # 执行到此处说明 x == '(' ，不进入到exp, 直接从 st 中弹出
        else:                               # 开始处理 算法运算符(+-*/)
            while (not st.is_empty() and priority[st.top()] >= priority[x]):
                exp.append(st.pop())        # 栈st中的栈顶元素的优先级 > 当前元素， 则把该运算符压入到 st
            st.push(x)                      # x 的优先级高， 就把它压入 st 中
        pass

    while not st.is_empty():                # 送出栈里的运算符
        if st.top() == '(':                 # 如果还有 '(' 就是 括号不匹配
            raise SyntaxError("Extra '('. ")
        exp.append(st.pop())

    return exp

def tokens(line : str):
    """
        line : 字符串              eg: line = '(3 - 5) * (6 + 17 * 4) / 3+ 2e-5'
        逐个生成 line 中的一个个项。 项是浮点数或运算符。本函数不能处理一元运算符也不能处理带符号的浮点数。
        line :
            1.表示中缀表达式
            2.表达式各项中可以有任意多个空格
            3.+-*/符号作为运算符，它们与前后向之间可以有或没有空格
            4.非空格且非运算符的一段就是运算对象
            5.出现3E/e-2，e/E后面的 - 号表示负的指数部分； 3e-2 看做是一个运算对象
            6.该函数不检查 运算对象 是否符合 Python 对浮点数格式的要求。
        该函数的缺点：
            1.不能处理负数 eg:-2
            2.不能处理一元运算符
    """
    i, llen = 0, len(line)
    while i < llen:
        while i < llen and line[i].isspace():       # str.isspace() : str 为一个或多个空格则返回 True, 否则返回 False
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:              # 为运算符，则生成迭代式
            yield line[i]
            i += 1
            continue
        pass

        j = i + 1

        # 运算对象(数字)的处理
        while (j < llen and not line[j].isspace() and line[j] not in infix_operators):  # j 不为空格且不为运算符
            # 处理负指数
            if ((line[j] == 'e' or line[j] == 'E') and j+1 < llen and line[j+1] == '-'):
                j = j+1
            j += 1
            pass
        yield line[i:j]                             # 生成运算对象子串
        i = j
        pass
    pass



if __name__ == '__main__':
    s = Sstack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print(s.top())
    s.pop()
    print(s.top())

    print('-------------------------')
#   遍历输出：
    while not s.is_empty():
        print(s.pop())

    print(s.is_empty())
    # print(s.pop())
    s.push(10)
    print(s._elems)

    my_list = [1]
    print(my_list.pop())

    ss = LStack()
    print(ss.is_empty())
    ss.push(10)
    print('res:', ss.top())
    ss.push(20)
    ss.push(30)


    # 变量输出
    while not ss.is_empty():
        print(ss.pop(), end='\t')
    print("\n\n------------------\n")

    line = '(3 - 5) * (6 + 17 * 4) / 3'    #
    print(type(tokens(line=line)))  # <class 'generator'>

    for x in tokens(line):
        print(x, end='\t')          # 输出时以一个 tab 键隔开
        pass

    exp = trans_infix_suffix(line)
    print('\nexp:', exp)
    sum = suf_exp_evaluator(exp)
    print("sum:", sum)

    line = ['I', 'love', 'China', '!']
    res = reverse(line)
    print(res)

    text = "123()[]{}456(]789{"
    check_parent(text)




