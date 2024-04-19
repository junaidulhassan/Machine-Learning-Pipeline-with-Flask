from flask import Flask
from flask import render_template,request


app = Flask(__name__)


@app.route("/form",methods=["POST","GET"])
def form():
    if request.method=="GET":
        return render_template("app.html")
    else:
        num1 = float(request.form["number1"])
        num2 = float(request.form["number2"])
        sum = (num1+num2)

        return render_template("app.html",score=sum)


if __name__=="__main__":
    app.run(debug=True)
