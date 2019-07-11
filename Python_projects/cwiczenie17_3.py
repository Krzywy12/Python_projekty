import re

line = "Bieg na orientacje dookola  ffffffffffffff ffffffffffffffffff ffffffffffffff miejskiego zoo."

x = re.findall(".oo.*?[ ,.,,]",line)
y = []

for i in x:
    k = i.strip()
    k = k.replace(".","")
    y.append(k)

print(y)

