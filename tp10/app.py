from flask import Flask,render_template,redirect
from TodoDAO import TodoDAO

app = Flask(__name__)
@app.route("/")
def index():

    dao =TodoDAO("todos_db.db")

    l=dao.findAll()

    return render_template('todo_list.html',todos=l)


@app.route("/delete/<id>")
def delete(id):
    dao =TodoDAO("todos_db.db")
    dao.delete(id)
    return redirect('/')
