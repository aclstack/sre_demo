from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    items = (['张三', 'zs'], ['李四', 'ls'], ['王五', 'ww'])
    return render_template('index.html', items=items)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return redirect('http://127.0.0.1:8000', code=302)



@app.route('/welcome.html')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
