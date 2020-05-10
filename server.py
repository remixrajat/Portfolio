from flask import Flask, render_template,url_for,request,redirect
import csv
import smstexter
app = Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)

@app.route('/')
def index():
    return render_template('index.html')



def write_to_file(data):
    with open('database.txt','a') as database:
        email = data['Email']
        subject = data['subject']
        details = data['details']
        file = (f'\n email = {email},subject = {subject},details = {details}')
        database.write(str(file))

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data['Email']
        subject = data['subject']
        details = data['details']
        spamwriter = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,details])

@app.route('/submit_request', methods=['POST', 'GET'])
def submit_request():
    if request.method == 'POST':
        # email = request.form['email']
        # subject = request.form['subject']
        # details = request.form['details']
        data = request.form.to_dict()
        write_to_csv(data)
        smstexter.messege()
        return redirect('/thankyou.html')
    else:
        return redirect('/tryagain.html')



# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')