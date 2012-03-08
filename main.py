from flask import Flask, request, render_template, redirect, url_for
import database
import forms
from datetime import date

app = Flask("SmallStuff")
app.debug = True

DB = database.Database()
#DB.DbInit()

LINKS = {
        'Workouts' : "/workouts",
        'Exercises' : '/exercises',
        'Create New Workout' : '/new_workout',
        'Add New Exercise' : '/new_exercise',
        }

def get_lastWorksheet(workout_name):
    return max(DB.workout.find({'name' : workout_name}))

@app.route("/exercises")
def exercises():
    return render_template("showallexercises.html", data=DB.exercises.find(), title="SmallStuff", links=LINKS)

@app.route("/workouts")
def workouts():
    return render_template("showallworkouts.html", data=DB.workouts.find(), title="SmallStuff", links=LINKS)

@app.route("/workout/<workout_name>", methods = ['GET', 'POST'])
def workout(workout_name):
    form = forms.WorkoutForm(request.form)
    exercises = map(lambda x: {x : DB.exercises.find_one({'name' : x})['tracking']}, DB.workouts.find_one({'name' : workout_name})['exercises'])
    
    if request.method == 'POST':
        d = {}
        for exercise_d in exercises:
            for exercise in exercise_d:
                d[exercise] = {}
                d[exercise]['journal'] = request.form['%s_journal' % (exercise)]
                for exercise_tracking in exercise_d[exercise]:
                    d[exercise][exercise_tracking] = request.form['%s_%s' % (exercise, exercise_tracking)]
        DB.workout.insert({'date' : form.workout_date.data.isoformat(), 'name' : workout_name,  'journal' : form.workout_journal.data, 'tracking' : d })
        return redirect(url_for('index'))
    data={ 'name' : DB.workouts.find_one({'name' : workout_name})['name'], 'exercises' : exercises }
    return render_template("worksheet.html", data=data, history=get_lastWorksheet(workout_name), form=form, title="SmallStuff", links=LINKS, date=date.today().strftime("%Y-%m-%d"))

@app.route("/new_exercise", methods = ['GET', 'POST'])
def new_exercise():
    form = forms.NewExerciseForm(request.form)
    if request.method == 'POST':
        DB.exercises.insert({'name' : form.exercise_name.data, 'tracking' : form.exercise_tracking.data })
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
