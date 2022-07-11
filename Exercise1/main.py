import collections

# n is how many words there are
n = int(input())
dict = collections.OrderedDict()

for i in range(n):
    word = input()
    if word in dict:     #this part adds words to dictionary and counts them
        dict[word] += 1
    else:
        dict[word] =1

print(len(dict))

for words,nums in dict.items():
    print(nums,end = " ")

