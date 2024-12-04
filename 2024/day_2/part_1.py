fp = open("input.txt", "r")

reports = []
while True:
    line = fp.readline()
    if line == "":
        break

    line = line.strip()
    reports.append(list(map(int, line.split())))

def isValidDifference(a, b):
  difference = abs(a - b)
  return difference > 0 and difference <= 3

def isSafeReportRecursive(report, action = ''):
  if(len(report) == 1):
    return True

  elif(not isValidDifference(report[0], report[1])):
    return False

  elif(report[0] < report[1] and (not action or action == 'less')):
    return isSafeReportRecursive(report[1:], 'less')

  elif(report[0] < report[1] and action == 'greater'):
    return False

  elif(report[0] > report[1] and (not action or action == 'greater')):
    return isSafeReportRecursive(report[1:], 'greater')

  elif(report[0] > report[1] and action == 'less'):
    return False

print(len(list(filter(lambda report: isSafeReportRecursive(report), reports))))
