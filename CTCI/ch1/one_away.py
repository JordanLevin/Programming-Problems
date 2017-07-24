#given 2 strings, determine if first can be made into second with one add/del/replace
def one_away(a, b):
    if len(a) != len(b):
        return False;
    for i in range(len(a)):
        # print(a[:i]+a[i+1:])
        # print(b[:i]+b[i+1:])
        if a[:i]+a[i+1:] == b:
            return True
        if b[:i]+b[i+1:] == a:
            return True
        if a[:i]+a[i+1:] == b[:i]+b[i+1:]:
            return True
    return False
if __name__ == '__main__':
    print(one_away(input(), input()))
