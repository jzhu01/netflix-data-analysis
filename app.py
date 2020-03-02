from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def home():
    return render_template('fullView.html')

@app.route('/individualView')
def singleView():
    return render_template('individual.html')

if __name__ == '__main__':
    app.run(debug=True)