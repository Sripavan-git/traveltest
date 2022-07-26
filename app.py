from flask import Flask, render_template, request,redirect,url_for
import mysql.connector as ms
from sec import sec
import smtplib


app = Flask(__name__)
app.register_blueprint(sec, url_prefix="/")
app.debug = True


@app.route("/login", methods=["GET", "POST"])
def log():
    try:
        name = request.form["user"]
        pswd = request.form['psswd']
        mydb = ms.connect(host="localhost", user="root", passwd="862002")
        cu = mydb.cursor()
        cu.execute("use proj")
        # cu.execute("create table logs(username varchar(40),pswd varchar(20))")
        # for i in range(a):
        # print("&"*20)
        cu.execute("insert into logs values(%s,%s)", (name, pswd,))
        mydb.commit()
        cu.close()
        return render_template("welcome.html")
        # print("completion....")
    except Exception as e:
        print(str(e))

    return render_template("login.html")


@app.route("/", methods=["GET", "POST"])  # landing page()
@app.route("/main")
def land():
    return render_template("main.html")


@app.route("/wel", methods=["GET", "POST"])  # welcome page()
def welc():
    return render_template("welcome.html")


# @app.route("/home")
# def homepage():
#     return render_template("navbar.html")


@app.route("/rough")
def rough():
    return render_template("rough.html")


# @app.route("/test")
# def user2():
#     return render_template("aus.html")


@app.route("/signup", methods=["GET", "POST"])
def sign():
    try:
        name = request.form["Fullname"]
        user = request.form["Username"]
        email = request.form["Email"]
        pswd = request.form["Password"]
        conf = request.form["Confirm Password"]
        mydb = ms.connect(host="localhost", user="root", passwd="862002")
        cu = mydb.cursor()
        # print("22"*20)
        cu.execute("use proj")
        # cu.execute("create table signup(username varchar(20),Fullname varchar(20),usermail varchar(30),passwd varchar(20));")
        cu.execute("insert into signup values(%s,%s,%s,%s)",
                   (name, user, email, pswd))
        mydb.commit()
        cu.close()


        # message = "Hey there...You've just signedup to my website Travel Space.... thank you for signing up and explore the world in our view"
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        # server.login("travelspace.mail@gmail.com", "7093350233")
        # server.sendmail("travelspace.mail@gmail.com", email, message)
        #
        return redirect(url_for("log"))


    except Exception as e:
        print(str(e))

    return render_template("signup.html")


# @app.route("/test", methods=["GET", "POST"])
# def test():
#     try:
#         name = request.form["email"]
#         pswd = request.form['psd']
#         mydb = ms.connect(host="localhost", user="root", passwd="root@2002")
#         cu = mydb.cursor()
#         cu.execute("use student")
#         # cu.execute("create table log(username varchar(40),pswd varchar(20))")
#         # a = int(input("enter how many values to insert: "))
#         # for i in range(a):

#         cu.execute("insert into log values(%s,%s)", (name, pswd,))
#         mydb.commit()
#         cu.close()
#         print("completion....")
#     except Exception as e:
#         print(str(e))

#     return render_template("user.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    try:
        name = request.form["name"]
        email = request.form["email"]
        msg = request.form["message"]
        mydb = ms.connect(host="localhost", user="root", passwd="862002")
        cu = mydb.cursor()
        cu.execute("use proj")
        # cu.execute("create table cont(name varchar(20),email varchar(20),message varchar(500))")
        cu.execute("insert into cont values(%s,%s,%s)", (name, email, msg))
        mydb.commit()
        cu.close()
    except Exception as e:
        print(str(e))
    return render_template("contact.html")


# @app.route("/aus")
# def coun1():
#     return render_template("aus.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
