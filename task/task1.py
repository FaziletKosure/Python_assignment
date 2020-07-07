
sentence = input('Enter a sentence :')
sentence_list = sentence.split()
print(sentence_list)
i = len(sentence_list)
j = 0
word = ''
while j < i:
    if len(sentence_list[j]) > len(word):
        word = sentence_list[j]
    j += 1
print('The longest word is', word, 'and the length is', len(word))
