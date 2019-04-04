from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '3.1415926'


menu_dict = {
    "主菜单1": {
        "子菜单1": "/deploy/1",
        "子菜单2": "/deploy/2",
        "子菜单3": "/deploy/3"
    },
    "主菜单2": {
        "子菜单1": "/user/1",
        "子菜单2": "/user/2",
        "子菜单3": "/user/3"
    },
    "主菜单3": {
        "子菜单1": "/monitor/1",
        "子菜单2": "/monitor/2",
        "子菜单3": "/monitor/3"
    }
}


@app.route('/')
def hello_world():
    items = (['张三', 'zs'], ['李四', 'ls'], ['王五', 'ww'])
    return render_template('index.html', items=items, menus=menu_dict)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        password = request.form.get('password')
        if user == '1' and password == '1':
            return render_template('index.html')
        flash('用户名或密码错误')
        return render_template('login.html')


@app.route('/welcome.html')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
