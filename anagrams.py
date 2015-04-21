from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'get':
        return render_template('main.html')
    else:
        myLetters = request.form(['letters'])
        myLetters = myLetters.strip()
        myLetters = sorted(myLetters)
        myLetters = myLetters.upper()
        # myLetters = list(myLetters)
        # myLetters = ''.join(sorted(myLetters))
        return render_template('solver.html', myLetters = myLetters)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
