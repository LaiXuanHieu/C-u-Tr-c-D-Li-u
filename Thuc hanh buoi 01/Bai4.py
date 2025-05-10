class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Dung lượng tối đa của queue
        self.queue = []  # Danh sách dùng làm queue

    def enqueue(self, item):
        """Thêm phần tử vào cuối queue nếu chưa đầy."""
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            print("Queue is full!")

    def dequeue(self):
        """Lấy phần tử đầu tiên ra khỏi queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty!"

    def front(self):
        """Lấy giá trị phần tử đầu tiên nhưng không xóa."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty!"

    def is_empty(self):
        """Kiểm tra queue có rỗng không."""
        return len(self.queue) == 0

    def is_full(self):
        """Kiểm tra queue có đầy không."""
        return len(self.queue) == self.capacity


# Test chương trình theo yêu cầu
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())  # False
print(queue1.front())    # 1
print(queue1.dequeue())  # 1
print(queue1.front())    # 2
print(queue1.dequeue())  # 2
print(queue1.is_empty()) # True
