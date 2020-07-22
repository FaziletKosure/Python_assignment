sentence = input("Enter a sentence : ")
letter_dict = {}
for i in sentence:
    if i in letter_dict:
        letter_dict[i] += 1
    else:
        letter_dict.update({i: 1})

print(letter_dict)
