from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/greeting")
def greeting():
    return """
    <h1>hi</h1>
    <ul>
        <li>1</il>
        <li>2</il>
        <li>3</il>
    </ul>
    """
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/lunch")
def lunch():
    menus = ["짜장면","투움바파스타","김치찜","굴국밥","만두라면"]
    pick = random.choice(menus)
    return render_template("lunch.html", pick=pick)

@app.route("/student/<string:name>")
def student(name):
    return render_template("student.html",name = name)

@app.route("/cube/<int:num>")
def cube(num):
    num = num**3
    return render_template("cube.html", num = num)

@app.route("/search")
def naver():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
