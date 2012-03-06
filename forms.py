from wtforms import Form, TextField, SelectMultipleField
import database

class NewExerciseForm(Form):
    exercise_name = TextField("Exercise Name")

class NewWorkoutForm(Form):
    workout_name = TextField("Workout Name")
    exercise_list = SelectMultipleField("Exercise List", choices=map(lambda x: (x['name'], x['name']), database.Database().exercises.find()))
