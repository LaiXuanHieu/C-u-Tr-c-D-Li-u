def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area

# Đọc input và xử lý từng test case
T = int(input().strip())

results = []
for _ in range(T):
    N = int(input().strip())
    heights = list(map(int, input().strip().split()))
    results.append(str(largest_rectangle_area(heights)))

# Xuất kết quả
print("\n".join(results))
