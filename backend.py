from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Here you can process any form data if needed
    return redirect(url_for('index_page'))

@app.route('/home_page')
def index_page():
  return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
