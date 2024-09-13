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
        flag=True
        for content in setData:
            cubeSet=content.split(",")
            # print(cubeSet)
            tcubeDict={"red":0,"green":0,"blue":0}
            for cube in cubeSet:
                data=cube.strip().split(" ")
                tcubeDict[data[1]]+=int(data[0])
            # print(tcubeDict)
            if compare(cubesDict,tcubeDict) != True:
                flag=False
                break
        if flag==True:
            gameNo=line.split(":")[0]
            gameNo=int(gameNo.strip().split(" ")[1])
            finalGamePoint+=gameNo

print (finalGamePoint)