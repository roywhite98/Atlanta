import re
string = '>WP_048261218.1 sugar-binding protein [Pectobacterium peruviense]'

pattern = re.compile(r'^(\>[\w\.]+)\s([\w\-\s\W]+?)\[([A-Za-z]+[\s]*[A-Za-z]+).*\]$')
a = pattern.match(string)
print(a.group(1))
print(a.group(3))
