import os
import numpy as np
from numpy import array, zeros, diag, diagflat, dot

import numpy

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import copy
from os.path import join, dirname, realpath

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/..')

ITERATION_LIMIT = 1000

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def check_roots(A, B, x):
	result=list()
	answer = list()
	message = None
	print(x)
	print(A)
	print(B)
	for row in range(len(A)):
		line_result = 0.0
		for col in range(len(A)):

			check = A[row][col] * x[col]
			line_result += check

		result.append(round(line_result))
	print(result)
	for i in range(len(result)):
		if result[i] == B[i]:
			answer.append(True)
		else:
			answer.append(False)
		print(answer)
	if len(answer) == 3:

		if answer == [True, True, True]:
			message = 'Root is correct!'
		else:
			message = 'Root is incorrect!'
	else:
		if answer == [True, True]:
			message = 'Root is correct!'
		else:
			message = 'Root is incorrect!'

	return message



def dd(X):
    result = None
    D = np.diag(np.abs(X)) # Find diagonal coefficients
    S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        result = 'Matrix is diagonally dominant!'
    else:
        result = 'Matrix is not diagonally dominant!'
    return result


def Jacobi(A, b):
	x=None
                                                                                                                                                     
	if x is None:
		x = zeros(len(A[0]))   

	D = diag(A)
	print(D)
	print(diagflat(D))
	R = A - diagflat(D) 

	for i in range(ITERATION_LIMIT):
		x = (b - dot(R,x)) / D
	return x.tolist()


def Jordan_Causs(n, a, b):
	j = 0
	for i in a:
		length = len(b)
		i.append(b[j])
		j+=1

	x = np.zeros(n)
	for i in range(n):
	    if a[i][i] == 0.0:
	        sys.exit('Divide by zero detected!')
	        
	    for j in range(n):
	        if i != j:
	            ratio = a[j][i]/a[i][i]

	            for k in range(n+1):
	                a[j][k] = a[j][k] - ratio * a[i][k]


	for i in range(n):
	    x[i] = a[i][n]/a[i][i]

	return x



def TakeMatrix(Matrix_a):
	array = Matrix_a[0].split(' ')
	delta1 = list()
	for i in array:
		delta1.append(int(i))
	print(delta1)
	size = len(delta1)
	line1 = list()
	line2 = list()
	line3 = list()
	line4 = list()
	delta = list()
	if size == 9:
		for i in delta1[:3]:
			line1.append(i)
		delta.append(line1)
		for i in delta1[3:6]:
			line2.append(i)
		delta.append(line2)
		for i in delta1[6:9]:
			line3.append(i)
		delta.append(line3)
	if size == 4:
		for i in delta1[:2]:
			line1.append(i)
		delta.append(line1)
		for i in delta1[2:]:
			line2.append(i)
		delta.append(line2)
	# delta = [[delta1[0], delta1[1], delta1[2]],[delta1[3], delta1[4], delta1[5]], [delta1[6], delta1[7], delta1[8]]]
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
	ch = None
	if request.method == 'POST':
		check = request.form.get('check')
		print(check)
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)

		M3 = numpy.array(array) 
		v3 = numpy.array(array1)
		result = numpy.linalg.solve(M3, v3)
		if check == 'on':
			ch = check_roots(array, array1, result)
		else:
			pass
	return render_template('task_1.html', array=array, array1=array1, result=result, ch=ch)


@app.route('/task_2', methods=['post', 'get'])
def Task_Two():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	ch= None
	if request.method == 'POST':
		check = request.form.get('check')
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)
		result = Gauss(array, array1)
		if check == 'on':
			ch = check_roots(array, array1, result)
		else:
			pass
	return render_template('task_2.html', array=array, array1=array1, result=result, ch=ch)


@app.route('/task_3', methods=['post', 'get'])
def Task_3():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	ch = None
	check_matrix = None
	if request.method == 'POST':
		check = request.form.get('check')
		a = request.form.get('A')
		b = request.form.get('B')
		if a != None and b != None:
			a_list.append(a)
			b_list.append(b)
			array = TakeMatrix(a_list)
			array1 = TakeB(b_list)
			check_matrix = dd(array)
			result = Zeidel(array, array1)
		else:
			result = None
		if check == 'on':
			ch = check_roots(array, array1, result)
		else:
			pass
	return render_template('task_3.html', result=result, check_matrix=check_matrix, ch=ch)


@app.route('/task_4', methods=['post', 'get'])
def Task_4():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	ch = None
	if request.method == 'POST':
		check = request.form.get('check')
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)
		result = Jordan_Causs(3, array, array1)
		if check == 'on':
			ch = check_roots(array, array1, result)
		else:
			pass
	return render_template('task_4.html', array=array, array1=array1, result=result, ch=ch)


@app.route('/task_5', methods=['post', 'get'])
def Task_5():
	a_list = list()
	b_list = list()
	array = []
	array1 = []
	result = []
	ch = None
	check_matrix = None
	if request.method == 'POST':
		check = request.form.get('check')
		a = request.form.get('A')
		b = request.form.get('B')
		a_list.append(a)
		b_list.append(b)
		array = TakeMatrix(a_list)
		array1 = TakeB(b_list)
		check_matrix = dd(array)
		result = Jacobi(array, array1)
		if check == 'on':
			ch = check_roots(array, array1, result)
		else:
			pass
	return render_template('task_5.html', result=result, check_matrix=check_matrix, ch=ch)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['post', 'get'])
def Read_From_File():
	pick = None
	filename= None
	list_a = list()
	list_b = list()
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			with open('./uploads/'+filename, 'r') as file:
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
		pick = option	
		print(pick)		
		if pick == '1':
			M3 = numpy.array(list_a) 
			v3 = numpy.array(list_b)
			result = numpy.linalg.solve(M3, v3)
		if pick == '2':
			result = Gauss(list_a, list_b)
		if pick == '3':
			result = Zeidel(list_a, list_b)
		if pick == '4':
			result = Jordan_Causs(3, list_a, list_b)
		if pick == '5':
			result = Jacobi(list_a, list_b)
			print(result)
	return render_template('upload_file.html', pick=pick, list_a=list_a, list_b=list_b, result=result)



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
