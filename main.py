from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to python with flask"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/FlaskTutorial', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        return render_template('success.html', email=email)
    else:
        pass


@app.route('/employees', methods=['GET'])
def employee():
    if request.method == 'GET':
        result = {'employee_id': 1, 'employee_name': "Kadar Khan"}
        return render_template('employee_details.html', emp_details=result)
        # return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)



