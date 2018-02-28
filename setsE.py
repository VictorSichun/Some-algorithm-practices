"""
Name: Sichun Yin
UPI: vyin171
id: 911587190
"""
import sys
listSet = {}
setList = {}
def isSet(item):
    global listSet
    if len(item) < 2:
        #print(1, item)
        return False
    elif item[0] == "{" and item[-1] == "}" :
        item = item[1:-1]
        return isElementList(item)




def isElementList(item):
    if not item:
        return True

    if isList(item):
        listSet[item] = True
        return True
    else:
        listSet[item] = False
            # print(2, item)
        return False


def isList(item):
    global listSet
    if isElement(item):
        return True
    else:
        for i,ltr in enumerate(item):
            if ltr == ',':
                commaA = item[: i]
                # print(commaA)
                commaB = item[i + 1:]
                # print(commaB)
                if isElement(commaA):
                    try:
                        if listSet[commaB]:
                            return True
                    except:
                        if isList(commaB):
                            listSet[commaB] = True
                            return True
                        else:
                            listSet[commaB] = False
        return False  # print(4, item)



def isElement(item):
    global setList
    if item == ',' or item == '{' or item == '}':
        return True
    else:
        try:
            return setList[item]
        except:
            if isSet(item):
                setList[item] = True
                return True
            else:
                setList[item] = False
                return False

def main():
    global setList
    global listSet
    length = int(sys.stdin.readline())
    for num in range(length):

        currentSet = sys.stdin.readline()
        currentSet = currentSet[:-1]
        if isSet(currentSet):
            setList[currentSet] = True
            print("Word #" + str(num + 1) + ": Set")
        else:
            setList[currentSet] = False
                #print(6, currentSet)
            print("Word #" + str(num + 1) + ": No Set")
main()
