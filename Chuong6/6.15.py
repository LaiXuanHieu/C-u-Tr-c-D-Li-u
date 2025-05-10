from collections import deque

# Sàng Eratosthenes để tìm tất cả số nguyên tố có 4 chữ số
def sieve_primes():
    primes = [True] * 10000
    primes[0] = primes[1] = False  # 0 và 1 không phải số nguyên tố
    
    for i in range(2, 100):
        if primes[i]:
            for j in range(i * i, 10000, i):
                primes[j] = False

    # Lọc ra các số nguyên tố có 4 chữ số
    prime_set = {i for i in range(1000, 10000) if primes[i]}
    return prime_set

# BFS tìm số bước biến đổi ít nhất từ S đến T
def bfs_shortest_path(S, T, prime_set):
    if S == T:
        return 0  # Nếu S đã là T, không cần bước nào
    
    queue = deque([(S, 0)])  # Hàng đợi chứa (số hiện tại, số bước)
    visited = set()  # Đánh dấu số đã xét
    visited.add(S)

    while queue:
        num, steps = queue.popleft()
        str_num = str(num)

        # Thay đổi từng chữ số một
        for i in range(4):  # Duyệt từng vị trí chữ số
            for digit in "0123456789":  # Thử thay đổi thành các số từ 0-9
                if digit == str_num[i]:  # Nếu giống số cũ, bỏ qua
                    continue

                new_num = str_num[:i] + digit + str_num[i+1:]  # Tạo số mới
                new_num = int(new_num)

                # Nếu số hợp lệ, chưa xét và là số nguyên tố thì thêm vào queue
                if new_num in prime_set and new_num not in visited:
                    if new_num == T:  # Nếu tìm thấy T, trả về ngay
                        return steps + 1
                    queue.append((new_num, steps + 1))
                    visited.add(new_num)

    return -1  # Nếu không tìm thấy đường đi (trường hợp đặc biệt)

def main():
    prime_set = sieve_primes()  # Tiền xử lý danh sách số nguyên tố
    T = int(input().strip())  # Số lượng test
    results = []
    
    for _ in range(T):
        S, T = map(int, input().strip().split())
        results.append(str(bfs_shortest_path(S, T, prime_set)))

    print("\n".join(results))  # In tất cả kết quả theo từng dòng

if __name__ == "__main__":
    main()
