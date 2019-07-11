import re

t = "__jeden____dwa____trzy__"

results = re.findall("__.*?__", t)

for match in results:
    print(match)
