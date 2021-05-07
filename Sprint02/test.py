import math
from numpy import arange

from matplotlib.pyplot import show, grid, plot, savefig

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
	step = (max_lim - min_lim) / float(n)
	for x in arange(min_lim, max_lim-step, step):
		integral += step*(f(x) + f(x + step)) / 2
	return integral


def trapezium_method(f, a, b, n):
	h = (b - a) / float(n)
	sum = 0.0
	for x in arange(a, b-h, h):
		sum += h*(f(x) + f(x + h)) / 2
	return sum

 
def simson_method(a, b, n, function):
    h = (b - a) / (2 * float(n))
 
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

	plot(x_list, y_list, 'r--')
	grid()
	savefig('grafic.jpg')
	show()
	return y_list


def runge_kutta_fourth(f, a,b, y_0,n):
    h= (b-a) / float(n)
    y_list = list()
    y_list.append(y_0)
    for i in range (0, n):
        k1=h*f(a,y_0)
        k2=h*f(a+h/2,y_0+k1/2)
        k3=h*f(a+h/2,y_0+k2/2)
        k4=h*f(a+h,y_0+k3)
        y1=y_0+ (k1+2*k2+2*k3+k4) /6
        y_list.append(y1)
        a=a+h
        y_0=y1
    return y_list


def runge_kutta_second(f, a,b, y_0,n):
    h= (b-a) / float(n)
    y_list = list()
    y_list.append(y_0)
    for i in range (0, n):
        k1=h*f(a,y_0)
        k2=h*f(a+h/2,y_0+k1/2)
        y1=y_0+ k2
        y_list.append(y1)
        a=a+h
        y_0=y1
    return y_list



def runge_kutta_third(f, a,b, y_0,n):
    h= (b-a) / float(n)
    y_list = list()
    y_list.append(y_0)
    for i in range (0, n):
        k1=h*f(a,y_0)
        k2=h*f(a+h/2,y_0+k1/2)
        k3=h*f(a+h/2,y_0+k2/2)
        y1=y_0+ (k1+2*k2+2*k3) /6
        y_list.append(y1)
        a=a+h
        y_0=y1
    return y_list


s1 = left_rectangle(lambda x: 1/math.log(x), 2, 5, 5)
print('===============@#@===============')
print(s1)
print(central_rectangle(lambda x: 1/math.log(x), 2, 5, 5))
print('===============@#trapezium@===============')
print(integrate(lambda x: 1/math.log(x) ,2, 5, 5))
print(trapezium_method(lambda x: 1/math.log(x), 2, 5, 10))
# print(sympson( 2, 5, 5, lambda x: 1/math.log(x)))
print('===============@#euler@===============')
print(euler_method(lambda x, y: math.pow(x, 2) - 2*y, 0, 1, 1, 10))
print('===============@#runge_kutta@===============')
print(runge_kutta_fourth(lambda x, y: math.pow(x, 2) - 2*y, 0, 1, 1, 10))
print(runge_kutta_second(lambda x, y: math.pow(x, 2) - 2*y, 0, 1, 1, 10))



