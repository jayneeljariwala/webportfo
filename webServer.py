from flask import Flask,request,render_template,url_for,redirect
import csv
app=Flask(__name__)
@app.route('/')
def my_home():
    return render_template('index.html')
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as db:
        email=data['email']
        subject=data['subject']
        message=data['Message']
        csv_writer=csv.writer(db,delimiter=',',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
@app.route('/submit_form',methods=['POST','GET'])
def submitform():
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'