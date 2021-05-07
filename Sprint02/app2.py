from flask import Flask, render_template, request, redirect, url_for
import math

from numpy import arange


# from matplotlib.pyplot import show, grid, plot, savefig, figsize

app = Flask(__name__)



def f(x):
	return 1 / math.log(x)

def left_rectangle(f, a, b, n):
	h = float((b-a)/float(n))
	sum = 0
	x = a
	for i in range(n):
		sum += f(x)
		x += h
	return sum*h



def rigth_rectangle(f, a, b, n):
	h = float((b-a)/float(n))
	sum = 0
	x = a + h
	for i in range(n):
		sum += f(x)
		print(f(x))
		x += h
	return sum*h


def central_rectangle(f, a, b, n):
	h = float((b-a)/float(n))
	sum = 0
	for i in range(n):
		sum += f(a + (h * (i+0.5)))
	return sum*h


def trapezium_method(f, a, b, n):
	h = (b - a) / n
	sum = 0.0
	for x in arange(a, b-h, h):
		sum += h*(f(x) + f(x + h)) / 2
	return sum


def simson_method(a, b, n, function):
    h = (b - a) / (2 * n)
 
    tmp_sum = float(function(a)) + float(function(b))
    for i in range(1, 2 * n):
        if i % 2 != 0:
            tmp_sum += 4 * float(function(a + (i * h)))
        else:
            tmp_sum += 2 * float(function(a + (i * h)))
 
    return tmp_sum * h / 3


def euler_method(f, a, b, y0, N):
	h = (b - a) / float(N)
	x0 = a
	f1 = f(x0, y0)
	hf = h * f1
	y1 = 0.0
	y_list = list()
	x_list = list()
	x_list.append(x0)
	y_list.append(y0)
	for i in range(1, N+1):
		print('i', i)
		x0+=h 
		print('x=',x0)
		x_list.append(x0)
		y1 = y0 + hf
		print('y=', y1)
		f2 = f(x0, y1)
		y_list.append(y1)
		print('f(x,y) = ',f2)
		hf1 = h * f2
		print('hf(x, y)',hf1)
		print('===iter===')
		y0 = y1
		hf = hf1

	# plot(x_list, y_list, 'r--')
	# grid()
	# show()
	return y_list


@app.route('/left_rect',  methods=['post', 'get'])
def left_rect():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		A = int(a)
		B = int(b)
		n = int(N)
		if option == '1':
			result = left_rectangle(lambda x: 1/math.log(x), A, B, n)
		if option == '2':
			result = left_rectangle(lambda x: 4*x + 3, A, B, n)
	return render_template('left_rect.html', result=result)

@app.route('/rigth_rect',  methods=['post', 'get'])
def rigth_rect():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		A = int(a)
		B = int(b)
		n = int(N)
		if option == '1':
			result = rigth_rectangle(lambda x: 1/math.log(x), A, B, n)
		if option == '2':
			result = rigth_rectangle(lambda x: 4*x + 3, A, B, n)
	return render_template('rigth.html', result=result)


@app.route('/central_rect',  methods=['post', 'get'])
def central_rect():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		A = int(a)
		B = int(b)
		n = int(N)
		if option == '1':
			result = central_rectangle(lambda x: 1/math.log(x), A, B, n)
		if option == '2':
			result = central_rectangle(lambda x: 4*x + 3, A, B, n)
	return render_template('central.html', result=result)


@app.route('/trapezium',  methods=['post', 'get'])
def trapezium():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		A = int(a)
		B = int(b)
		n = int(N)
		if option == '1':
			result = trapezium_method(lambda x: 1/math.log(x), A, B, n)
		if option == '2':
			result = trapezium_method(lambda x: 4*x + 3, A, B, n)
	return render_template('trapezium.html', result=result)


@app.route('/simson_method',  methods=['post', 'get'])
def simson():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		A = int(a)
		B = int(b)
		n = int(N)
		if option == '1':
			result = simson_method(A, B, n, lambda x: 1/math.log(x))
		if option == '2':
			result = simson_method(A, B, n, lambda x: 4*x + 3)
	return render_template('simson.html', result=result)


@app.route('/euler_method',  methods=['post', 'get'])
def euler():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		y = request.form.get('Y')
		A = int(a)
		B = int(b)
		n = int(N)
		Y0 = int(y)
		if option == '1':
			result = euler_method(lambda x, y: math.pow(x, 2) - 2*y, A, B, Y0 ,n)
		if option == '2':
			result = euler_method(lambda x, y: x + y, A, B, Y0, n)
	return render_template('euler.html', result=result)


@app.route('/second_order',  methods=['post', 'get'])
def second():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		y = request.form.get('Y')
		A = int(a)
		B = int(b)
		n = int(N)
		Y0 = int(y)
		if option == '1':
			result = euler_method(lambda x, y: math.pow(x, 2) - 2*y, A, B, Y0 ,n)
		if option == '2':
			result = euler_method(lambda x, y: x + y, A, B, Y0, n)
	return render_template('second_order.html', result=result)


@app.route('/third_order',  methods=['post', 'get'])
def third():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		y = request.form.get('Y')
		A = int(a)
		B = int(b)
		n = int(N)
		Y0 = int(y)
		if option == '1':
			result = euler_method(lambda x, y: math.pow(x, 2) - 2*y, A, B, Y0 ,n)
		if option == '2':
			result = euler_method(lambda x, y: x + y, A, B, Y0, n)
	return render_template('third_order.html', result=result)


@app.route('/fourth_order',  methods=['post', 'get'])
def fourth():
	result = None
	if request.method == 'POST':
		option = request.form.get('op')
		a = request.form.get('A')
		b = request.form.get('B')
		N = request.form.get('N')
		y = request.form.get('Y')
		A = int(a)
		B = int(b)
		n = int(N)
		Y0 = int(y)
		if option == '1':
			result = euler_method(lambda x, y: math.pow(x, 2) - 2*y, A, B, Y0 ,n)
		if option == '2':
			result = euler_method(lambda x, y: x + y, A, B, Y0, n)
	return render_template('fourth_order.html', result=result)


@app.route('/')
def main_menu():
    return render_template('main_menu.html')