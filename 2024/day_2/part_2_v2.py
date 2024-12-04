# fp = open("test_input.txt", "r")
fp = open("input.txt", "r")

def isValidDifference(a, b):
  difference = abs(a - b)

  return difference > 0 and difference <= 3

def isConsistentlyDecreasing(report):
  for idx, _ in enumerate(report):
    if(idx + 1 == len(report)):
      break

    currentValue = report[idx]
    nextValue = report[idx + 1]

    if(isValidDifference(currentValue, nextValue) and currentValue > nextValue):
      continue

    else:
      return False

  return True

def isConsistentlyIncreasing(report):
  for idx, _ in enumerate(report):
    if(idx + 1 == len(report)):
      break

    currentValue = report[idx]
    nextValue = report[idx + 1]

    if(isValidDifference(currentValue, nextValue) and currentValue < nextValue):
      continue

    else:
      return False

  return True

def attemptToFix(report):
  for idx, _ in enumerate(report):
    filteredReport = list(map(lambda levelDetails: levelDetails[1], filter(lambda levelDetails: idx != levelDetails[0], enumerate(report))))
    print(filteredReport)

    if(isConsistentlyDecreasing(filteredReport)):
      print('\n', 'Report :', report, ' succeeded (decreasing) by removing: ', report[idx], '\n')
      return True
    elif(isConsistentlyIncreasing(filteredReport)):
      print('\n', 'Report :', report, ' succeeded (increasing) by removing: ', report[idx], '\n')
      return True

  print('\n', 'Failed to fix report: ', report, '\n')
  return False

safeReportCount = 0
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    report = list(map(int, line.split()))

    if(isConsistentlyDecreasing(report)):
      safeReportCount += 1
    else:
      if(isConsistentlyIncreasing(report)):
        safeReportCount += 1
      else:
        if(attemptToFix(report)):
          safeReportCount += 1

print(safeReportCount)