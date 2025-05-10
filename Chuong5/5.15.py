def next_greater_right_smaller(arr, n):
    next_greater = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            next_greater[stack.pop()] = i
        stack.append(i)
    
    next_smaller = [-1] * n
    stack.clear()
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            next_smaller[stack.pop()] = arr[i]
        stack.append(i)
    
    result = []
    for i in range(n):
        if next_greater[i] != -1:
            result.append(next_smaller[next_greater[i]])
        else:
            result.append(-1)
    
    return result

T = int(input().strip())
results = []

for _ in range(T):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    results.append(" ".join(map(str, next_greater_right_smaller(arr, n))))

print("\n".join(results))