import math
import random
import matplotlib.pyplot as plt

# Số ngày trong năm
days = range(1, 366)

# Mô phỏng nhiệt độ (theo chu kỳ mùa)
base_temp = 15  # nhiệt độ cơ bản
season_variation = [10 * math.sin(2 * math.pi * day / 365) for day in days]  # dao động theo mùa
daily_temp = [base_temp + season_variation[i] + random.gauss(0, 2) for i in range(len(days))]

# Mô phỏng lượng mưa (dựa trên xác suất theo mùa)
rain_chance = [0.3 + 0.2 * math.cos(2 * math.pi * (day - 80) / 365) for day in days]  # Xác suất mưa cao vào mùa xuân và thu
rain_amount = [random.random() < rain_chance[i] for i in range(len(days))]  # Sự kiện mưa
precipitation = [rain_amount[i] * random.uniform(0, 10) for i in range(len(days))]  # Lượng mưa ngẫu nhiên khi mưa xảy ra

# Vẽ biểu đồ kết quả mô phỏng
plt.figure(figsize=(12, 6))

# Biểu đồ nhiệt độ
plt.subplot(2, 1, 1)
plt.plot(days, daily_temp, color='orange', label="Nhiệt độ (°C)")
plt.title("Mô phỏng nhiệt độ theo ngày trong năm")
plt.ylabel("Nhiệt độ (°C)")
plt.grid(True)
plt.legend()

# Biểu đồ lượng mưa
plt.subplot(2, 1, 2)
plt.bar(days, precipitation, color='blue', label="Lượng mưa (mm)")
plt.title("Mô phỏng lượng mưa")
plt.xlabel("Ngày")
plt.ylabel("Lượng mưa (mm)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()