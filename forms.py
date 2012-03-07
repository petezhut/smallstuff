from wtforms import Form, TextField, SelectMultipleField, DateField, TextAreaField
import database

class NewExerciseForm(Form):
    exercise_name = TextField("Exercise Name")
    exercise_tracking = SelectMultipleField("Exercise Tracking", choices = map(lambda x: (x, x), ['Sets', 'Reps', 'Time', 'Distance', 'Weight']))

class NewWorkoutForm(Form):
    workout_name = TextField("Workout Name")
    exercise_list = SelectMultipleField("Exercise List", choices=map(lambda x: (x['name'], x['name']), database.Database().exercises.find()))

class WorkoutForm(Form):
    workout_date = DateField("Workout Date")
    workout_journal = TextAreaField("Workout Journal")
