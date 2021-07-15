from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import db
from models import Todo
app = Flask(__name__)



@app.route('/edit')
def home():
    todo_list = db.session.query(Todo).all()
    return render_template("base.html", todo_list=todo_list)

@app.route('/')
def list():
    todo_list = db.session.query(Todo).all()
    return render_template("list.html", todo_list=todo_list)

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = db.session.query(Todo).filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))



if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    run()