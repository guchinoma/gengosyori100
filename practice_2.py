# -*- coding: utf-8 -*-

s_1 = u"パトカー"
s_2 = u"タクシー"
a = []

length = len(s_1)

for i in range(length):
    a.append(s_1[i])
    a.append(s_2[i])

for j in a:
    j.encode("utf-8").decode("utf-8")
    print j,