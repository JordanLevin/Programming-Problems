def urlify(chars, length):
    shift = len(chars) - length
    for i in range(length-1, -1, -1):
        # print([str(i).replace(' ', '-') for i in chars])
        # print(i)
        # print(shift)
        if chars[i] != ' ':
            chars[i+shift] = chars[i]
            if shift != 0:
                chars[i] = ' '
        else:
            shift -=2
    for i in range(0, len(chars)):
        if chars[i] == ' ':
            chars[i] = '%'
            chars[i+1] = '2'
            chars[i+2] = '0'
    return chars

if __name__ == '__main__':
    print(urlify(list(input()), int(input())))


'''
test word one    (end of string)
test word on    e  
test word o    ne  
test word     one  
test word     one  
'''
