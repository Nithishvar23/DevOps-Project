from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result=""

    if request.method=="POST":

        number=int(request.form["number"])

        if number%2==0:
            result=f"{number} is EVEN"

        else:
            result=f"{number} is ODD"

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8777)