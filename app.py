from flask import Flask, render_template, redirect, session, url_for, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("purchase", purchase=user))
    else:
        return render_template('main.html')


@app.route('/purchase', methods=["POST", "GET"])
def purchase():
    return render_template('purchase.html')


@app.route('/check', methods=["POST", "GET"])
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
