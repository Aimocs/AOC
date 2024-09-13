import math
final=0
def linetolist(line):
    return list(filter(lambda x: x != '', line.split(' ')))


def pointCalculator(winCards,handCards):
    tpoint=1
    winCardCount=0
    for card in handCards:
        if(card in winCards):
            winCardCount+=1
    if(winCardCount==1):
        return 1
    elif(winCardCount==0):
        return 0
    tpoint=int(math.pow(2,winCardCount-1))
    return tpoint

with open("puzzel.txt","r") as file:
    for line in file:
       gameCards=line.split(":")[1]
       winCards=linetolist(gameCards.split("|")[0])
       handCards=linetolist(gameCards.split("|")[1].strip())
       final+=pointCalculator(winCards,handCards)
print(final)