s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

a = s.split()

a_number = []

for i in a:
    number = len(i)
    a_number.append(number)

for j in a_number:
    print j

