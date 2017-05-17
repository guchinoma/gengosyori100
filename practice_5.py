import re

s = "I am an NLPer"

def n_gram_word(number, string):
    array = []
    answer_array = []

    array = re.split("\W+", string)
    print array
    string_number = len(array)

    for i in range(number):
        answer_array.append(array[i])

    print answer_array

    for j in range(number, string_number):
        del answer_array[0]
        answer_array.append(array[j])
        print answer_array


def n_gram_letter(number, string):

    answer_array = []

    a = re.sub(r"\W+", "", string)

    string_number = len(a)

    for i in range(number):
        answer_array.append(a[i])

    print answer_array

    for l in range(number, string_number):
        del answer_array[0]
        answer_array.append(a[l])
        print answer_array


n_gram_word(2, s)
n_gram_letter(2, s)
