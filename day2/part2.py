# only 12 red cubes, 13 green cubes, and 14 blue cubes.
cubesDict={"red":12,"green":13,"blue":14}

def compare(dict1,dist2) -> bool:
    for key in dict1:
        if int(dict1[key])<int(dist2[key]):
            return False
    return True
finalGamePoint=0
with open('puzzel.txt', 'r') as file:
    
    for line in file:
        allData=line.split(":")[1]
        setData=allData.split(";")
        tcubeDict={"red":0,"green":0,"blue":0}
        for content in setData:
            cubeSet=content.split(",")
            for cube in cubeSet:
                data=cube.strip().split(" ")
                if(tcubeDict[data[1]]<int(data[0])):
                    tcubeDict[data[1]]=int(data[0])
        product=1
        for value in tcubeDict.values():
            product *= value
        finalGamePoint+=product
print(finalGamePoint)