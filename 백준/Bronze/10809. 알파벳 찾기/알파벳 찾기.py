from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

word = input()

for i in alphabet_list:
    print(word.find(i), end=' ')