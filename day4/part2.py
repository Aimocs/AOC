def winCardCount(winCards,handCards):    
    winCardCount=0
    for card in handCards:
        if(card in winCards):
            winCardCount+=1
    return winCardCount 
def linetolist(line):
    return list(filter(lambda x: x != '', line.split(' ')))

def addCards(cardNo,space,cardCopies):
    if(cardNo in cardCopies):
        cardCopies[cardNo]+=1
    else:
        cardCopies[cardNo]=1
    for i in range(1,space+1):
        if(cardNo+i in cardCopies):
            cardCopies[cardNo+i]+=cardCopies[cardNo]
        else:
            cardCopies[cardNo+i]=cardCopies[cardNo]
    return cardCopies
with open("puzzel.txt","r") as file:
    cardCopies={}
    lines = file.readlines()
    length=len(lines)
    for i in range(len(lines)):
        curLine = lines[i].strip()
        gameCards = curLine.split(":")[1]
        curLine = curLine.split(":")[0].split(" ")
        winCards=linetolist(gameCards.split("|")[0])
        handCards=linetolist(gameCards.split("|")[1].strip()) 
        # remove elements(white spaces ) from the curLine
        curLine = list(filter(lambda x : x!= "",curLine))
        cardNo=int(curLine[1])
        winCardsCount=winCardCount(winCards,handCards)
        space = length - cardNo
        if(space >= winCardsCount):
            space= winCardsCount
            cardCopies=addCards(cardNo,space,cardCopies)
        else: 
            cardCopies=addCards(cardNo,space,cardCopies)
    print(sum(cardCopies.values()))     
