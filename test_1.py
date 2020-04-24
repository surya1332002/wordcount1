"""
asd 2
sdf 2
"""

data = {}
x = "asd sdf asd sdf"
x = x.split(" ")
for i in x:
    if i not in data.keys():
        data[i] = 1
    else:
        data[i] += 1

print(data)


a = "1 2 3 4 5"
x = [int(i) for i in a.split(" ")]
print(sum(x))