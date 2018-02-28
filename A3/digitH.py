import sys

linesNum = int(sys.stdin.readline())
schwifty = ''
lastNum = 0
while linesNum != 0:
    lineCounter = 1
    lineLen = 1
    adder = 1
    thisCase = int(sys.stdin.readline())
    while thisCase > lineLen:
        thisCase -= lineLen
        lineLen += adder
        if lineCounter == 9:
            lineLen += 1
            adder += 1
        elif lineCounter == 99:
            lineLen += 1
            adder += 1
        elif lineCounter == 999:
            lineLen += 1
            adder += 1
        elif lineCounter == 9999:
            lineLen += 1
            adder += 1
        lineCounter += 1

    if thisCase < len(schwifty):
        print(schwifty[thisCase - 1])
    else:
        for i in range(lastNum + 1, lineCounter + 1):
            schwifty += str(i)
        print(schwifty[thisCase - 1])
        lastNum = lineCounter
    linesNum -= 1