def arithmetic_arranger(problems, displayAnswers = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  displayLine1 = ""
  displayLine2 = ""
  displayLine3 = ""
  displayLine4 = ""
  
  for problem in problems:
    elems = problem.split(" ")
    firstNum = elems[0]
    operator = elems[1]
    secondNum = elems[2]
    if (firstNum.isdigit() is not True) or (secondNum.isdigit() is not True):
      return "Error: Numbers must only contain digits."
    if (operator != '+') and (operator != '-'):
      return "Error: Operator must be '+' or '-'."
    firstLen = len(firstNum)
    secondLen = len(secondNum)
    if (firstLen > 4) or (secondLen > 4):
      return "Error: Numbers cannot be more than four digits."
    length = max(firstLen, secondLen) + 2
    firstNum = firstNum.rjust(length)
    secondNum = secondNum.rjust(length - 2) 
    line = ""
    for i in range(length):
      line = line + "-"
    displayLine1 = displayLine1 + firstNum + "    "
    displayLine2 = displayLine2 + operator + " " + secondNum + "    "
    displayLine3 = displayLine3 + line + "    "
    if (displayAnswers):
      answer = 0
      if (operator == '+'):
        answer = int(firstNum) + int(secondNum)
      elif (operator == "-"):
        answer = int(firstNum) - int (secondNum)
      displayLine4 = displayLine4 + str(answer).rjust(length) + "    "
  display = displayLine1.rstrip() + "\n" + displayLine2.rstrip() + "\n" + displayLine3.rstrip()
  if (displayAnswers):
    display = display + "\n" + displayLine4.rstrip()
  return display