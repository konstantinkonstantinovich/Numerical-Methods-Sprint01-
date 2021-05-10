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





@app.route('/', methods=['post', 'get'])
def main():
	result = None
	if request.method == 'POST':
		a = request.form.get('A')
		b = request.form.get('B')
		option = request.form.get('op')
		print(a)
		print(b)
		list_a = parse_string(a)
		list_b = parse_string(b)

	return render_template('main.html', a=list_a, b=list_b)