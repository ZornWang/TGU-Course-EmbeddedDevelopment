from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='.', static_folder="./static", static_url_path="")


@app.route('/')
@app.route('/index')
def index():
    return render_template('ex5/static/client.html')


@app.route('/lightControl', methods=['POST'])
def lightControl():
    print(request.headers)
    # print(request.stream.read()) # 不要用，否则下面的form取不到数据
    print(request.form)
    print(request.form['loginname'])
    print(request.form.get('loginname'))
    print(request.form.getlist('loginname'))
    print(request.form.get('loginname', default='little apple'))
    return 'welcome'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
