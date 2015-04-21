from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        myLetters = request.form['letters']
        myLetters = ''.join(sorted(myLetters))
        myLetters = myLetters.strip()

        myWords = []
        myLetterList = list(myLetters)
        lettersLength = len(myLetterList)

        for x in myLetterList:
            for word in open("/usr/share/dict/words"):
                if x in word and word <= lettersLength:
                    myWords.append(word)
        return render_template('solver.html', myLetters = myLetters, myWords=myWords)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)