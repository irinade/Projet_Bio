import random
from students_list import students

n =  12
groups = {}
g = 1

while len(students) != 0 :
	i = random.randint(0,len(students) - 1)
	a = students.pop(i)

	if g not in groups :
		groups[g] = []
	groups[g].append(a)

	g += 1
	if g > n:
		g = 1

print(groups)
