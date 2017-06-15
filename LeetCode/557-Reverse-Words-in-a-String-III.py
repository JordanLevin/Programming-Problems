lass Solution(object):
    def reverseWords(self, s):
        result = ""
        word_list = s.split(" ")
        for word in word_list:
            result+=word[::-1] + " "
        return result.strip()
