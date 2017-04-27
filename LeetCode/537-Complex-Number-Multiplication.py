class Solution(object):
    def complexNumberMultiply(self, a, b):
        first = a.split("+")
        second = b.split("+")
        a = int(first[0])
        b = int(first[1].replace("i", ""))
        c = int(second[0])
        d = int(second[1].replace("i", ""))
        print(c)
        print(d)
        p1 = a*c - b*d
        p2 = a*d + c*b
        return str(p1) + "+" + str(p2) + "i"