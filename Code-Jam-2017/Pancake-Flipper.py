def main():

    amount = int(input().strip())

    for i in range(amount):
        inputs = input().split(" ")
        pancakes = input[0]
        k = input[1] #number that the flipper does at one time?
        done = false
        result = 0
        while !done:
            done = true
            for flipped in pancakes:
                if flipped == '-':
                    done = false
            if done:
                break;
            result+=1
            #logic goes here
        print("Case #" + str(i+1) + ": " + str(result))


