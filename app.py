from flask import Flask, render_template
app = Flask(__name__)
app.config.from_pyfile('settings.py')

@app.route('/')
def home():
    return '<h1>Hey there!</h1>'

@app.route('/individualView')
def singleView():
    return render_template('individual.html')

if __name__ == '__main__':
    app.run(debug=True)