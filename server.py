from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)


def csv_file(data):
    with open('database.csv', mode='a', newline='\n') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            csv_file(data)
            return redirect('/thankyou.html')
        except:
            return 'Data didn\'t save to database'
    else:
        return 'Something went wrong. The Autobots lost, the future is dismal. Only you can save us now.'