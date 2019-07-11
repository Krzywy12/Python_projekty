import re

line = "Piekny jest lepszy niz brzydki,"

matches = re.findall("piekny",line,re.IGNORECASE)
print(matches)
