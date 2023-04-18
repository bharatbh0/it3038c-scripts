from flask import Flask, render_template, request

app = Flask(__name__)

##function calculate is define to perfrom basic operations here only +, -, *, and /
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

##Send the user to homepage 
@app.route('/')
def home():
    return render_template('calculate.html')

##Once the user chooses the choices result then excuates showing the answer
@app.route('/result', methods=['POST'])
def result():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operator = request.form['operator']
    result = calculate(num1, num2, operator)
    return render_template('result.html', result=result)

##Checks if the current module is the main module and runs the application with debug enabled 
if __name__ == '__main__':
    app.run(debug=True)

