﻿from application import app, db
from flask import render_template, request
from application.works.models import Work

@app.route("/works/new/")
def works_form():
    return render_template("works/new.html")

@app.route("/works/new/", methods=["POST"])
def works_create():
    w = Work(request.form.get("name"), request.form.get("published"), request.form.get("description"))
    
    db.session().add(w)
    db.session().commit()
    
    return "hello world!"