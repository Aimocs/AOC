def removeSpaceandconverttoInt(line):
    if(line!=""):
       return int(line)
    return None
def product_of_elements(arr):
    product = 1
    for num in arr:
        product *= num
    return product

with open("puzzel.txt", 'r') as file:
    lines = file.readlines()
    raceTimes = list(filter(None,map(removeSpaceandconverttoInt,lines[0].strip().split(":")[1].split(" "))))
    recordDistance=list(filter(None,map(removeSpaceandconverttoInt,lines[1].strip().split(":")[1].split(" "))))
    # the races times all times 
    ultres=[]
    for j in range(0,len(raceTimes)):
        result=[]
        for i in range(0,raceTimes[j]+1):
            timeTomove= raceTimes[j] - i 
            result.append(timeTomove*i)
        #    code to count all the winning races
        ultres.append(len(list(filter(lambda x: x>recordDistance[j],result))))
    print(product_of_elements(ultres))
        # check if it beats recordDistance