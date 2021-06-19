from flask import Flask,render_template, request
from simpleeval import simple_eval
from math import *


app=Flask(__name__)




def calculator(expr):
	try:
		inputs = expr.split()
		output = []

		for i in inputs:
			if i.startswith('√'):
				i = sqrt(float(i.replace('√', '')))

			output.append(str(i))

		c=''.join(output)
		return str(simple_eval(c))
	except SyntaxError:
		return "Please Enter Correctly"
	except ZeroDivisionError:
		return "Can't divide by Zero"


@app.route('/')
def random():
	return render_template('entry.html')




@app.route('/',methods=['POST'])
def calculate():
	if request.method == "POST":
		expr=request.form['submit_action']
		results=calculator(expr)

		return render_template('result.html',result=results)

@app.route('/',methods=['POST'])
def newone():
	if request.method == "POST":
		expr=request.form['submit_action']
		results=calculator(expr)

		return render_template('result.html',result=results)

if __name__ == '__main__':
    app.run(debug=True)