from flask import Flask

app = Flask(__name__)

@app.route('/math/all', method = ['GET'])
def math_operation(operation):
    num1 = 15
    num2 = 25
    result = None

    if operation == 'add':
        result = num1 + num2

    elif operation == 'sub':
        result = num1 - num2
    
    elif operation == 'multi':
        result = num1 * num2

    elif operation == 'div':
        result = num1 / num2

    return f"{The result of {operation} is {result}}"

if __name__ == '__main__':
    app.run()