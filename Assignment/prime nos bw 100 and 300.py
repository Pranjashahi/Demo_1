nos = []
for i in range( 100 , 300):
    count = 0
    for j in range(1 , i + 1):
        if i % j == 0:
            count +=1
    if count == 2:
        nos.append(i)
print(nos)