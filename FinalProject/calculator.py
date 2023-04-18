from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

@app.route('/')
def home():
    return render_template('calculate.html')

@app.route('/result', methods=['POST'])
def result():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operator = request.form['operator']
    result = calculate(num1, num2, operator)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

