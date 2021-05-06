import math
from numpy import arange


# def f(x):
# 	return 1 / math.log(x)

def left_rectangle(f, a, b, n):
	t = float((b-a)/float(n))
	sum = 0
	x = a
	for i in range(n):
		sum += f(x)
		print(f(x))
		x += t
	return sum*t


def central_rectangle(f, a, b, n):
	h = float((b-a)/float(n))
	sum = 0
	for i in range(n):
		sum += f(a + (h * (i+0.5)))
	return sum*h


def integrate(f, min_lim, max_lim, n):
	integral = 0.0
	step = (max_lim - min_lim) / n
	for x in arange(min_lim, max_lim-step, step):
		integral += step*(f(x) + f(x + step)) / 2
	return integral


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

s1 = left_rectangle(lambda x: 1/math.log(x), 2, 5, 5)
print('===============@#@===============')
print(s1)
print(central_rectangle(lambda x: 1/math.log(x), 2, 5, 5))
print('===============@#trapezium@===============')
print(integrate(lambda x: 1/math.log(x) ,2, 5, 5))
print(trapezium_method(lambda x: 1/math.log(x), 2, 5, 10))
print(sympson( 2, 5, 5, lambda x: 1/math.log(x)))

