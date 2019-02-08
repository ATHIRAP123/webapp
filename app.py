from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "welcome to my website"
@app.route("/home")
def name():
    return "welcome to my home"
@app.route("/about")
def about():
    return "welcome to my about page"
if(__name__=="__main__"):
    app.run(debug=True)