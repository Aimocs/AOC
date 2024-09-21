#defining card's strength
strengthMap = { "A":13 ,  "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}

# list of different kind of cards 
fiveKind=[]
fourKind=[]
fullHouseKind=[]
threeKind=[]
twoKind=[]
oneKind=[]
painKind=[]
# mics
def removeNewline(x):
    return x.strip()

# takes hand and returns count dict of Card for eg.. typeFinder("ABBEE") returns {"A":1,"B":2,"E":2}
def typeFinder(handCards):
    typeMap={}
    for card in handCards:
        if(card in typeMap.keys()):
            typeMap[card]+=1    
        else:
            typeMap[card]=1
    return typeMap

# get card by number of card
def cardBynumber(deck, number):
# have to add something debug   
    for i in deck.keys():
        if deck[i] == number and i != "V":
            return i

with open('puzzel.txt','r') as file:
    lines= file.readlines()
    lines=list(map(removeNewline,lines))
    tempRes=[]
    for line in lines:
        hand = line.split(" ")[0] 
        value = int(line.split(" ")[1])
        parsedHand=typeFinder(hand)
        highKind=max(parsedHand.values())
        lowKind=min(parsedHand.values())
        parsedHand["V"]= value
        parsedHand["hand"]=hand
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
            cpparsed= parsedHand
            card= cardBynumber(cpparsed,2)
            del cpparsed[card]
            if(cardBynumber(cpparsed,2)!= None):
                twoKind.append(parsedHand)
            else:
                oneKind.append(parsedHand)
        else:
            painKind.append(parsedHand)
# print(fiveKind,fourKind,threeKind,fullHouseKind)
# print(fourKind)
# i think i found why test's are important i want to know what indexInsert does quickly without looking at the code , had i a test for this function i could just see what was expected and what was given.TDD FTW Also a painless debuging exp
# takes list index and value returns list with the value on the index
def indexInsert(deck, index, value):
    if index < 0:
        deck.insert(0, value)
    elif index >= len(deck):
        deck.append(value)
    else:
        deck.insert(index, value)
    return deck

# compares and returns which is stronger on the basis of card sequence
# RETURN VALUE : IF 1 the first deck stronger -1 IF the second deck stronger
def compare (deck1,deck2):
    for i in range(0,len(deck1)):
        if(strengthMap[deck1[i]]  < strengthMap[deck2[i]]):
            return -1
        elif( strengthMap[deck1[i]] >  strengthMap[deck2[i]]):
            return 1
# returns sortedFiveKind from weaktostrong
def sortFiveKind(decks):
    sortedFive=[]
    for i in range(0,len(decks)):
        Card = list(decks[i].keys())[0]
        Value = decks[i]['V']
        CardStrength = int(strengthMap[Card[0]])
        if(i == 0 ):
            # for test i will use Card instead of "value"
            insert = {"value" : Value, "strength" : CardStrength}
            sortedFive.append(insert)
            continue
        index = len(sortedFive)
        for j in range(0,len(sortedFive)):
            if(CardStrength < sortedFive[j]['strength']):
                index=j
                break
        insert = {"value":Value , "strength": CardStrength}
        indexInsert(sortedFive,index,insert )
    return (list(map(lambda x : x['value'],sortedFive)))
''' 

def sortFourKind(decks):
    sortedFour=[]
    for i in range(0,len(decks)):
        # Value = decks[i]['V']
        Card=cardBynumber(decks[i],4)
        # aCard=cardBynumber(decks[i],1)
        aCard=list(decks[i].keys())[0]
        Cardstrength = strengthMap[Card]
        aCardstregnth = strengthMap[aCard]
        strength= str(Cardstrength)+"-"+str(aCardstregnth)
        if(i == 0):           
            decks[i].update({ "strength": strength })
            sortedFour.append(decks[i])
            continue
        index=len(sortedFour)
        for j in range(0,len(sortedFour)):
            jstrength=int(sortedFour[j]['strength'].split("-")[0])
            # ajstrength=int(sortedFour[j]['strength'].split("-")[1])
            if(Cardstrength < jstrength):
                index = j
            elif Cardstrength == jstrength:
                if(compare(sortedFour[j]['hand'],decks[i]['hand'])==1):
                    index = j
        decks[i].update({"strength":strength})
        print(sortedFour)
        indexInsert(sortedFour,index,decks[i])
    return (list(map(lambda x : x['V'],sortedFour)))


'''
def sortFourKind(decks):
    sortedFour=[]
    for i in range(0,len(decks)):
        # Value = decks[i]['V']
        Card=cardBynumber(decks[i],4)
        # aCard=cardBynumber(decks[i],1)
        aCard=list(decks[i].keys())[0]
        Cardstrength = strengthMap[Card]
        aCardstregnth = strengthMap[aCard]
        strength= str(Cardstrength)+"-"+str(aCardstregnth)
        if(i == 0):           
            sortedFour.append(decks[i])
            continue
        index=len(sortedFour)
        for j in range(0,len(sortedFour)):
            if(compare(sortedFour[j]['hand'],decks[i]['hand'])==1):
                index = j
                break
        indexInsert(sortedFour,index,decks[i])
    return (list(map(lambda x : x['V'],sortedFour)))

def sortFullHouse(decks):
    sortedFull=[]
    for i in range(0,len(decks)):
        # Value = decks[i]['V']
        Card=cardBynumber(decks[i],3)
        # aCard=cardBynumber(decks[i],1)
        aCard=list(decks[i].keys())[0]
        Cardstrength = strengthMap[Card]
        aCardstregnth = strengthMap[aCard]
        strength= str(Cardstrength)+"-"+str(aCardstregnth)
        if(i == 0):           
            sortedFull.append(decks[i])
            continue
        index=len(sortedFull)
        for j in range(0,len(sortedFull)):
            # jstrength=int(sortedFull[j]['strength'].split("-")[0])
            # ajstrength=int(sortedFour[j]['strength'].split("-")[1])
            #if(Cardstrength < jstrength):
                #index = j
            #elif Cardstrength == jstrength:
            if(compare(sortedFull[j]['hand'],decks[i]['hand'])==1):
                index = j
                break
        indexInsert(sortedFull,index,decks[i])
    return (list(map(lambda x : x['V'],sortedFull)))

def sortTwoKind(decks):
    sortedFull=[]
    for i in range(0,len(decks)):
        # Value = decks[i]['V']
        # aCard=cardBynumber(decks[i],1)
        if(i == 0):           
            sortedFull.append(decks[i])
            continue
        index=len(sortedFull)
        for j in range(0,len(sortedFull)):
            print(compare(sortedFull[j]['hand'],decks[i]['hand']),"F",sortedFull[j]['hand'],"d",decks[i]['hand'],decks[i]["V"])
            if(compare(sortedFull[j]['hand'],decks[i]['hand'])==1):
                index = j
                print(index);
                break
            print(compare(sortedFull[j]['hand'],decks[i]['hand']),decks[i]['V'])
        print(sortedFull)
        indexInsert(sortedFull,index,decks[i])
    return (list(map(lambda x : x['V'],sortedFull)))    

five = sortFiveKind(fiveKind)
four = sortFourKind(fourKind)
full = sortFullHouse(fullHouseKind)
three = sortFullHouse(threeKind)
two = sortTwoKind(twoKind)
one = sortTwoKind(oneKind)
pain = sortTwoKind(painKind)
print(fiveKind,"<-Five",fourKind,"<-4",fullHouseKind,"<-full")#,threeKind,"<-3",twoKind,"<-2",oneKind,"<-1")
four.extend(five)
full.extend(four)
three.extend(full)
two.extend(three)
one.extend(two)
pain.extend(one)
sum=0;
for i,j in zip(range(0,len(pain)),range(1,len(pain)+1)):
    number = pain[i] * j
    sum = sum + number
print(one,sum)
