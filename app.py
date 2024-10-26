from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/howto')
def howto():
    return render_template('howto.html')


@app.route('/scenario')
def scenario():
    return render_template('scenario.html')


if __name__ == '__main__':
    app.run(debug=True)
