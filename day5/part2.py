
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
with open("test.txt","r") as file:
    lines = file.readlines()
    seeds= lines[0].split(":")[1].strip()
    seeds = seeds.split(" ")
    seeds = list(map(int, seeds))
    print(seeds)
    source= []
    j=0
    from tqdm import trange
    while j < len(seeds)-1:
        for i in trange(int(seeds[j]),int(seeds[j+1])+int(seeds[j])):
            source.append(i)
        j+=2
    print(source)
    maps=[]
    for i in range(2,len(lines)):
        lineInList=lines[i].strip().split(" ")
        if(lineInList[0]==""):
            print(maps)
            source = compare(maps,source)
            print(source)
            maps=[]
            continue
        elif("to" in lineInList[0].split("-")):
            continue
        maps.append({"destination":int(lineInList[0]),"source":int(lineInList[1]),"range":int(lineInList[2])})
    print(min(compare(maps,source)))



