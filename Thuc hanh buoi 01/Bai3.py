class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity  # Dung lượng tối đa của stack
        self.stack = []  # Danh sách dùng làm stack

    def push(self, item):
        """Thêm phần tử vào stack nếu chưa đầy."""
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        """Lấy phần tử trên cùng ra khỏi stack."""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def top(self):
        """Lấy giá trị phần tử trên cùng nhưng không xóa."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        """Kiểm tra stack có rỗng không."""
        return len(self.stack) == 0

    def is_full(self):
        """Kiểm tra stack có đầy không."""
        return len(self.stack) == self.capacity


# Test chương trình theo yêu cầu
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())  # False
print(stack1.top())      # 2
print(stack1.pop())      # 2
print(stack1.top())      # 1
print(stack1.pop())      # 1
print(stack1.is_empty()) # True
