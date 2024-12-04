fp = open("input.txt", "r")

arr_1 = []
arr_2 = []

while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    [first, second] = line.split()

    arr_1.append(first)
    arr_2.append(second)

arr_1.sort()
arr_2.sort()

total = 0

for idx, value in enumerate(arr_1):
 total += abs(int(arr_2[idx]) - int(value))

print(total)
