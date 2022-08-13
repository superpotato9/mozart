final = []
with open('train.txt', 'r+') as file:
    for line in file.readlines():
        if ' - ' not in line:
            final.append(line)
for i in final:
    print(i)



