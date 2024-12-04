import re

fp = open("input.txt", "r")
# fp = open('test_input.txt', 'r')

total = 0
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    matches = re.findall(r"((mul\()\d{1,3},\d{1,3}(\)))", line)

    allMatches = ''
    for match in matches:
      allMatches += match[0]

    allNumbers = list(map(int, re.findall(r'\d{1,3}', allMatches)))

    while True:
      print(allNumbers)
      if(not len(allNumbers)):
        break

      total += (allNumbers[0] * allNumbers[1])

      allNumbers = allNumbers[2:]


print(total)