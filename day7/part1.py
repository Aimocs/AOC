strengthMap = { "A":13 ,  "K":12, " Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, " 2":1}



fiveKind=[]
fourKind=[]
fullHouseKind=[]
threeKind=[]
twoKind=[]
oneKind=[]



def removeNewline(x):
    return x.strip()

def typeFinder(handCards):
    typeMap={}
    for card in handCards:
        if(card in typeMap.keys()):
            typeMap[card]+=1    
        else:
            typeMap[card]=1
    return typeMap


with open('test.txt','r') as file:
    lines= file.readlines()
    lines=list(map(removeNewline,lines))
    tempRes=[]
    for line in lines:
        hand = line.split(" ")[0]
        parsedHand=typeFinder(hand)
        highKind=max(parsedHand.values())
        lowKind=min(parsedHand.values())
        if highKind==5:
            fiveKind.append(parsedHand)
        elif highKind==4:
            fourKind.append(parsedHand)
        elif highKind==3:
            if lowKind == 2:
                fullHouseKind.append(parsedHand)
            else:
                threeKind.append(parsedHand)
        elif highKind == 2:
            twoKind.append(parsedHand)
        elif highKind ==1 :
            oneKind.append(parsedHand)

print(fiveKind,fourKind,threeKind,fullHouseKind)
def sortForFive(deck):
    for i in range(0,len(deck)):
        fCard = i.keys[0]
        fCardStrength = strengthMap[fCard]
        

def sortForFour(deck):
    print(hand)
def sortForFull(deck):
    print(hand)
def sortForThree(deck):
    print(hand)
def sortForTwo(deck):
    print(hand)
def sortForOne(hand):
    print(hand)
typeFinder("AAAB3")
sortForFive(fiveKind)
