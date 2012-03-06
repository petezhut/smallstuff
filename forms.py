from wtforms import Form, TextField, SelectMultipleField

class NewExerciseForm(Form):
    exercise_name = TextField("Exercise Name")
    exercise_list = SelectMultipleField("Exercise List", choices=[( 1, 'Exercise 1'), (2, 'Exercise 2'), (3, 'Exercise 3')])
