
from flask import Flask, request, render_template
app = Flask(__name__)
'''@app.route('/')
def index():
    return ' this is index page0'
@app.route('/a1')
def a1():
    return '<h2>this is second page</h2>'
@app.route('/profile/<username>')
def profle(username):
    return "hey there is %s" %username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "post id is%s" % post_id
@app.route('/')
def index():
    return 'method used : %s' % request.method
@app.route('/bacon', methods=['GET' ,'POST'])
def bacon():
    if request.method == 'POST':
        return "your are using POST"
    else:
        return "your are using GET"
@app.route('/profile/<name>')
def profile(name):
    return render_template('log.html', name=name)
@app.route('/')
@app.route("/<user>")
def index(user=None):
    return render_template('user.html',user=user)
@app.route("/shoping")
def shoping():
    food = ['banaba' , 'apple' , 'mango']
    return render_template('shoping.html' , food=food)'''
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    age = request.form['age']
    db = request.form['dateofbirth']
    return render_template('pass.html', n=name, age=age, db=db)
if __name__ == "__main__":
    app.run(debug=True)

