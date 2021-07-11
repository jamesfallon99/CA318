subnet = "255.255.255.0"
print(int(subnet.split(".")[2]))



word = "sun"
word = word.split()
word[0] = 'a'

letters = "abcdefghijklmnopqrstuvwxyz"

word = "sun"
lis = []
lis.append(word)
i = 0
j = 0
while j < len(word):
    while i < len(letters):
        new_word = lis[0].replace(lis[0][j], letters[i])
        i += 1
        lis.append(new_word)
    j += 1
    i = 0
for new_word in lis:
    if new_word == word:
        lis.remove(new_word)
print(lis)
i = 0
while i < len(lis):
    i += 1
print(i)