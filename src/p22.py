f = open('C:\\Users\\Ninjoncrack\\Desktop\\names.txt', 'r')
nameArray = ""
for line in f.readlines():
    nameArray = line.split(",")

for i in range(0,len(nameArray)):
    nameArray[i] = nameArray[i][1:-1]
nameArray.sort()

total = 0
for distance in range(0, len(nameArray)):
    letterSum = 0
    for letter in nameArray[distance]:
        letterSum += ord(letter.lower()) - 96
    total += (distance+1)*letterSum
        
print(total)
