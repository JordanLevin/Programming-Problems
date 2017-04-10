test_cases = input().strip()
for i in range(int(test_cases)):
    #number = input().strip()
    number = int(input().strip())
    tidy = False
    while not tidy:
        tidy = True
        for j in range(len(str(number))-1, 0, -1):
            if(int(str(number)[j]) < int(str(number)[j-1])):
                tidy = False
        if tidy:
            print("Case #" + str(i+1) + ": " + str(number))
        else:
            number = number - number%(10**(len(str(number))-j))-1
            #print(number%(10**len(str(number))-1))
            #number = number[:j+1] +'0' + number[j+2:]
            #number = str(int(number)-1)
            #print(number)
            #number = str(int(number)-1)
                

