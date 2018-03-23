﻿from application import app, db
from flask import redirect, render_template, request, url_for
from application.works.models import Work

@app.route("/works", methods=["GET"])
def works_index():
    return render_template("works/list.html", works = Work.query.all())

@app.route("/works/new/")
def works_form():
    return render_template("works/new.html")

# This is just a test functionality that will be edited so as
# to be a bit more useful later. For now this is here just for learning purposes.
@app.route("/works/<work_id>/", methods=["POST"])
def work_reset_description(work_id):

    w = Work.query.get(work_id)
    w.description = "No description has been provided yet."
    db.session().commit()
  
    return redirect(url_for("works_index"))

@app.route("/works/new/", methods=["POST"])
def works_create():
    w = Work(request.form.get("name"), request.form.get("published"), request.form.get("description"))
    
    db.session().add(w)
    db.session().commit()
    
    return redirect(url_for("works_index"))