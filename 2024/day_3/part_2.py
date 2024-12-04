import re

fp = open("input.txt", "r")
# fp = open('test_input_2.txt', 'r')

# the `?` after the `*` is what makes it so that I don't select from the first `don't` to the last `do`, it selects them individually
REGEX = r"(?<=don\'t\(\)).*?(?=do\(\))"

megaLine = ''
total = 0
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    megaLine += line

megaLine = re.sub(REGEX, '', megaLine)
matches = re.findall(r"((mul\()\d{1,3},\d{1,3}(\)))", megaLine)

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
