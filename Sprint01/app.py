
import numpy
from flask import Flask, render_template, request


app = Flask(__name__)


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
		M3 = numpy.array(array) # Матрица (левая часть системы)
		v3 = numpy.array(array1) # Вектор (правая часть системы)
		result = numpy.linalg.solve(M3, v3)

	return render_template('task_1.html', array=array, array1=array1, result=result)


