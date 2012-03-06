from flask import Flask, request, render_template, redirect, url_for
import database
import forms

app = Flask("SmallStuff")
app.debug = True

DB = database.Database()
DB.DbInit()
@app.route("/")
def index():
    return render_template('basic.html', title = "SmallStuff")

@app.route("/showall")
def showall():
    return render_template("showall.html", data=DB.exercises.find())

@app.route("/new_exercise", methods = ['GET', 'POST'])
def new_exercise():
    form = forms.NewExerciseForm(request.form)
    if request.method == 'POST':
        DB.exercises.insert({'name' : form.exercise_name.data})
        return redirect(url_for('showall'))
    return render_template('new_exercise.html', form=form)


if __name__ == '__main__':
    app.run()
