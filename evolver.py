import itertools

program = open('./miller_rabin.pyc', 'rb')
word = program.read(4) #32 bit words -> 4 bytes at a time
words = [word]
while word:
    words.append(word)
    word = program.read(4)

for i in itertools.permutations(words):
    print(i)