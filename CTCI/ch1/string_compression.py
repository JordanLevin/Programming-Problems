#convert a string to a bunch of characters with the number of characters after
#if length wouldnt change, return original
def string_compression(word):
    ret = ''
    i = 0
    while i < len(word):
        count = 0
        character = word[i]
        while i < len(word) and word[i] == character:
            i+=1
            count+=1
        ret += (character + str(count))
    if len(ret) > len(word):
        return word
    return ret



if __name__ == '__main__':
    print(string_compression(input()))
