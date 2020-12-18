from flask import Flask, render_template, redirect, session, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/purchase')
def purchase():
    return render_template('purchase.html')


@app.route('/check')
def check():
    return render_template('check.html')


# @app.route('/', methods=['GET', 'POST'])
# def base():
#     if request.method == "POST":
#         return render_template('purchase.html')


# @app.route('/purchase', methods=['GET', 'POST'])
# def purchase():
#     return render_template('purchase.html')


if __name__ == '__main__':
    app.run()
