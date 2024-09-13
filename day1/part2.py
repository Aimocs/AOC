def checkLeft(str):
    length=len(str)
    for i in range(length):
        lettercoll=""
        balancefactor= length-i
        if(balancefactor>=5):
            balancefactor=5
        elif(balancefactor<5):
            balancefactor=length-i
        for j  in range (i,i+balancefactor):
            if(str[j].isdigit() and lettercoll==""):
                return str[j]
            lettercoll+=str[j]
            if (lettercoll in wnumber.keys()):
                return wnumber[lettercoll]

def checkRight(str,leftnumber):
    result=leftnumber
    length=len(str)
    for i in range(length):
        lettercoll=""
        balancefactor= length-i
        if(balancefactor>=5):
            balancefactor=5
        elif(balancefactor<5):
            balancefactor=length-i
        for j  in range (i,i+balancefactor):
            if(str[j].isdigit() and lettercoll==""):
                result=str[j]
            lettercoll+=str[j]
            if (lettercoll in wnumber.keys()):
                result=wnumber[lettercoll]
    return result


# Open the file in read mode
calibration_sum=0
# word number dict
wnumber={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
def calibration_value(str):
    lettercoll=""
    left=checkLeft(str)
    right=checkRight(str,left)
    return (int(left)*10+int(right))
with open('calibration.txt', 'r') as file:
    for line in file:
        # print(calibration_value(line))
        calibration_sum+=calibration_value(line)

print(calibration_sum)