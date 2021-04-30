list_a = list()
list_b = list()
with open('file.txt', 'r') as file:
	line = file.read()[3:].split('\n')
	for lin in line:
		new_list = lin.split(' ')
		arr = list()
		for i in new_list:
			arr.append(int(i))
		list_a.append(arr)
	for i in list_a:
		list_b.append(i[-1])
		del i[-1]
		

print(line)
print(list_a)
print(list_b)