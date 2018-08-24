from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)


@app.route('/')
def index():
    # Driver code
    return get_host_name_ip()  # Function call
    # return "Welcome to python with flask"


def get_host_name_ip():
    # print('in get ip function')
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        # print("Hostname :  ", host_name)
        # print("IP : ", host_ip
        return render_template('welcome.html', host_name=host_name, host_ip=host_ip)
    except socket.error:
        # if host_ip == '' or host_name == '' :
        no_host = "Unable to get Hostname and IP"
        return render_template('welcome.html', no_host=no_host)


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
        return render_template('employee_details', emp_details=result)
        # return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
