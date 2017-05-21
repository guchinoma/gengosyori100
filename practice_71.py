import re

stop_list = ["of", "by", "the", "beneath", "whilst"]

def stop_word_search(word, list_stop):
    len_list = len(list_stop)
    for i in xrange(len_list):
        obj = re.findall(list_stop[i], word)
        if obj:
            return True
            break
        else:
            continue

    for j in xrange(len_list):
        str_cap = list_stop[j].title()
        #print str_cap
        obj_1 = re.findall(str_cap, word)
        if obj_1:
            return True
            break
        elif i == len_list:
            return False
        else:
            continue


a = raw_input()

answer = stop_word_search(a, stop_list)

print answer