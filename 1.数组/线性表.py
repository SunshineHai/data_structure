
# 定义结点
class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

# 头结点定义为空(头结点指向第一个元素)
class single_linked_list:

    def __init__(self):
        self._head = None   # 下划线开头，表明该成员变量是私有的
    # 判断是否为空
    def is_empty(self):
        return self._head is None

    # 开头插入
    def prepend(self, data):
        self._head = Node(data, self._head)

    # 移除首元素,并返回该结点的data
    def prepop(self):
        if self.head is None:
            raise LinkedListUnderflow("in prepop")
        e = self._head.data
        self._head = self._head.next
        return e

    # 移除尾部元素，并返回该结点的值
    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        temp = self._head
        # 注意 temp 和 temp.next 的区别
        while temp.next is not None:
            temp = temp.next
        e = temp.data
        temp.next = None
        return e
#       该结点会自动被回收，如果是C语言需要手动free，释放节点的内存

    # 尾部添加
    def append(self, data):
        if self._head is None:
            self._head = Node(data)
            return
        # 遍历查找尾部结点
        temp = self._head
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)
        return self._head

    ''':找到满足给定条件的表元素, pred 是给定条件的函数
       :只能找到第一个满足条件时的元素，pred 可以使用 lambda 表达式
    '''
    def find(self, pred):
        temp = self._head
        while temp is not None:
            if pred(temp.data):
                return temp.data
            temp = temp.next
        return
    # 找到满足 pred 的所有 结点值
    def filter(self, pred):
        temp = self._head
        while temp is not None:
            if pred(temp.data):
                yield temp.data
            temp = temp.next
        return

    # 传统遍历
    def print_all(self, head):
        temp = head
        while temp is not None:
            print(temp.data, end='\t')
            temp = temp.next
        print()
        pass

    """:arg传统的遍历结点的所有值
        这里使用谓词函数，调用的时候传入print函数即可
        使用 C语言遍历时，可以直接把printf()函数写到函数里面
    """
    def for_each(self, proc):
        temp = self._head
        while temp is not None:
            proc(temp.data, end='\t')
            temp = temp.next
        return

    ''':遍历所有结点的data值：使用生成器函数定义迭代器
    '''
    def elements(self):
        temp = self._head
        while temp is not None:
            yield temp.data       # 使用 yield  定义迭代器
            temp = temp.next
        return

    '''
        递归 反转链表
    '''
    def reverse_list(self, head):

        if head is None or head.next is None:    # 递归结束条件
            return head
        else:
            ans = self.reverse_list(head.next)   # 递归下一个结点 到 倒数第二个结点

            head.next.next = head                # 最后一个结点指向倒数第二个结点
            head.next = None                     # 最后一结点的指针域赋值为空
        return ans






if __name__ == '__main__':
    mlist = single_linked_list()
    for i in range(10):
        head = mlist.prepend(i)
    for i in range(11, 20):
        head = mlist.append(i)
#    遍历输出所有元素
    for x in mlist.elements():
        print(x, end='\t')
    print()
    
    res = mlist.find(lambda x: x>15)
    print(res)

    for x in mlist.filter(lambda x: x>15):
        print(x, end='\t')
    print()

    mlist.for_each(print)
    print()
    mlist.print_all(head)

    print('--------------------')
    mlist1 = single_linked_list()
    for i in range(1, 6):
        head = mlist1.append(i)
    for i in mlist1.elements():
        print(i, end='\t')
    print("head:", head.data)
    head = mlist1.reverse_list(head)
    mlist1.print_all(head)
    print()










