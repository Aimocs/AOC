final=0

# class for maanging line metadata
class Linemetadata:
    def __init__(self, number, scope,symbols):
        self.number = number
        self.scope = scope
        self.symbols = symbols


# function that takes in a line and returns Linemetadata
def lineobject(line):
    number=""
    index=[]
    symbols=[]
    scope=[]
    finalnumber=[]
    defaultSymbols=["*"]
    j=0
    length=len(line)
    for i in line:
        if(i.isdigit()):
            number+=i
            index.append(j)
            if(j==length-1):
                finalnumber.append(number)
                scope.append(index)
                number=""
                index=[]
        elif(i in defaultSymbols):
            if(number!=""):
                finalnumber.append(number)
                scope.append(index)
                number=""
                index=[]
            symbols.append(j)
        else:
            if(number!=""):
                finalnumber.append(number)
                scope.append(index)
                number=""
                index=[]
        j+=1
    return Linemetadata(finalnumber,scope,symbols)

# function that compares lineobjects and returns sum of ratio of gear of the targetline
def compare(topline,targetline,bottomline):
    result=[]
    symbols=[]
    symbols.extend(targetline.symbols)
    for symbol in symbols:
        numberCount=[]
        # we know target will never be none
        for i in range(len(targetline.number)):
            if(symbol == max(targetline.scope[i])+1):
                numberCount.append(int(targetline.number[i]))
            if(symbol == min(targetline.scope[i])-1):
                numberCount.append(int(targetline.number[i]))
            if(symbol in targetline.scope[i]):
                numberCount.append(int(targetline.number[i]))
        if(topline is not None):
            for i in range(len(topline.number)):
                if(symbol == max(topline.scope[i])+1):
                    numberCount.append(int(topline.number[i]))
                if(symbol == min(topline.scope[i])-1):
                    numberCount.append(int(topline.number[i]))
                if(symbol in topline.scope[i]):
                    numberCount.append(int(topline.number[i]))
        if(bottomline is not None):
            for i in range(len(bottomline.number)):
                if(symbol == max(bottomline.scope[i])+1):
                    numberCount.append(int(bottomline.number[i]))
                if(symbol == min(bottomline.scope[i])-1):
                    numberCount.append(int(bottomline.number[i]))
                if(symbol in bottomline.scope[i]):
                    numberCount.append(int(bottomline.number[i]))
        if len(numberCount) == 2:
            result.append(numberCount[0]*numberCount[1])
    return sum(result)



# main part where each line is fed into the lineobject and compare function and sum is calculated
with open('puzzel.txt', 'r') as file:

    lines = file.readlines()
    for i in range(len(lines)):
        target = lineobject(lines[i])
        if(i==0):
            top=None
            bottom=lineobject(lines[i+1])
        elif(i==len(lines)-1):
            top=lineobject(lines[i-1])
            bottom=None
        else:
            top=lineobject(lines[i-1])
            bottom=lineobject(lines[i+1])
        final+=compare(top,target,bottom)
print(final)