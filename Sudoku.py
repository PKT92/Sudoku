path = 'test.txt'
inputFile = open(path, 'r')
test = [[] for i in range(9)]
for i in range(9):
    tmp = inputFile.readline()[:-1]
    for j in range(9):
        test[i].append(tmp[j])
print(*test, sep='\n')