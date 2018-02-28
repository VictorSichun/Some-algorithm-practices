import sys
import math

linesNum = int(sys.stdin.readline())
while linesNum != 0:
    lineCounter = 1
    lineLen = 1
    adder = 1
    schwifty = ''
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
        elif lineCounter == 99999:
            lineLen += 1
            adder += 1
        lineCounter += 1
    for i in range(1, thisCase + 1):
        schwifty += str(i)
    print(schwifty[thisCase - 1])
    linesNum -= 1