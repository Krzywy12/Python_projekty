import re

x = "__dd_dd__ddddd__dd__"

x = re.findall("__.*?__",x)
print(x)
