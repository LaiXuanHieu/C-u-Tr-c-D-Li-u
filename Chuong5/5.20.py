def decode_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)  # Tính số lặp nhiều chữ số
        elif char == '[':
            stack.append((current_string, current_number))  # Lưu trạng thái trước khi vào []
            current_string = ""
            current_number = 0
        elif char == ']':
            last_string, repeat_count = stack.pop()  # Lấy phần trước đó
            current_string = last_string + current_string * repeat_count  # Nhân chuỗi con rồi nối vào
        else:
            current_string += char  # Ký tự thường, thêm vào chuỗi hiện tại

    return current_string

# Đọc input và xử lý từng test case
T = int(input().strip())

results = []
for _ in range(T):
    encoded_string = input().strip()
    results.append(decode_string(encoded_string))

# Xuất kết quả
print("\n".join(results))
