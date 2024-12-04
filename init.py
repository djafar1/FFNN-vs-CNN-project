import os

from flask import Flask, render_template, redirect, url_for, session, abort, request, flash


app = Flask(__name__)

@app.route("/", methods = ['GET','POST']) 
def model(): 
    if request.method == "POST":
        if(request.form['num'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.form['num']
            return render_template("answer.html", num=number)
    if request.method == 'GET':
        return render_template("index.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)