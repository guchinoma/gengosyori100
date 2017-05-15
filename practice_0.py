s = "stressed"
s_a = []
l = len(s)

for i in range(l):
    letter = s[-i - 1]
    s_a.append(letter)

print "%s" % s_a


