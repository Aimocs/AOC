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
    defaultSymbols=["*","#","+","$","=","-","&","@","%","!","/","^","?"]
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

# function that compares lineobjects and returns sum of all the valid numbers in the targetline
def compare(topline,targetline,bottomline):
    result=[]
    symbols=[]
    if(topline is not None):
        symbols.extend(topline.symbols)
    if(targetline is not None):
        symbols.extend(targetline.symbols)
    if(bottomline is not None):
        symbols.extend(bottomline.symbols)
    for symbol in symbols:
        for i in range(len(targetline.number)):
            # for diagonal 
            if(-1 in targetline.scope[i]):
                continue
            if(symbol == max(targetline.scope[i])+1):
                result.append(int(targetline.number[i]))
                targetline.scope[i].append(-1)
            if(symbol == min(targetline.scope[i])-1):
                result.append(int(targetline.number[i]))
                targetline.scope[i].append(-1)
            if(symbol in targetline.scope[i]):
                result.append(int(targetline.number[i]))
                targetline.scope[i].append(-1)
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