# This is to start the Flask Application in Development.
from logging import debug
import os
import csv
from flask import Flask, render_template, send_from_directory, url_for, request
from werkzeug.utils import redirect

app = Flask(__name__)

# Below is the decorator that is available on the Flask object so that it can be executed on every run.


# @app.route("/")
# def hello_world():
#     return "<p>Hello, Manish Gandhi Dodda!</p>"

@app.route('/')
def default_home():
    return render_template('index.html')


@app.route('/<pagename>')
def html_page(pagename=None):
    return render_template(pagename)


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', mode='a') as database:
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Didnot save to database'
    else:
        return 'Something went wrong. Please try again'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
