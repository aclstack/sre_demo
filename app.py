from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    items = (['张三', 'zs'], ['李四', 'ls'], ['王五', 'ww'])
    return render_template('index.html', items=items)


@app.route('/welcome.html')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(port=8000)
