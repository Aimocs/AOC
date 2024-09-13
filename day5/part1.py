# function that compare source and destination and returns corresponding number
def compare(map,source):
    result=[]
    for i in source:
        foundFlag=False
        for j in map:
            uprange= j["source"]
            downrange= j["range"]+j["source"]
            if(uprange<=i<=downrange):
                addative = i - j["source"]
                result.append(addative+j["destination"])
                foundFlag=True
        if(foundFlag==False):
            result.append(i)

    # returns a list that looks something like the initial list 
    return result
with open("puzzel.txt","r") as file:
    lines = file.readlines()
    seeds= lines[0].split(":")[1].strip()
    seeds = seeds.split(" ")
    seeds = list(map(int, seeds))
    source= seeds
    maps=[]
    for i in range(2,len(lines)):
        lineInList=lines[i].strip().split(" ")
        if(lineInList[0]==""):
            source = compare(maps,source)
            maps=[]
            continue
        elif("to" in lineInList[0].split("-")):
            continue
        maps.append({"destination":int(lineInList[0]),"source":int(lineInList[1]),"range":int(lineInList[2])})
    print(min(compare(maps,source)))



