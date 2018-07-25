from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('scratch.html')
@app.route('/weather')
def rand():
    import random
    actions = ['сегодня будет солнечно', 'сегодня будет дождь']
    res = random.randint(0,1)
    if res == 0:
        return render_template('b.html')
    return render_template('v.html')
@app.route('/profile')
def profiel():
    return render_template('a.html')
app.run(debug=True, port=8080)