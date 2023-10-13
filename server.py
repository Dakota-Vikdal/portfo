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
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(f'{data}\n')
    
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        csv_file(data)
        # with open('database.txt', 'a') as file:
        #     file.write(f'{data}\n')
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. The Autobots lost, the future is dismall. Only you can save us now.'