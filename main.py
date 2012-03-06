from flask import Flask, request, render_template, redirect, url_for
import database
import forms

app = Flask("SmallStuff")
app.debug = True

DB = database.Database()
#DB.DbInit()

LINKS = {
        'workouts' : "/workouts",
        'exercises' : '/exercises',
        'new_workout' : '/new_workout',
        'new_exercise' : '/new_exercise',
        }

@app.route("/exercises")
def exercises():
    return render_template("showallexercises.html", data=DB.exercises.find(), title="SmallStuff", links=LINKS)

@app.route("/workouts")
def workouts():
    return render_template("showallworkouts.html", data=DB.workouts.find(), title="SmallStuff", links=LINKS)

@app.route("/new_exercise", methods = ['GET', 'POST'])
def new_exercise():
    form = forms.NewExerciseForm(request.form)
    if request.method == 'POST':
        DB.exercises.insert({'name' : form.exercise_name.data})
        return redirect(url_for('exercises'))
    return render_template('new_exercise.html', form=form, title="SmallStuff", links=LINKS)

@app.route("/new_workout", methods = ['GET', 'POST'])
def new_workout():
    form = forms.NewWorkoutForm(request.form)
    if request.method == 'POST':
        DB.workouts.insert({'name' : form.workout_name.data, 'exercises' : form.exercise_list.data })
        return redirect(url_for('workouts'))
    return render_template('new_workout.html', form=form, title="SmallStuff", links=LINKS)


@app.route("/")
def index():
    return render_template('basic.html', title="SmallStuff", links=LINKS)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
