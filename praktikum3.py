file= open("E:/data1.txt","r")
sum = 0
for data1 in file:
    try:
        sum = sum + int(data1)

    except ValueError:
        continue
print(sum)
