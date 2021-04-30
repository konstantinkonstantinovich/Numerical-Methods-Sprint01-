
import numpy
from flask import Flask, render_template, request

import copy

UPLOAD_FOLDER = '/uploads/files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def parse_file():
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



def TakeMatrix(Matrix_a):
	array = Matrix_a[0].split(' ')
	delta1 = list()
	for i in array:
		delta1.append(int(i))
	delta = [[delta1[0], delta1[1], delta1[2]],[delta1[3], delta1[4], delta1[5]], [delta1[6], delta1[7], delta1[8]]]
	return delta


def TakeB(Matrix_b):
	array = Matrix_b[0].split(' ')
	delta1 = list()
	for i in array:
		delta1.append(int(i))
	return delta1



def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def Gauss(A, B):
    column = 0
    while (column < len(B)):
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            return None
        if current_row != column:
            SwapRows(A, B, current_row, column)
        DivideRow(A, B, column, A[column][column])
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        column += 1
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X


# def Jordan_Gauss(A, B):
# 	column = 0
# 	m = len(B)
# 	for i in range(m):
# 		if A[0][0] == 1:
# 			print('Первое значение первой строки == 1')
# 		else:
# 			if A[i][0] == 1:
# 				 SwapRows(A, B, i, 0)
# 	while column < len(B):
# 		for i in range()





def Zeidel(A, b):
	x = [.0 for i in range(len(A))]
	Iteration = 0
	converge = False
	pogr = 0.
	while not converge:
	    x_new = copy.copy(x)
	    for i in range(len(A)):
	        s1 = sum(A[i][j] * x_new[j] for j in range(i))
	        s2 = sum(A[i][j] * x[j] for j in range(i + 1, len(A)))
	        x_new[i] = (b[i] - s1 - s2) / A[i][i]
	    pogr = sum(abs(x_new[i] - x[i])  for i in range(len(A)))
	    converge =  pogr < 1e-6
	    Iteration += 1
	    x = x_new
	return x


@app.route('/')
def hello_world():
    return render_template('main_menu.html')


@app.route('/task_1', methods=['post', 'get'])
def Task_One():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	if request.method == 'POST':
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)
		M3 = numpy.array(array) 
		v3 = numpy.array(array1)
		result = numpy.linalg.solve(M3, v3)

	return render_template('task_1.html', array=array, array1=array1, result=result)


@app.route('/task_2', methods=['post', 'get'])
def Task_Two():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	if request.method == 'POST':
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)
		result = Gauss(array, array1)
	return render_template('task_2.html', array=array, array1=array1, result=result)


@app.route('/task_3', methods=['post', 'get'])
def Task_3():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	if request.method == 'POST':
		a = request.form.get('A')
		b = request.form.get('B')
		if a != None and b != None:
			a_list.append(a)
			b_list.append(b)
			array = TakeMatrix(a_list)
			array1 = TakeB(b_list)
			result = Zeidel(array, array1)
		else:
			result = None
	return render_template('task_3.html', result=result)


@app.route('/upload', methods=['post', 'get'])
def Read_From_File():
	pick = None
	filename= None
	if request.method == 'POST':
		option = request.form.get('op')
		file = request.files['file']
		pick = option
		filename = file
	return render_template('upload_file.html', pick=pick, filename=filename)
