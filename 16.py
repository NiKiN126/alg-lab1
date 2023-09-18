a = {1: 1}
for i in range(2, 2024):
    a[i] = i * a[i - 1]
print(a[2023] / a[2020])
