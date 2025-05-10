import math

class Softmax:
    def __call__(self, x):
        exp_x = [math.exp(i) for i in x]  # Tính e^x cho từng phần tử
        sum_exp_x = sum(exp_x)  # Tổng tất cả giá trị mũ
        return [i / sum_exp_x for i in exp_x]  # Chia từng phần tử cho tổng

class SoftmaxStable:
    def __call__(self, x):
        c = max(x)  # Tìm giá trị lớn nhất trong x
        exp_x = [math.exp(i - c) for i in x]  # Tính e^(x-c) để tránh tràn số
        sum_exp_x = sum(exp_x)
        return [i / sum_exp_x for i in exp_x]

# Test Example
data = [1, 2, 3]

softmax = Softmax()
softmax_stable = SoftmaxStable()

output1 = softmax(data)
output2 = softmax_stable(data)

print("Softmax Output:", output1)
print("Softmax Stable Output:", output2)