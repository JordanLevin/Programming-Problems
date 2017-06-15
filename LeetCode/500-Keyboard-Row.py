class Solution(object):
    def findWords(self, words):
        top = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        mid = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        bot = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        ret = []
        for word in words:
            if self.word_in_row(top, word):
                ret.append(word)
            elif self.word_in_row(mid, word):
                ret.append(word)
            elif self.word_in_row(bot, word):
                ret.append(word)
        return ret
    def word_in_row(self, row, word):
        ret = True
        for char in word.lower():
            if char not in row:
                ret = False
        return ret
