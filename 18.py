data = []
for i in range(500):
    data.append(float(input().replace(',', '.')))
print(data)
s = data[0]
max_s = 0
for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        s += data[i + 1]
    if data[i] <= data[i + 1] or i + 2 == len(data):
        max_s = max(max_s, s)
        s = data[i + 1]
print(int(max_s))

