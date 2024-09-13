# Open the file in read mode
calibration_sum=0
def calibration_value(str):
    ff= False
    fl= False
    length = len(str)
    for i in range(length):
        if str[i].isdigit():
            if(ff== False):
                ff = True
                front=int(str[i])
            last=int(str[i])
    return (front*10+last)
with open('calibration.txt', 'r') as file:
    for line in file:
        calibration_sum+=calibration_value(line)

print(calibration_sum)