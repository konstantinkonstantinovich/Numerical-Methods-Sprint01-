from flask import Flask, render_template, request, redirect, url_for
import math




app = Flask(__name__)


def parse_string(A_set):
	first_step = A_set.split(' ')
	result_list = list()
	for i in first_step:
		result_list.append(int(i))

	result = list(set(result_list))
	result.sort()
	return result



def alg_association(A_set, B_set):
	C_set = list()
	i = 0
	j = 0
	while A_set and B_set:
		if A_set[i] < B_set[i]:
			d = A_set[i]
			del A_set[i]
		elif A_set[i] > B_set[i]:
			d = B_set[j]
			del B_set[i]
		else:
			d = A_set[i]
			del A_set[i]
			del B_set[j]
		C_set.append(d)	
	if A_set != None:
		C_set = C_set + A_set
	if B_set != None:
		C_set = C_set + B_set
	return C_set


def alg_intersections(A_set, B_set):
	C_set = list()
	i = 0
	j = 0
	d = None
	while A_set and B_set:
		if A_set[i] < B_set[i]:
			del A_set[i]
		elif A_set[i] > B_set[i]:
			del B_set[i]
		else:
			C_set.append(A_set[i])
			del A_set[i]
			del B_set[j]
	return C_set


def alg_entry(A_set, B_set):
	i = 0
	j = 0
	while A_set and B_set:
		if A_set[i] < B_set[i]:
			return False
		elif A_set[i] > B_set[i]:
			del B_set[i]
		else:
			del A_set[i]
			del B_set[j]
	return True


def alg_difference(A_set, B_set):
	C_set = list()
	i = 0
	j = 0
	while A_set and B_set:
		if A_set[i] < B_set[i]:
			C_set.append(A_set[i])
			del A_set[i]
		elif A_set[i] > B_set[i]:
			del B_set[i]
		else:
			del A_set[i]
			del B_set[j]
	if A_set:
		C_set = C_set + A_set
	return C_set	


def alg_symmetrical_difference(A_set, B_set):
	C_set = list()
	i = 0
	j = 0
	while A_set and B_set:
		if A_set[i] < B_set[i]:
			C_set.append(A_set[i])
			del A_set[i]
		elif A_set[i] > B_set[i]:
			C_set.append(B_set[j])
			del B_set[i]
		else:
			del A_set[i]
			del B_set[j]
	if A_set:
		C_set = C_set + A_set
	if B_set:
		C_set = C_set + B_set
	return C_set	



@app.route('/', methods=['post', 'get'])
def main():
	result = None
	title = None
	if request.method == 'POST':
		a = request.form.get('A')
		b = request.form.get('B')
		option = request.form.get('op')
		print(a)
		print(b)
		list_a = parse_string(a)
		list_b = parse_string(b)
		l_a= parse_string(a)
		l_b = parse_string(b)
		print(list_a)
		print(list_b)
		if option == '1':
			title = 'Combining A and B!'
			result = alg_association(list_a, list_b)
			img = 'static/images/asso.jpg'
		if option == '2':
			result = alg_intersections(list_a, list_b)
			img = 'static/images/a1.jpg'
			title = 'Intersection of A and B!'
		if option == '3':
			title = 'Inclusion of A into B!'
			if alg_entry(list_a, list_b) == False:
				result = 'A is not a subset of B.'
				img = ''
			else: 
				result = 'A is a subset of B.'
				img = 'static/images/download.jpg'
		if option == '4':
			title = 'Inclusion of A into B!'
			if alg_entry(list_b, list_a) == False:
				result = 'B is not a subset of A.'
				img = ''
			else: 
				result = 'B is a subset of A.'
				img = 'static/images/download.jpg'
		if option == '5':
			title = 'Difference between A and B!'
			result = alg_difference(list_a, list_b)
			img = 'static/images/1.jpg'
			print(alg_difference(list_a, list_b))
		if option == '6':
			title = 'Difference between B and A!'
			result = alg_difference(list_b, list_a)
			img = 'static/images/2.jpg'
			print(alg_difference(list_b, list_a))
		if option == '7':
			title = 'Symmetric difference between A and B!'
			result = alg_symmetrical_difference(list_a, list_b)
			img = 'static/images/images.png'
			print(alg_symmetrical_difference(list_a, list_b))
	return render_template('main.html', a=l_a, b=l_b, result=result, img=img, title=title)





