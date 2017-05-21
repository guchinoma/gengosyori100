import random
import re

file_path_positive = "rt-polaritydata/rt-polaritydata/rt-polarity.neg"
file_path_negative = "rt-polaritydata/rt-polaritydata/rt-polarity.pos"

file_name_txt = "sentiment.txt"

pattern_1 = "-1."
pattern_2 = "+1."

counter_pos = 0
counter_neg = 0

str_1 = []
str_2 = []
str_a = []
str_b = []

with open(file_path_negative, "r") as f:
    
    str_1 = f.readlines()

with open(file_path_positive, "r") as f:
    
    str_2 = f.readlines()


for i in str_1:
    str_a.append("-1 " + i)

for j in str_2:
    str_b.append("+1 " + j)

str_end = str_a + str_b
random.shuffle(str_end)

with open("sentiment.txt", "w") as f:
    for k in str_end:
        f.write(k)


with open("sentiment.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
         obj_n = re.match(pattern_1, l)
         if obj_n:
             counter_neg = counter_neg + 1
         else:
             counter_pos = counter_pos + 1

print counter_neg
print counter_pos













