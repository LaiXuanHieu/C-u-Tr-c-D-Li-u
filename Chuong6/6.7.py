from collections import deque

def is_adjacent(word1, word2):
    """Kiểm tra xem word1 và word2 có khác nhau đúng 1 ký tự không"""
    count = sum(1 for a, b in zip(word1, word2) if a != b)
    return count == 1

def shortest_transformation_path(n, s, t, words):
    """Tìm khoảng cách ngắn nhất từ s -> t trong tập words"""
    if s == t:
        return 0  # Nếu s và t trùng nhau, không cần di chuyển

    word_set = set(words)  # Để tìm kiếm từ nhanh hơn
    if t not in word_set:
        return -1  # Không thể đến được t nếu t không có trong từ điển

    queue = deque([(s, 1)])  # Hàng đợi BFS (từ hiện tại, số bước)
    visited = set([s])  # Đánh dấu từ đã ghé thăm

    while queue:
        current_word, steps = queue.popleft()

        # Duyệt qua tất cả các từ trong tập từ điển
        for word in list(word_set):
            if is_adjacent(current_word, word):
                if word == t:
                    return steps + 1  # Nếu tìm thấy t, trả về số bước

                queue.append((word, steps + 1))
                visited.add(word)
                word_set.remove(word)  # Loại bỏ khỏi tập từ để tránh lặp lại

    return -1  # Nếu không thể tìm được đường đi

# Đọc dữ liệu từ input
T = int(input().strip())  # Số bộ test
results = []

for _ in range(T):
    n, s, t = input().strip().split()
    n = int(n)
    words = input().strip().split()

    result = shortest_transformation_path(n, s, t, words)
    results.append(str(result))

# In kết quả mỗi test trên một dòng
print("\n".join(results))
