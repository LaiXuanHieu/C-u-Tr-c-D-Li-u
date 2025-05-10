from collections import deque

def generate_lucky_numbers(max_length):
    queue = deque(["6", "8"])
    lucky_numbers = []

    while queue:
        number = queue.popleft()
        if len(number) > max_length:
            break
        lucky_numbers.append(int(number))
        queue.append(number + "6")
        queue.append(number + "8")

    return sorted(lucky_numbers, reverse=True)  # Sắp xếp giảm dần

def main():
    T = int(input().strip())  # Số lượng bộ test
    test_cases = [int(input().strip()) for _ in range(T)]  # Đọc từng giá trị N

    for N in test_cases:
        lucky_numbers = generate_lucky_numbers(N)
        print(len(lucky_numbers))
        print(*lucky_numbers)

if __name__ == "__main__":
    main()
