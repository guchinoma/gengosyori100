# -*- coding: utf-8 -*-

s = u"パタトクカシーー"
print "%s" % s
s_len = len(s)
s_len = s_len/2
a = []
for i in range(s_len):
    element = i * 2 + 1
    a.append(s[element])

for j in a:
    j.encode("utf-8").decode("utf-8")
    print j, 
