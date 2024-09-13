def removeSpaceandconverttoInt(line):
    if(line!=""):
       return line
def product_of_elements(arr):
    product = 1
    for num in arr:
        product *= num
    return product


with open("puzzel.txt", 'r') as file:
    lines = file.readlines()
    raceTimes = list(filter(removeSpaceandconverttoInt,lines[0].strip().split(":")[1].split(" ")))
    recordDistance=list(filter(removeSpaceandconverttoInt,lines[1].strip().split(":")[1].split(" ")))
    # the races times all times 
    race=int(''.join(map(str, raceTimes)))
    record=int(''.join(map(str, recordDistance)))
    result=[]
    for i in range(0,race+1):
        timeTomove= race - i 
        result.append(timeTomove*i)
    print(len(list(filter(lambda x: x>record,result))))
        # check if it beats recordDistance