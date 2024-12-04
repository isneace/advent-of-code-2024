# fp = open("input.txt", "r")
fp = open("test_input.txt", "r")

def isValidDifference(a, b):
  difference = abs(a - b)

  return difference > 0 and difference <= 3

def handleFailedCase(report, action, dampenerIsUsed):
  if(not dampenerIsUsed):
    if(len(report) >= 3 and isSafeReportRecursive([report[1], report[2]], action, dampenerIsUsed)):
      return isSafeReportRecursive(report[1:], action, True)
    else:
      # Removes the second index rather than the first
      report.pop(1)

      return isSafeReportRecursive(report, action, True)

  elif(dampenerIsUsed):
    print('----- Failed report ----- \n')

    return False

def isSafeReportRecursive(report, action, dampenerIsUsed):
  print(report)

  if(len(report) == 1):
    print('----- Successful report ----- \n')

    return True

  elif(not isValidDifference(report[0], report[1])):
    return handleFailedCase(report, action, dampenerIsUsed)

  elif(report[0] < report[1] and (not action or action == 'less')):
    return isSafeReportRecursive(report[1:], 'less', dampenerIsUsed)

  elif(report[0] < report[1] and action == 'greater'):
    return handleFailedCase(report, action, dampenerIsUsed)

  elif(report[0] > report[1] and (not action or action == 'greater')):
    return isSafeReportRecursive(report[1:], 'greater', dampenerIsUsed)

  elif(report[0] > report[1] and action == 'less'):
    return handleFailedCase(report, action, dampenerIsUsed)

  else:
    raise Exception("Else case hit, should not have happened.")

safeReportCount = 0
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()

    report = list(map(int, line.split()))
    reportIsSafe = isSafeReportRecursive(report, '', False)

    if(reportIsSafe):
      safeReportCount += 1

print(safeReportCount)