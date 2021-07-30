from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('dib_79.pkl')

@app.route('/')

def landing():
    return 'Here we go!'

@app.route('/home')

def home():
    return render_template('home.html')

@app.route('/welcome')

def welcome():
    return render_template('welcome.html')

@app.route('/blogs', methods = ['POST'])

def blogs():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    pred = model.predict([[int(preg) ,int(plas) , int(pres) , int(skin) , int(test) , int(mass) , int(pedi) , int(age)]])

    if pred[0] == 1:
        output = 'diabetic'
    else:
        output = 'not diabetic'
    
    return render_template('blogs.html', predicted_text = f'You are {output}.')

@app.route('/english')

def english():
    return 'Waddup?!'

@app.route('/hindi')

def hindi():
    return 'Namaste!'

@app.route('/french')

def french():
    return 'Bon Jour!'

@app.route('/filipino')

def filipino():
    return 'Mabuhay!'

@app.route('/chinese')

def chinese():
    return 'Ni hao!'

@app.route('/thai')

def thai():
    return 'Sah wah dee ka!'

@app.route('/hawaiian')

def hawaiian():
    return 'Mahaalo!'

@app.route('/japanese')

def japanese():
    return 'Ari Gato!'


if __name__ == '__main__':
    app.run(debug=True)
