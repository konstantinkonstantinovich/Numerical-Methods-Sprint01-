list_a = list()
list_b = list()
with open('file.txt', 'r') as file:
	line = file.read()[2:].split('\n')
	for lin in line:
		new_list = lin.split(' ')
		arr = list()
		for i in new_list:
			arr.append(float(i))
		list_a.append(arr)
	for i in list_a:
		list_b.append(i[-1])
		del i[-1]
		

print(line)
print(list_a)
print(list_b)
print('$==================*$#*=================&')

x = [-1., 1., 3.]
result=list()

for row in range(len(list_a)):
	line_result = 0.0
	for col in range(len(list_a)):
		# print(list_a[row][col], x[col])

		check = list_a[row][col] * x[col]
		line_result += check

	result.append(line_result)

answer = list()
for i in range(len(result)):
	if result[i] == list_b[i]:
		answer.append(True)
	else:
		answer.append(False)

if answer == [True, True, True]:
	print('Root is correct!')

print(answer)
print(result)

print(list_a)




# print('$==================*$#*=================&')


# def SwapRows(A, B, row1, row2):
#     A[row1], A[row2] = A[row2], A[row1]
#     B[row1], B[row2] = B[row2], B[row1]


# def CombineRows(A, B, row, source_row, weight):
#     A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
#     B[row] += B[source_row] * weight


# for row in list_a:
# 	# print(row)
# 	for col in range(len(row)):

# 		length = len(row)
# 		i = 0
# 		while i < length:
# 			if list_a[i][0] == 1:
# 				SwapRows(list_a, list_b, i, 0)
# 			i+=1



# print(list_a)
# print(list_b)
# print('===========================@End swap elements@=====================ap')

# for row in range(len(list_a)):
# 	if row > 0:
# 		for col in range(len(list_a)):
# 			multiplier = -list_a[row][0]
# 			f_row = list_a[0][col] * multiplier
# 			current = list_a[row][col]
# 			current += f_row
# 			list_a[row][col]
			
# 			print('After', current)

# print(list_a)


			