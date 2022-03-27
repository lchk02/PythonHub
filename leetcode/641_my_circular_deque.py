""" 641. 设计循环双端队列
设计实现双端队列。

实现 MyCircularDeque 类:
    MyCircularDeque(int k)：构造函数,双端队列最大为 k 。
    boolean insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true，否则返回 false 。
    boolean insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true，否则返回 false 。
    boolean deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true，否则返回 false 。
    boolean deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true，否则返回 false 。
    int getFront())：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
    int getRear()：获得双端队列的最后一个元素。如果双端队列为空，返回 -1 。
    boolean isEmpty()：若双端队列为空，则返回true，否则返回 false 。
    boolean isFull()：若双端队列满了，则返回true，否则返回 false 。

示例 1：
输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
"getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4

提示：
    1 <= k <= 1000
    0 <= value <= 1000
    insertFront,insertLast,deleteFront,deleteLast,getFront,getRear,isEmpty,isFull
    调用次数不大于2000次

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
"""


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0 for _ in range(k+1)]
        self.size = k + 1
        self.head = 0
        self.tail = 0

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        else:
            self.head = (self.head - 1) % self.size
            self.deque[self.head] = value
            return True

    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        else:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.size
            return True

    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.head = (self.head + 1) % self.size
            return True

    def delete_last(self) -> bool:
        if self.is_empty():
            return False
        else:
            self.tail = (self.tail - 1) % self.size
            return True

    def get_front(self) -> int:
        return -1 if self.is_empty() else self.deque[self.head]

    def get_rear(self) -> int:
        return -1 if self.is_empty() else self.deque[self.tail-1]

    def is_empty(self) -> bool:
        return self.head == self.tail

    def is_full(self) -> bool:
        return (self.tail + 1) % self.size == self.head
