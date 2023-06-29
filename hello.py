from flask import Flask, render_template
import operations as oper
import argparse

app = Flask(__name__)

@app.route('/')

def hello_world():
    parser = argparse.ArgumentParser()
    # indicate the first value
    parser.add_argument('--v1', type=int, required=True)
    # indicate the second value
    parser.add_argument('--v2', type=int, required=True)
    # indicate operation to perform
    parser.add_argument('--op', type=str, choices=['/', '*', '+', '-'], default='+')

    args = parser.parse_args()

    value_1 = args.v1
    value_2 = args.v2
    operation = args.op

    result = oper.main(value_1, value_2, operation)

    return render_template('index.html', v1=value_1, v2=value_2, op=operation, res=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
