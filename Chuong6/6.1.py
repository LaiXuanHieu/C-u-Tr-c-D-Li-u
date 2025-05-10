def generate_binary_numbers(n):
    return " ".join(bin(i)[2:] for i in range(1, n + 1))

# Đọc số lượng test case
T = int(input().strip())

results = []
for _ in range(T):
    n = int(input().strip())
    results.append(generate_binary_numbers(n))

# Xuất kết quả mỗi test case trên một dòng
print("\n".join(results))
