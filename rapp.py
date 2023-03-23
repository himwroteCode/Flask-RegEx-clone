import re
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1> hello wwelcome to string regex checker </h1>"
    #return render_template('home page.html')
    return render_template('regform.html')
    
     
@app.route('/result')
def result():
    return render_template('result.html') 
 
 
@app.route('/regex',methods =['POST', 'GET'])
def regex():
    if request.method=="POST":
        target_string  = request.form['target_string']      #str(input("enter the string you want to check reg ex for : "))
        regex_ptrn = request.form['regex_ptrn']       #input(" enter the regex patttern that you want to check  fo r your string : ")
        matched_string = re.findall(regex_ptrn, target_string)
        return render_template('regform.html', matched_string=matched_string)
          #('your matched string is ',matched_string)


if __name__=='__main__':
    app.run(debug=True)