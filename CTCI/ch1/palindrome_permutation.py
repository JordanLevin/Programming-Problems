from collections import defaultdict

#given a string, return a list of permutations which are palindromes

def palindrome_permutation(string):
    characters = defaultdict(int)
    for c in string:
        characters[c]+=1

if __name__ == '__main__':
    palindrome_permutation(input)
