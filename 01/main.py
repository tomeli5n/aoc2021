#day 1

with open("input.txt") as f:
    data = f.readlines()

#print(data)
datapoint = 9999 # TODO: change to input
increased_datapoint = 0

for measure in data:
    if datapoint < int(measure):
       increased_datapoint += 1
    datapoint = int(measure)
    
print("part one:" + str(increased_datapoint))

# part two

print(range(len(data)))

increased_3avg = 0

try:
    for i in range(len(data)):
        print("_________" + str(i))
   
        _a = int(data[i]) + int(data[(i+1)]) + int(data[(i+2)])
        _b = int(data[(i+1)]) + int(data[(i+2)]) + int(data[(i+3)])
        print("a: " + str(_a))
        print("b: " + str(_b))

        if _a < _b:
            print("increased: " + str(_a) + " " + str(_b))
            increased_3avg += 1
except:
    print("out of range")

print("part two:" + str(increased_3avg))