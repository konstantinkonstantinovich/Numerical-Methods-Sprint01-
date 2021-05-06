from flask import Flask, render_template, request, redirect, url_for
import math

from numpy import arange


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


@app.route('/')
def main_menu():
    return render_template('main_menu.html')