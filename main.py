print ('[1] Circle')
print ('[2] Diamond')
print ('[3] Square')
print ('[4] Triangle')
print ('[5] Pentagon')
inpt = int(input('Enter no. of shape'))
if inpt == 1:
    with open('circle.py') as c:
        exec(c.read())
if inpt == 2:
    with open('diamond.py') as d:
        exec(d.read())
if inpt == 3:
    with open('square.py') as s:
        exec(s.read())
if inpt == 4:
    with open('trianlge.py') as t:
        exec(t.read())
if inpt == 5:
    with open('pentagon.py') as p:
        exec(p.read())
