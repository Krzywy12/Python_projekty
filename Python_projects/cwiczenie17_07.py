import re

line = "Kocham $ f"

m = re.findall("\$",line,re.IGNORECASE)

print(m)
