from pymongo import Connection

class Database:
    conn = Connection()
    
    def DbInit(self):
        db = self.conn.smallstuff
        db.workouts.drop()
        db.exercises.drop()
        workouts = db.workouts
        exercises = db.exercises

    def addExercise(self, name):
        self.conn.smallstuff.exercises.insert({'name' : name})
    
    def getAllExercises(self):
        return self.conn.smallstuff.exercises.find()
