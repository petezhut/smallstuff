from flask import Flask, request, render_template
from wtforms import Form, TextField
import database

app = Flask("SmallStuff")
app.debug = True

DB = database.Database()

@app.route("/")
def index():
    return render_template('basic.html', title = "SmallStuff")

@app.route("/greet")
def greet():
    return render_template('new_exercise.html', name = "Jason", title = "SmallStuff")

class NewExerciseForm(Form):
    exercise_name = TextField("Exercise Name")

@app.route("/new_exercise", methods = ['GET', 'POST'])
def new_exercise():
    form=NewExerciseForm(request.form)
    if request.method == 'POST':
        return form.exercise_name.data
    return render_template('new_exercise.html', form=form)


if __name__ == '__main__':
    app.run()
