from flask import Flask,render_template
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('html/index.html')


@app.route('/about')
def about():
    return render_template('html/about.html')


if __name__=="__main__":
    app.run(debug=True)