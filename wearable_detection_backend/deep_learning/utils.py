class LoopQueue(object):
    """
    自定义的循环队列，用于缓存安卓端传入的血压检测数据。
    """

    def __init__(self, size=5):
        # 预留一个空间用于判断队列是否为满
        self.queue = [None] * (size + 1)
        # 队首指针，指向要出队的队首元素
        self.front = 0
        # 队尾指针，指向下一个入队的位置
        self.rear = 0

    def __len__(self):
        return len(self.queue)

    def is_full(self):
        return (self.rear + 1) % len(self.queue) == self.front

    def is_empty(self):
        return self.rear == self.front

    def enqueue(self, elem):
        self.queue[self.rear] = elem
        self.rear = (self.rear + 1) % len(self.queue)

    def dequeue(self):
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)

    def list(self):
        """
        遍历队列元素，并拼接成一个list返回
        :return:包含队列所有元素的list
        """
        front = self.front
        rear = self.rear

        queue_list = []

        while front != rear:
            queue_list.extend(self.queue[front])
            front = (front + 1) % len(self.queue)

        return queue_list
