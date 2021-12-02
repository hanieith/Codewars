# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

def high(x):
    lenw = list()
    x = x.split()
    words = ' abcdefghijklmnopqrstuvwxyz'
    c = 0
    for i in x:
        if c != 0:
            lenw.append(c)
            c = 0
        for a in i:
          c += words.find(a)
    lenw.append(c)
    z = lenw.index(max(lenw))
    return x[z]
# for checking
# z = input()
# print(high(z))
