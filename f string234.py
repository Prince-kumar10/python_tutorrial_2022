import math

p1 = "student "
p4= 26
p2 = "and"
p5 = "is"
p3 = "roll number"
v = "prince is good %s %s %s %s %s"%(p1,p2,p3,p5,p4)
b = v.format()
# print(b)

# THIS IS FUNCTON OF F STRING
v1 = "clock"
v2 = " is "
v3 = "very"
v4 = "nice "
v5 = "and clock"
v6 = "number "
v7 = "is "
v8 = 12


a = f"this {v1} {v2} {v3} {v4} {v5} {v6}{v7}{v8}{math.cos(65)}"
print(a)