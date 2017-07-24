def is_unique(word):
    seen = set()
    for character in word:
        if character not in seen:
            seen.add(character)
        else:
            return False
    return True
    

if __name__ == '__main__':
    print(is_unique(input()))
