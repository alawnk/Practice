i = 1
s = 0
while i < 100:
    # print(i)
    # i = i + 1
    if i%2 == 0:
        s = s - i
    else:
        s = s + i
    i = i+1
    print(s)

