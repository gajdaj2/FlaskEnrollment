import json

from application import app
from flask import render_template, request, Response


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", login=False, index=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    coursesData2 = [
        {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
         "term": "Spring"},
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
         "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                           "term": "Fall, Spring"},
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
         "term": "Fall"}]

    return render_template("course_offerings.html", coursesData=coursesData2, courses=True, term=term)


@app.route("/register")
def register():
    return render_template("register.html", login=False, register=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=True, data={"id": id, "title": title, "term": term})


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/api/")
@app.route("/api/<idx>")
def api_courses(idx=None):
    coursesData2 = [
        {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
         "term": "Spring"},
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
         "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                           "term": "Fall, Spring"},
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
         "term": "Fall"}]
    jdata = None
    if idx == None:
        jdata = coursesData2
    else:
        for x in coursesData2:
            if x["courseID"] == idx:
                jdata = x
                break
            else:
                jdata = None

    if jdata is None:
        jdata = [{"error": "No key"}]

    return Response(json.dumps(jdata), mimetype="application/json")
