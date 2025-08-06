from collection import Counter
my_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
print(Counter(my_list))

my_list1 = ['a','a','b','b','b','c','c','c','c']
print(Counter(my_list1))

Sentence = 'A quick brown fox jumps over the lazy dog'
words = Sentence.split()
print(Counter(words))

letters = 'aaabbbbbcccccddddddddddeeeeeeffffffffggggggggghhhhhhiiiiii'
c = Counter(letters)
print(Counter(c))
print(c.most_common(3))
print(list(c))     # this shows the list in the string
print(set(c))     # this shows the set in the string
print(dict(c))    # this shows the dictionary in the string
print(c.items())  # this shows the items in the string
print(c.values()) # this shows the values in the string
print(c.keys())   # this shows the keys in the string
print(c['a'])     # this shows the number of a in the string
