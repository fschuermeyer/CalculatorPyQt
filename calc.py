class Calculator:
    
    operatoren = ["+","-","*","/"]

    def __init__(self):
        pass

    def isOperator(self,item):
        return item in self.operatoren

    def worker(self,formel):
        formelList = []

        for x in formel:
            if x.isnumeric():
                value = x
                if len(formelList) > 0 and (formelList[len(formelList) -1].isnumeric() or '.' in formelList[len(formelList) -1]):
                    formelList[len(formelList) -1] += value
                else:
                    formelList.append(value)
            elif self.isOperator(x):
                formelList.append(x)
            elif x == '.':
                formelList[len(formelList) -1] += x
                
        self.formels = { "+":lambda a,b : a+b,"-":lambda a,b : a-b,"*": lambda a,b: a*b,"/": lambda a,b: a/b}

        formelList = self.removeOpteratoren(formelList)
        formelList = self.pointFirst(formelList)

        while len(formelList) >= 3 and not self.isOperator(formelList[0]):
            value = self.formels[formelList[1]](float(formelList[0]),float(formelList[2]))

            formelList.pop(0)
            formelList.pop(0)
            formelList[0] = value
        
        return formelList[0]

    def removeOpteratoren(self,formelList):
        
        if self.isOperator(formelList[0]) and formelList[0] == "-":
            formelList[1] = float(formelList[0] + formelList[1])

            formelList.pop(0)

            return formelList
        elif self.isOperator(formelList[0]):
            value = self.formels[formelList[0]](0,float(formelList[1]))
            formelList[1] = value
            formelList.pop(0)

            return formelList
        else:
            return formelList

    def pointFirst(self,formelList):
        index = 0

        while "/" in formelList or "*" in formelList:
            if formelList[index] == "/" or formelList[index] == "*":
                formelList[index] = self.formels[formelList[index]](float(formelList[index-1]),float(formelList[index+1]))
                formelList.pop(index+1)
                formelList.pop(index-1)

                index -= 1
            else:
                index += 1

        return formelList
                 

def testUnit(value,defined):
    return value == defined


if __name__ == "__main__":
    
    c = Calculator()

    if testUnit(c.worker("57/5*10+20*5-2"),212) and testUnit(c.worker("-57/5*10+20*5-2"),-16):
        print("Work")

        