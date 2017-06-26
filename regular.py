import re

text ='<meta class="name"> GIoi thieu Website kiem tra 100 regular expression </meta>'

d = re.findall(r'\d{1,3}', text)

c = re.findall(r'.*\s([0-9]{1,10})\s.*',text)

print (d, c)
print(type(d[0]), type(c[0]))