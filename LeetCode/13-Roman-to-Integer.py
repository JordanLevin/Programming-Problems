class Solution(object):
    def romanToInt(self, s):
        value = 0
        characters = [i for i in s]
        for i in range(len(characters)):
            if characters[i] == 'I':
                characters[i] = 1
            if characters[i] == 'V':
                characters[i] = 5
            if characters[i] == 'X':
                characters[i] = 10
            if characters[i] == 'L':
                characters[i] = 50
            if characters[i] == 'C':
                characters[i] = 100
            if characters[i] == 'D':
                characters[i] = 500
            if characters[i] == 'M':
                characters[i] = 1000
        if len(characters) == 1:
            return characters[0]
        check_first = False
        ignore = False
        for i in range(len(characters)-1, 0, -1):
            if ignore:
                ignore = False
                continue
            if characters[i-1] < characters[i]:
                value += characters[i] - characters[i-1]
                if i == 2:
                    check_first = True
                ignore = True
            else:
                if i == 1:
                    check_first = True
                value += characters[i]
        if check_first:
            value += characters[0]
        return value