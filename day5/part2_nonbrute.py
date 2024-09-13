# function compares and returns new source
def compare(map,source):
    result=[]
    length = len(source)
    i=0
    while i < len(source):
        foundFlag=False
        for j in map:
            # print(result)
            uprange= j["source"]
            downrange= j["range"]+j["source"]-1
            if(uprange<=source[i][0]<=downrange):
                if(uprange<=source[i][1]<=downrange):
                    first= source[i][0] - j["source"]
                    first = first + j["destination"]
                    second= (source[i][1]-source[i][0]) + first
                    result.append([first,second])
                    foundFlag=True
                else:
                    first = source[i][0] - j["source"]
                    first = first + j["destination"]
                    second = j['destination']+j['range']-1
                    result.append([first,second])
                    source[i]=[int(downrange)+1,source[i][1]]
                    
            elif(uprange<=source[i][1]<=downrange):
                first = j['destination']
                second = source[i][1]-uprange
                second = second + j['destination']
                result.append([first,second])
                source[i]=[source[i][0],(source[i][0]+(uprange-source[i][0]))-1]

            elif(source[i][0]<=j['source']<=source[i][1]):
                first = j['destination']
                second = j['destination']+j['range']-1
                result.append([first,second])
                foundFlag=True
                remaining = compare(map,[[source[i][0],source[i][0]+(j['source']-source[i][0]-1)],[j['source']+j['range'],source[i][1]]])
                result.extend(remaining)
        if(foundFlag==False):
            result.append([source[i][0],source[i][1]])
        i=i+1
    return result
# finding min 
def returnMin(x):
    return min(x)
with open("puzzel.txt","r") as file:
    lines = file.readlines()
    seeds= lines[0].split(":")[1].strip()
    seeds = seeds.split(" ")
    seeds = list(map(int, seeds))
    source= []
    j=0

    while j < len(seeds)-1:
        source.append([int(seeds[j]),int(seeds[j])+int(seeds[j+1])-1])
        j+=2
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
    # last compare because no "" line 
    final = compare(maps,source)
    print(min((list(map(returnMin,final)))))