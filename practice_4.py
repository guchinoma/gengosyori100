import re

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
number_array = [0, 4, 5, 6, 7, 8, 14, 15, 18]
answer_dict = {}

a = re.split('\W+', s)
del a[-1]
a_number = len(a)

for i in range(a_number):
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        letter = a[i]
        letter_answer = letter[0:1]
        answer_dict[letter_answer] = i

    else:
        letter = a[i]
        letter_answer = letter[0:2]
        answer_dict[letter_answer] = i

print answer_dict




