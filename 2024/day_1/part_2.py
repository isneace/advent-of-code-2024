fp = open("input.txt", "r")

arr_1 = []
arr_2 = []

while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    [first, second] = line.split()

    arr_1.append(int(first))
    arr_2.append(int(second))

total = sum([arr_2.count(value) * value for value in arr_1])

print(total)