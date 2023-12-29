from flask import Flask, render_template, url_for, request

from datetime import datetime

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html', home = True)

@app.route('/simple')
def simple():
    return render_template("simple.html", home = False)

@app.route('/advanced')
def advanced():
    return render_template("advanced.html", home = False)


@app.route("/calculate", methods = ['post'])
def calculate():
    first_number = float(request.form['firstNumber'])
    operation = request.form['operation']
    second_number = float(request.form['secondNumber'])


    if operation == "plus":
        result = first_number+second_number
    
    elif operation == "minus":
        result = first_number - second_number

    elif operation == "multiply":
        result = first_number*second_number

    elif operation == "divide":
        if second_number == 0:
            result = "You can't divide by zero"
        else:
            result = round(first_number/second_number,3)

    return render_template('simple.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)